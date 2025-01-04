import json
from unittest.mock import patch

import pytest

from backend.common.frc_api import FRCAPI
from backend.common.futures import InstantFuture
from backend.common.models.event import Event
from backend.common.sitevars.apistatus_fmsapi_down import ApiStatusFMSApiDown
from backend.common.sitevars.fms_api_secrets import (
    ContentType as FMSApiSecretsContentType,
)
from backend.common.sitevars.fms_api_secrets import FMSApiSecrets
from backend.common.storage.clients.in_memory_client import InMemoryClient
from backend.common.urlfetch import URLFetchResult
from backend.tasks_io.datafeeds.datafeed_fms_api import DatafeedFMSAPI


@pytest.fixture(autouse=True)
def reset_gcs_client():
    yield
    InMemoryClient.CLIENT = None


@pytest.fixture()
def fms_api_secrets(ndb_stub):
    FMSApiSecrets.put(FMSApiSecretsContentType(username="zach", authkey="authkey"))


def test_init(ndb_stub):
    with pytest.raises(
        Exception, match="Missing FRC API auth token. Setup fmsapi.secrets sitevar."
    ):
        DatafeedFMSAPI(save_response=True)


@pytest.mark.parametrize(
    "event_code, expected",
    list(Event.EVENT_SHORT_EXCEPTIONS.items()) + [("miket", "miket")],
)
def test_get_event_short_event_first_code_none(event_code, expected):
    event = Event(
        year=2022,
        event_short=event_code,
    )
    assert DatafeedFMSAPI._get_event_short(event.year, event_code, event) == expected


@pytest.mark.parametrize(
    "event_code, expected",
    list(Event.EVENT_SHORT_EXCEPTIONS_2023.items()),
)
def test_get_event_short_2023_event_first_code_none(event_code, expected):
    event = Event(
        year=2023,
        event_short=event_code,
    )
    assert DatafeedFMSAPI._get_event_short(event.year, event_code, event) == expected


def test_get_event_short_event_first_code():
    event = Event(
        year=2020,
        event_short="miket",
        first_code="miket",
    )
    assert (
        DatafeedFMSAPI._get_event_short(event.year, "miket", event) == event.first_code
    )


def test_get_event_short_event_cmp():
    event = Event(year=2022, event_short="arc")
    assert DatafeedFMSAPI._get_event_short(event.year, "arc", event) == "archimedes"


def test_get_event_short_event_cmp_2023():
    event = Event(year=2023, event_short="arc")
    assert DatafeedFMSAPI._get_event_short(event.year, "arc", event) == "arpky"


def test_get_root(fms_api_secrets):
    content = {
        "currentSeason": 2021,
        "maxSeason": 2021,
        "name": "FIRST ROBOTICS COMPETITION API",
        "apiVersion": "3.0",
        "status": "normal",
    }
    response = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/",
        200,
        json.dumps(content),
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(
        FRCAPI, "root", return_value=InstantFuture(response)
    ) as mock_root:
        df.get_root_info().get_result() is None

    mock_root.assert_called_once_with()


def test_get_root_failure(fms_api_secrets):
    content = {}
    response = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/",
        500,
        json.dumps(content),
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(
        FRCAPI, "root", return_value=InstantFuture(response)
    ) as mock_root:
        assert df.get_root_info().get_result() is None

    mock_root.assert_called_once_with()


def test_mark_api_down(fms_api_secrets):
    response1 = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/",
        500,
        "",
    )

    response2 = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/",
        200,
        "{}",
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(FRCAPI, "root", return_value=InstantFuture(response1)):
        assert df.get_root_info().get_result() is None
        assert ApiStatusFMSApiDown.get() is True

    with patch.object(FRCAPI, "root", return_value=InstantFuture(response2)):
        assert df.get_root_info().get_result() == {}
        assert ApiStatusFMSApiDown.get() is False


def test_save_response(fms_api_secrets, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("SAVE_FRC_API_RESPONSE", "true")
    content = {
        "currentSeason": 2021,
        "maxSeason": 2021,
        "name": "FIRST ROBOTICS COMPETITION API",
        "apiVersion": "3.0",
        "status": "normal",
    }
    response = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/root",
        200,
        json.dumps(content),
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(FRCAPI, "root", return_value=InstantFuture(response)):
        df.get_root_info().get_result()

    client = InMemoryClient.get()
    files = client.get_files()
    assert len(files) == 1

    f = client.read(files[0])
    assert f is not None
    assert f == response.content


def test_save_response_unchanged(fms_api_secrets, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("SAVE_FRC_API_RESPONSE", "true")
    content = {
        "currentSeason": 2021,
        "maxSeason": 2021,
        "name": "FIRST ROBOTICS COMPETITION API",
        "apiVersion": "3.0",
        "status": "normal",
    }

    response = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/root",
        200,
        json.dumps(content),
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(FRCAPI, "root", return_value=InstantFuture(response)):
        df.get_root_info().get_result()

    client = InMemoryClient.get()
    files = client.get_files()
    assert len(files) == 1
    f_name = files[0]

    with patch.object(FRCAPI, "root", return_value=InstantFuture(response)):
        df.get_root_info().get_result()

    # Since the content didn't change, we shouldn't have written another
    assert client.get_files() == [f_name]


def test_save_response_updated(fms_api_secrets, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("SAVE_FRC_API_RESPONSE", "true")
    content = {
        "currentSeason": 2021,
        "maxSeason": 2021,
        "name": "FIRST ROBOTICS COMPETITION API",
        "apiVersion": "3.0",
        "status": "normal",
    }

    response = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/root",
        200,
        json.dumps(content),
    )

    df = DatafeedFMSAPI(save_response=True)
    with patch.object(FRCAPI, "root", return_value=InstantFuture(response)):
        df.get_root_info().get_result()

    client = InMemoryClient.get()
    files = client.get_files()
    assert len(files) == 1

    content2 = {
        "currentSeason": 2021,
        "maxSeason": 2021,
        "name": "SECOND ROBOTICS COMPETITION API",
        "apiVersion": "3.0",
        "status": "normal",
    }
    response2 = URLFetchResult.mock_for_content(
        "https://frc-api.firstinspires.org/v3.0/root",
        200,
        json.dumps(content2),
    )
    with patch.object(FRCAPI, "root", return_value=InstantFuture(response2)):
        df.get_root_info().get_result()

    # Since the content is different, we should have two items
    files = client.get_files()
    assert len(files) == 2

    f = client.read(files[0])
    assert f is not None
    assert f == response.content

    f2 = client.read(files[1])
    assert f2 is not None
    assert f2 == response2.content
