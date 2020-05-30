from .._code.source import getfslineno as getfslineno
from ..compat import NOTSET as NOTSET, ascii_escaped as ascii_escaped
from _pytest.outcomes import fail as fail
from _pytest.warning_types import PytestUnknownMarkWarning as PytestUnknownMarkWarning
from collections.abc import MutableMapping
from typing import Any, Iterable, List, Optional, Union

EMPTY_PARAMETERSET_OPTION: str

def istestfunc(func: Any): ...
def get_empty_parameterset_mark(config: Any, argnames: Any, func: Any): ...

class ParameterSet:
    @classmethod
    def param(cls, *values: Any, marks: Any = ..., id: Optional[Any] = ...): ...
    @classmethod
    def extract_from(cls, parameterset: Any, force_tuple: bool = ...): ...

class Mark:
    name: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def combined_with(self, other: Mark) -> Mark: ...
    def __init__(
        self,
        name: Any,
        args: Any,
        kwargs: Any,
        param_ids_from: Any,
        param_ids_generated: Any,
    ) -> None: ...
    def __ne__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class MarkDecorator:
    mark: Any = ...
    @property
    def name(self): ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    @property
    def markname(self): ...
    def with_args(self, *args: Any, **kwargs: Any): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def __init__(self, mark: Any) -> None: ...
    def __ne__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def get_unpacked_marks(obj: Any): ...
def normalize_mark_list(
    mark_list: Iterable[Union[Mark, MarkDecorator]]
) -> List[Mark]: ...
def store_mark(obj: Any, mark: Any) -> None: ...

class MarkGenerator:
    def __getattr__(self, name: str) -> MarkDecorator: ...

MARK_GEN: Any

class NodeKeywords(MutableMapping):
    node: Any = ...
    parent: Any = ...
    def __init__(self, node: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
