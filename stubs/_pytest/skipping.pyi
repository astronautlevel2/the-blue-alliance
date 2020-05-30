from _pytest.config import hookimpl as hookimpl
from _pytest.mark.evaluate import MarkEvaluator as MarkEvaluator
from _pytest.outcomes import fail as fail, skip as skip, xfail as xfail
from _pytest.store import StoreKey as StoreKey
from typing import Any

skipped_by_mark_key: Any
evalxfail_key: Any
unexpectedsuccess_key: Any

def pytest_addoption(parser: Any) -> None: ...
def pytest_configure(config: Any): ...
def pytest_runtest_setup(item: Any) -> None: ...
def pytest_pyfunc_call(pyfuncitem: Any) -> None: ...
def check_xfail_no_run(item: Any) -> None: ...
def check_strict_xfail(pyfuncitem: Any) -> None: ...
def pytest_runtest_makereport(item: Any, call: Any) -> None: ...
def pytest_report_teststatus(report: Any): ...
