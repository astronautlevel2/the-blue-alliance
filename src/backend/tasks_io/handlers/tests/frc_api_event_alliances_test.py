import datetime
from typing import Dict, Optional
from unittest import mock

from freezegun import freeze_time
from google.appengine.ext import testbed
from werkzeug.test import Client

from backend.common.consts.event_type import EventType
from backend.common.futures import InstantFuture
from backend.common.models.alliance import EventAlliance
from backend.common.models.event import Event
from backend.common.models.event_details import EventDetails
from backend.tasks_io.datafeeds.datafeed_fms_api import DatafeedFMSAPI


def create_event(
    official: bool,
    end_date: Optional[datetime.datetime] = None,
    remap_teams: Optional[Dict[str, str]] = None,
) -> None:
    Event(
        id="2020nyny",
        year=2020,
        event_short="nyny",
        event_type_enum=EventType.REGIONAL,
        start_date=datetime.datetime(2020, 4, 1),
        end_date=end_date or datetime.datetime(2020, 4, 2),
        official=official,
        remap_teams=remap_teams,
    ).put()


def test_enqueue_bad_when(tasks_client: Client) -> None:
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/asdf")
    assert resp.status_code == 404


@freeze_time("2020-4-1")
def test_enqueue_current(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=True)
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/now")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 1

    expected_keys = ["2020nyny"]
    assert [f"/tasks/get/fmsapi_event_alliances/{k}" for k in expected_keys] == [
        t.url for t in tasks
    ]


@freeze_time("2020-4-1")
def test_enqueue_current_skips_unofficial(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=False)
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/now")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 0


@freeze_time("2020-4-1")
def test_enqueue_current_no_output_in_taskqueue(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    resp = tasks_client.get(
        "/tasks/enqueue/fmsapi_event_alliances/now",
        headers={"X-Appengine-Taskname": "test"},
    )
    assert resp.status_code == 200
    assert len(resp.data) == 0

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 0


@freeze_time("2020-4-1")
def test_enqueue_last_day_only(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=True, end_date=datetime.datetime(2020, 4, 1))
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/last_day_only")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 1

    expected_keys = ["2020nyny"]
    assert [f"/tasks/get/fmsapi_event_alliances/{k}" for k in expected_keys] == [
        t.url for t in tasks
    ]


@freeze_time("2020-4-1")
def test_enqueue_last_day_only_skips_unofficial(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=False)
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/last_day_only")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 0


def test_enqueue_explicit_year(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=True)
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/2020")
    assert resp.status_code == 200

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 1
    assert tasks[0].url == "/tasks/get/fmsapi_event_alliances/2020nyny"


def test_enqueue_explicit_year_skips_unofficial(
    tasks_client: Client, taskqueue_stub: testbed.taskqueue_stub.TaskQueueServiceStub
) -> None:
    create_event(official=False)
    resp = tasks_client.get("/tasks/enqueue/fmsapi_event_alliances/2020")
    assert resp.status_code == 200

    tasks = taskqueue_stub.get_filtered_tasks(queue_names="datafeed")
    assert len(tasks) == 0


def test_get_bad_key(tasks_client: Client) -> None:
    resp = tasks_client.get("/tasks/get/fmsapi_event_alliances/asdf")
    assert resp.status_code == 404


def test_get_no_event(tasks_client: Client) -> None:
    resp = tasks_client.get("/tasks/get/fmsapi_event_alliances/2020nyny")
    assert resp.status_code == 404


@mock.patch.object(DatafeedFMSAPI, "get_event_alliances")
def test_get_no_alliances(fmsapi_event_alliances_mock, tasks_client: Client) -> None:
    create_event(official=True)
    fmsapi_event_alliances_mock.return_value = InstantFuture([])

    resp = tasks_client.get("/tasks/get/fmsapi_event_alliances/2020nyny")
    assert resp.status_code == 200
    assert len(resp.data) > 0


@mock.patch.object(DatafeedFMSAPI, "get_event_alliances")
def test_get_no_events_no_output_in_taskqueue(
    fmsapi_event_alliances_mock, tasks_client: Client
) -> None:
    create_event(official=True)
    fmsapi_event_alliances_mock.return_value = InstantFuture([])

    resp = tasks_client.get(
        "/tasks/get/fmsapi_event_alliances/2020nyny",
        headers={"X-Appengine-Taskname": "test"},
    )
    assert resp.status_code == 200
    assert len(resp.data) == 0


@mock.patch.object(DatafeedFMSAPI, "get_event_alliances")
def test_get(
    fmsapi_event_alliances_mock,
    tasks_client: Client,
) -> None:
    create_event(official=True)
    alliances = [EventAlliance(picks=["frc254"])]
    fmsapi_event_alliances_mock.return_value = InstantFuture(alliances)

    resp = tasks_client.get("/tasks/get/fmsapi_event_alliances/2020nyny")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    # Make sure we write objects
    details = EventDetails.get_by_id("2020nyny")
    assert details is not None
    assert details.alliance_selections == alliances


@mock.patch.object(DatafeedFMSAPI, "get_event_alliances")
def test_get_remapteams(
    fmsapi_event_alliances_mock,
    tasks_client: Client,
) -> None:
    create_event(official=True, remap_teams={"frc254": "frc9000"})
    alliances = [EventAlliance(picks=["frc254"])]
    fmsapi_event_alliances_mock.return_value = InstantFuture(alliances)

    resp = tasks_client.get("/tasks/get/fmsapi_event_alliances/2020nyny")
    assert resp.status_code == 200
    assert len(resp.data) > 0

    # Make sure we write objects
    details = EventDetails.get_by_id("2020nyny")
    assert details is not None
    assert details.alliance_selections == [EventAlliance(picks=["frc9000"])]
