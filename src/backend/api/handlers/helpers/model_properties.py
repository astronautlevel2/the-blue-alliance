from typing import List, NewType

from backend.common.queries.dict_converters.event_converter import EventDict
from backend.common.queries.dict_converters.match_converter import MatchDict
from backend.common.queries.dict_converters.team_converter import TeamDict

# Type aliases
ModelType = NewType("ModelType", str)

simple_event_properties = [
    "key",
    "name",
    "year",
    "event_code",
    "event_type",
    "district",
    "start_date",
    "end_date",
    "city",
    "state_prov",
    "country",
]

simple_team_properties = [
    "key",
    "team_number",
    "nickname",
    "name",
    "city",
    "state_prov",
    "country",
]

simple_match_properties = [
    "key",
    "event_key",
    "comp_level",
    "set_number",
    "match_number",
    "alliances",
    "winning_alliance",
    "time",
    "actual_time",
    "predicted_time",
]

search_team_properties = [
    "key",
    "nickname",
]

search_event_properties = [
    "key",
    "name",
]


def filter_event_properties(events: List[EventDict], model_type: ModelType) -> List:
    if not events:
        return []
    if model_type == "simple":
        return [
            {key: event[key] for key in simple_event_properties} for event in events
        ]
    elif model_type == "keys":
        return [event["key"] for event in events]
    elif model_type == "search":
        return [
            {key: event[key] for key in search_event_properties} for event in events
        ]
    else:
        raise Exception("Unknown model_type: {}".format(model_type))


def filter_team_properties(teams: List[TeamDict], model_type: ModelType) -> List:
    if not teams:
        return []
    if model_type == "simple":
        return [{key: team[key] for key in simple_team_properties} for team in teams]
    elif model_type == "keys":
        return [team["key"] for team in teams]
    elif model_type == "search":
        return [{key: team[key] for key in search_team_properties} for team in teams]
    else:
        raise Exception("Unknown model_type: {}".format(model_type))


def filter_match_properties(matches: List[MatchDict], model_type: ModelType) -> List:
    if not matches:
        return []
    if model_type == "simple":
        return [
            {key: match[key] for key in simple_match_properties} for match in matches
        ]
    elif model_type == "keys":
        return [match["key"] for match in matches]
    else:
        raise Exception("Unknown model_type: {}".format(model_type))
