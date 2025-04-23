# TODO: Delete file
from pathlib import Path

from ..command import Command
from ... import globals

command_name = "df"


def command_cb(option: None = None, arguments: list[str] | None = None):
    try:
        file = arguments[0]
        if (globals.current_path / file).exists:
            (globals.current_path / file).unlink()
        else:
            raise Exception(f"{file} doesn't exist in {globals.current_path}.")
    except Exception as e:
        print(f"{e}")


delete_file = Command(command_name, command_cb)
