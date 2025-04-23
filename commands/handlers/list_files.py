from pathlib import Path

from ..command import Command
from ... import globals

command_name = "ls"


def command_cb():
    for item in globals.current_path.iterdir():

        if item.is_dir():
            print(f"{item.name}/")
        else:
            print(item.name)


list_files = Command(command_name, command_cb)
