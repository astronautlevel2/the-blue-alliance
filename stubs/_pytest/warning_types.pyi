from _pytest.compat import TYPE_CHECKING as TYPE_CHECKING
from typing import Any

class PytestWarning(UserWarning):
    __module__: str = ...

class PytestAssertRewriteWarning(PytestWarning):
    __module__: str = ...

class PytestCacheWarning(PytestWarning):
    __module__: str = ...

class PytestConfigWarning(PytestWarning):
    __module__: str = ...

class PytestCollectionWarning(PytestWarning):
    __module__: str = ...

class PytestDeprecationWarning(PytestWarning, DeprecationWarning):
    __module__: str = ...

class PytestExperimentalApiWarning(PytestWarning, FutureWarning):
    __module__: str = ...
    @classmethod
    def simple(cls: Any, apiname: str) -> PytestExperimentalApiWarning: ...

class PytestUnhandledCoroutineWarning(PytestWarning):
    __module__: str = ...

class PytestUnknownMarkWarning(PytestWarning):
    __module__: str = ...

class UnformattedWarning:
    category: Any = ...
    template: Any = ...
    def format(self, **kwargs: Any) -> _W: ...
    def __init__(self, category: Any, template: Any) -> None: ...
    def __ne__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

PYTESTER_COPY_EXAMPLE: Any
