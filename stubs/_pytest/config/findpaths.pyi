import py
from . import Config as Config
from .exceptions import UsageError as UsageError
from _pytest.compat import TYPE_CHECKING as TYPE_CHECKING
from _pytest.outcomes import fail as fail
from typing import Any, Iterable, List, Optional, Tuple

def exists(path: Any, ignore: Any = ...): ...
def getcfg(args: Any, config: Optional[Any] = ...): ...
def get_common_ancestor(paths: Iterable[py.path.local]) -> py.path.local: ...
def get_dirs_from_args(args: Any): ...

CFG_PYTEST_SECTION: str

def determine_setup(
    inifile: Optional[str],
    args: List[str],
    rootdir_cmd_arg: Optional[str] = ...,
    config: Optional[Config] = ...,
) -> Tuple[py.path.local, Optional[str], Any]: ...
