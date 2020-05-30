import pexpect
from _pytest._code import Source as Source
from _pytest.capture import MultiCapture as MultiCapture, SysCapture as SysCapture
from _pytest.compat import TYPE_CHECKING as TYPE_CHECKING
from _pytest.config import ExitCode as ExitCode
from _pytest.fixtures import FixtureRequest as FixtureRequest
from _pytest.main import Session as Session
from _pytest.monkeypatch import MonkeyPatch as MonkeyPatch
from _pytest.nodes import Collector as Collector, Item as Item
from _pytest.pathlib import Path as Path
from _pytest.python import Module as Module
from _pytest.reports import TestReport as TestReport
from _pytest.tmpdir import TempdirFactory as TempdirFactory
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

IGNORE_PAM: Any

def pytest_addoption(parser: Any) -> None: ...
def pytest_configure(config: Any) -> None: ...

class LsofFdLeakChecker:
    def get_open_files(self): ...
    def matching_platform(self): ...
    def pytest_runtest_protocol(self, item: Any) -> None: ...

class PytestArg:
    request: Any = ...
    def __init__(self, request: FixtureRequest) -> None: ...
    def gethookrecorder(self, hook: Any) -> HookRecorder: ...

def get_public_names(values: Any): ...

class ParsedCall:
    def __init__(self, name: Any, kwargs: Any) -> None: ...
    def __getattr__(self, key: Any) -> None: ...

class HookRecorder:
    calls: Any = ...
    def __init__(self, pluginmanager: Any) -> None: ...
    def finish_recording(self) -> None: ...
    def getcalls(self, names: Union[str, Iterable[str]]) -> List[ParsedCall]: ...
    def assert_contains(self, entries: Any) -> None: ...
    def popcall(self, name: str) -> ParsedCall: ...
    def getcall(self, name: str) -> ParsedCall: ...
    def getreports(
        self, names: Union[str, Iterable[str]] = ...
    ) -> List[TestReport]: ...
    def matchreport(
        self,
        inamepart: str = ...,
        names: Union[str, Iterable[str]] = ...,
        when: Any = ...,
    ) -> Any: ...
    def getfailures(
        self, names: Union[str, Iterable[str]] = ...
    ) -> List[TestReport]: ...
    def getfailedcollections(self) -> List[TestReport]: ...
    def listoutcomes(
        self,
    ) -> Tuple[List[TestReport], List[TestReport], List[TestReport]]: ...
    def countoutcomes(self) -> List[int]: ...
    def assertoutcome(
        self, passed: int = ..., skipped: int = ..., failed: int = ...
    ) -> None: ...
    def clear(self) -> None: ...

def linecomp() -> LineComp: ...
def LineMatcher_fixture(request: FixtureRequest) -> Type[LineMatcher]: ...
def testdir(request: FixtureRequest, tmpdir_factory: Any) -> Testdir: ...

rex_session_duration: Any
rex_outcome: Any

class RunResult:
    ret: Any = ...
    outlines: Any = ...
    errlines: Any = ...
    stdout: Any = ...
    stderr: Any = ...
    duration: Any = ...
    def __init__(
        self,
        ret: Union[int, ExitCode],
        outlines: List[str],
        errlines: List[str],
        duration: float,
    ) -> None: ...
    def parseoutcomes(self) -> Dict[str, int]: ...
    def assert_outcomes(
        self,
        passed: int = ...,
        skipped: int = ...,
        failed: int = ...,
        error: int = ...,
        xpassed: int = ...,
        xfailed: int = ...,
    ) -> None: ...

class CwdSnapshot:
    def __init__(self) -> None: ...
    def restore(self) -> None: ...

class SysModulesSnapshot:
    def __init__(self, preserve: Optional[Callable[[str], bool]] = ...) -> None: ...
    def restore(self) -> None: ...

class SysPathsSnapshot:
    def __init__(self) -> None: ...
    def restore(self) -> None: ...

