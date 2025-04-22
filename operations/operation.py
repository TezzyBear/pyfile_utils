from dataclasses import dataclass
from typing import Callable


@dataclass
class Operation:
    command_name: str
    callback: Callable[[], None]

    def run(self):
        self.callback()
