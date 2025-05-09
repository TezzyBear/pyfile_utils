from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Command:
    _name: str
    _callback: Callable[[], None]
    # Aditional options to modify functionality of command
    _options: list[str] = field(default_factory=list)
    #
    _argument: str | None = None

    @property
    def command_name(self):
        return self._name

    def run(self, runArgs: dict = field(default_factory=dict)):
        self._callback(**runArgs)

    def add_option(self, option_name: str):
        self._options.append(option_name)

    def get_options(self):
        return self._options

    def supports_option(self, option: str) -> bool:
        return True if option in self._options else False
