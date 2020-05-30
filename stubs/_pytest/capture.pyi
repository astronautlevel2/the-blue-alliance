from _pytest.compat import (
    CaptureAndPassthroughIO as CaptureAndPassthroughIO,
    CaptureIO as CaptureIO,
    TYPE_CHECKING as TYPE_CHECKING,
)
from _pytest.config import Config as Config
from _pytest.fixtures import FixtureRequest as FixtureRequest
from collections import namedtuple
from typing import Any, BinaryIO, Iterable, Optional

patchsysdict: Any

def pytest_addoption(parser: Any) -> None: ...
def pytest_load_initial_conftests(early_config: Config) -> Any: ...

class CaptureManager:
    def __init__(self, method: _CaptureMethod) -> None: ...
    def is_capturing(self): ...
    def is_globally_capturing(self): ...
    def start_global_capturing(self) -> None: ...
    def stop_global_capturing(self) -> None: ...
    def resume_global_capture(self) -> None: ...
    def suspend_global_capture(self, in_: bool = ...) -> None: ...
    def suspend(self, in_: bool = ...) -> None: ...
    def resume(self) -> None: ...
    def read_global_capture(self): ...
    def activate_fixture(self) -> None: ...
    def deactivate_fixture(self) -> None: ...
    def suspend_fixture(self) -> None: ...
    def resume_fixture(self) -> None: ...
    def global_and_fixture_disabled(self) -> None: ...
    def item_capture(self, when: Any, item: Any) -> None: ...
    def pytest_make_collect_report(self, collector: Any) -> None: ...
    def pytest_runtest_setup(self, item: Any) -> None: ...
    def pytest_runtest_call(self, item: Any) -> None: ...
    def pytest_runtest_teardown(self, item: Any) -> None: ...
    def pytest_keyboard_interrupt(self, excinfo: Any) -> None: ...
    def pytest_internalerror(self, excinfo: Any) -> None: ...

def capsys(request: Any) -> None: ...
def capsysbinary(request: Any) -> None: ...
def capfd(request: Any) -> None: ...
def capfdbinary(request: Any) -> None: ...

class CaptureFixture:
    captureclass: Any = ...
    request: Any = ...
    def __init__(self, captureclass: Any, request: Any) -> None: ...
    def close(self) -> None: ...
    def readouterr(self): ...
    def disabled(self) -> None: ...

def safe_text_dupfile(f: Any, mode: Any, default_encoding: str = ...): ...

class EncodedFile:
    errors: str = ...
    buffer: Any = ...
    encoding: Any = ...
    def __init__(self, buffer: BinaryIO, encoding: str) -> None: ...
    def write(self, s: str) -> int: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def mode(self) -> str: ...
    def __getattr__(self, name: Any): ...

CaptureResult = namedtuple("CaptureResult", ["out", "err"])

class MultiCapture:
    out: Any = ...
    err: Any = ...
    in_: Any = ...
    def __init__(
        self,
        out: bool = ...,
        err: bool = ...,
        in_: bool = ...,
        Capture: Optional[Any] = ...,
    ) -> None: ...
    def start_capturing(self) -> None: ...
    def pop_outerr_to_orig(self): ...
    def suspend_capturing(self, in_: bool = ...) -> None: ...
    def resume_capturing(self) -> None: ...
    def stop_capturing(self) -> None: ...
    def readouterr(self) -> CaptureResult: ...

class NoCapture:
    EMPTY_BUFFER: Any = ...
    __init__: Any = ...
    start: Any = ...
    done: Any = ...
    suspend: Any = ...
    resume: Any = ...

class FDCaptureBinary:
    EMPTY_BUFFER: bytes = ...
    targetfd: Any = ...
    targetfd_save: Any = ...
    start: Any = ...
    done: Any = ...
    syscapture: Any = ...
    tmpfile: Any = ...
    tmpfile_fd: Any = ...
    def __init__(self, targetfd: Any, tmpfile: Optional[Any] = ...) -> None: ...
    def snap(self): ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def writeorg(self, data: Any) -> None: ...

class FDCapture(FDCaptureBinary):
    EMPTY_BUFFER: Any = ...
    def snap(self): ...
    def writeorg(self, data: Any) -> None: ...

class SysCaptureBinary:
    EMPTY_BUFFER: bytes = ...
    name: Any = ...
    tmpfile: Any = ...
    def __init__(self, fd: Any, tmpfile: Optional[Any] = ...) -> None: ...
    def start(self) -> None: ...
    def snap(self): ...
    def done(self) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def writeorg(self, data: Any) -> None: ...

class SysCapture(SysCaptureBinary):
    EMPTY_BUFFER: Any = ...
    def snap(self): ...
    def writeorg(self, data: Any) -> None: ...

class TeeSysCapture(SysCapture):
    name: Any = ...
    tmpfile: Any = ...
    def __init__(self, fd: Any, tmpfile: Optional[Any] = ...) -> None: ...

map_fixname_class: Any

class DontReadFromInput:
    encoding: Any = ...
    def read(self, *args: Any) -> None: ...
    readline: Any = ...
    readlines: Any = ...
    __next__: Any = ...
    def __iter__(self) -> Any: ...
    def fileno(self) -> None: ...
    def isatty(self): ...
    def close(self) -> None: ...
    @property
    def buffer(self): ...
