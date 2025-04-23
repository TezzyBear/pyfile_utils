from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Operation:
    _command_name: str
    _callback: Callable[[], None]
    # Aditional options to modify functionality of command
    _options: list[str] = field(default_factory=list)
    #
    _argument: str | None = None

    @property
    def command_name(self):
        return self._command_name

    def run(self, options: str | None = None):
        if options:
            self._callback(options)
        else:
            self._callback()

    def add_option(self, option_name: str):
        self._options.append(option_name)

    def get_options(self):
        return self._options

    def supports_option(self, option: str) -> bool:
        return True if option in self._options else False