class Testdir:
    __test__: bool = ...
    CLOSE_STDIN: Any = ...
    class TimeoutExpired(Exception): ...
    request: Any = ...
    tmpdir: Any = ...
    test_tmproot: Any = ...
    plugins: Any = ...
    def __init__(
        self, request: FixtureRequest, tmpdir_factory: TempdirFactory
    ) -> None: ...
    def finalize(self) -> None: ...
    def make_hook_recorder(self, pluginmanager: Any): ...
    def chdir(self) -> None: ...
    def makefile(self, ext: Any, *args: Any, **kwargs: Any): ...
    def makeconftest(self, source: Any): ...
    def makeini(self, source: Any): ...
    def getinicfg(self, source: Any): ...
    def makepyfile(self, *args: Any, **kwargs: Any): ...
    def maketxtfile(self, *args: Any, **kwargs: Any): ...
    def syspathinsert(self, path: Optional[Any] = ...) -> None: ...
    def mkdir(self, name: Any): ...
    def mkpydir(self, name: Any): ...
    def copy_example(self, name: Optional[Any] = ...): ...
    Session: Any = ...
    def getnode(self, config: Any, arg: Any): ...
    def getpathnode(self, path: Any): ...
    def genitems(self, colitems: Any): ...
    def runitem(self, source: Any): ...
    def inline_runsource(self, source: Any, *cmdlineargs: Any): ...
    def inline_genitems(self, *args: Any): ...
    def inline_run(
        self, *args: Any, plugins: Any = ..., no_reraise_ctrlc: bool = ...
    ) -> Any: ...
    def runpytest_inprocess(self, *args: Any, **kwargs: Any) -> RunResult: ...
    def runpytest(self, *args: Any, **kwargs: Any) -> RunResult: ...
    def parseconfig(self, *args: Any): ...
    def parseconfigure(self, *args: Any): ...
    def getitem(self, source: Any, funcname: str = ...): ...
    def getitems(self, source: Any): ...
    config: Any = ...
    def getmodulecol(
        self, source: Any, configargs: Any = ..., withinit: bool = ...
    ): ...
    def collect_by_name(
        self, modcol: Module, name: str
    ) -> Optional[Union[Item, Collector]]: ...
    def popen(
        self,
        cmdargs: Any,
        stdout: Any = ...,
        stderr: Any = ...,
        stdin: Any = ...,
        **kw: Any
    ): ...
    def run(self, *cmdargs: Any, timeout: Any = ..., stdin: Any = ...) -> RunResult: ...
    def runpython(self, script: Any) -> RunResult: ...
    def runpython_c(self, command: Any): ...
    def runpytest_subprocess(self, *args: Any, timeout: Any = ...) -> RunResult: ...
    def spawn_pytest(
        self, string: str, expect_timeout: float = ...
    ) -> pexpect.spawn: ...
    def spawn(self, cmd: str, expect_timeout: float = ...) -> pexpect.spawn: ...

class LineComp:
    stringio: Any = ...
    def __init__(self) -> None: ...
    def assert_contains_lines(self, lines2: Sequence[str]) -> None: ...

class LineMatcher:
    lines: Any = ...
    def __init__(self, lines: List[str]) -> None: ...
    def fnmatch_lines_random(self, lines2: Sequence[str]) -> None: ...
    def re_match_lines_random(self, lines2: Sequence[str]) -> None: ...
    def get_lines_after(self, fnline: str) -> Sequence[str]: ...
    def fnmatch_lines(
        self, lines2: Sequence[str], *, consecutive: bool = ...
    ) -> None: ...
    def re_match_lines(
        self, lines2: Sequence[str], *, consecutive: bool = ...
    ) -> None: ...
    def no_fnmatch_line(self, pat: str) -> None: ...
    def no_re_match_line(self, pat: str) -> None: ...
    def str(self) -> str: ...
