from _pytest import outcomes as outcomes
from _pytest._io.saferepr import safeformat as safeformat, saferepr as saferepr
from _pytest.compat import ATTRS_EQ_FIELD as ATTRS_EQ_FIELD
from typing import Any, List, Optional

def format_explanation(explanation: str) -> str: ...
def issequence(x: Any) -> bool: ...
def istext(x: Any) -> bool: ...
def isdict(x: Any) -> bool: ...
def isset(x: Any) -> bool: ...
def isdatacls(obj: Any) -> bool: ...
def isattrs(obj: Any) -> bool: ...
def isiterable(obj: Any) -> bool: ...
def assertrepr_compare(
    config: Any, op: str, left: Any, right: Any
) -> Optional[List[str]]: ...
