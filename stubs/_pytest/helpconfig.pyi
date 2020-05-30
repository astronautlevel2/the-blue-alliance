from _pytest.config import PrintHelp as PrintHelp
from argparse import Action
from typing import Any, Optional

class HelpAction(Action):
    def __init__(
        self,
        option_strings: Any,
        dest: Optional[Any] = ...,
        default: bool = ...,
        help: Optional[Any] = ...,
    ) -> None: ...
    def __call__(
        self,
        parser: Any,
        namespace: Any,
        values: Any,
        option_string: Optional[Any] = ...,
    ) -> None: ...

def pytest_addoption(parser: Any) -> None: ...
def pytest_cmdline_parse() -> None: ...
def showversion(config: Any) -> None: ...
def pytest_cmdline_main(config: Any): ...
def showhelp(config: Any) -> None: ...

conftest_options: Any

def getpluginversioninfo(config: Any): ...
def pytest_report_header(config: Any): ...
