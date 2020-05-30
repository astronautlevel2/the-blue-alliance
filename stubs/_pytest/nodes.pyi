import py
from _pytest._code.code import (
    ExceptionChainRepr as ExceptionChainRepr,
    ExceptionInfo as ExceptionInfo,
    ReprExceptionInfo as ReprExceptionInfo,
)
from _pytest._code.source import getfslineno as getfslineno
from _pytest.compat import (
    TYPE_CHECKING as TYPE_CHECKING,
    cached_property as cached_property,
)
from _pytest.config import Config as Config, PytestPluginManager as PytestPluginManager
from _pytest.deprecated import NODE_USE_FROM_PARENT as NODE_USE_FROM_PARENT
from _pytest.fixtures import (
    FixtureDef as FixtureDef,
    FixtureLookupError as FixtureLookupError,
    FixtureLookupErrorRepr as FixtureLookupErrorRepr,
)
from _pytest.main import Session as Session
from _pytest.mark.structures import (
    Mark as Mark,
    MarkDecorator as MarkDecorator,
    NodeKeywords as NodeKeywords,
)
from _pytest.outcomes import Failed as Failed, fail as fail
from _pytest.store import Store as Store
from typing import Any, Optional, Tuple, Union

SEP: str
tracebackcutdir: Any

def ischildnode(baseid: Any, nodeid: Any): ...

class NodeMeta(type):
    def __call__(self, *k: Any, **kw: Any): ...

class Node(metaclass=NodeMeta):
    name: Any = ...
    parent: Any = ...
    config: Any = ...
    session: Any = ...
    fspath: Any = ...
    keywords: Any = ...
    own_markers: Any = ...
    extra_keyword_matches: Any = ...
    def __init__(
        self,
        name: str,
        parent: Optional[Node] = ...,
        config: Optional[Config] = ...,
        session: Optional[Session] = ...,
        fspath: Optional[py.path.local] = ...,
        nodeid: Optional[str] = ...,
    ) -> None: ...
    @classmethod
    def from_parent(cls: Any, parent: Node, **kw: Any) -> Any: ...
    @property
    def ihook(self): ...
    def warn(self, warning: Any) -> None: ...
    @property
    def nodeid(self): ...
    def __hash__(self) -> Any: ...
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def listchain(self): ...
    def add_marker(
        self, marker: Union[str, MarkDecorator], append: bool = ...
    ) -> None: ...
    def iter_markers(self, name: Optional[Any] = ...): ...
    def iter_markers_with_node(self, name: Optional[Any] = ...) -> None: ...
    def get_closest_marker(self, name: Any, default: Optional[Any] = ...): ...
    def listextrakeywords(self): ...
    def listnames(self): ...
    def addfinalizer(self, fin: Any) -> None: ...
    def getparent(self, cls: Any): ...
    def repr_failure(
        self, excinfo: Any, style: Any = ...
    ) -> Union[str, ReprExceptionInfo, ExceptionChainRepr, FixtureLookupErrorRepr]: ...

def get_fslocation_from_item(
    item: Item,
) -> Tuple[Union[str, py.path.local], Optional[int]]: ...

class Collector(Node):
    class CollectError(Exception): ...
    def collect(self) -> None: ...
    def repr_failure(self, excinfo: Any): ...

class FSHookProxy:
    fspath: Any = ...
    pm: Any = ...
    remove_mods: Any = ...
    def __init__(
        self, fspath: py.path.local, pm: PytestPluginManager, remove_mods: Any
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class FSCollector(Collector):
    fspath: Any = ...
    def __init__(
        self,
        fspath: py.path.local,
        parent: Any = ...,
        config: Any = ...,
        session: Any = ...,
        nodeid: Any = ...,
    ) -> None: ...
    @classmethod
    def from_parent(cls, parent: Any, fspath: Any, **kw: Any): ...

class File(FSCollector): ...

class Item(Node):
    nextitem: Any = ...
    user_properties: Any = ...
    def __init__(
        self,
        name: Any,
        parent: Optional[Any] = ...,
        config: Optional[Any] = ...,
        session: Optional[Any] = ...,
        nodeid: Optional[Any] = ...,
    ) -> None: ...
    def runtest(self) -> None: ...
    def add_report_section(self, when: str, key: str, content: str) -> None: ...
    def reportinfo(self) -> Tuple[Union[py.path.local, str], Optional[int], str]: ...
    def location(self) -> Tuple[str, Optional[int], str]: ...
