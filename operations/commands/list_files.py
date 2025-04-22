from os import listdir

from ..operation import Operation
from ... import globals

command_name = "ls"


def command_cb():
    print(f"Executing {command_name} at {globals.current_path}")
    print(listdir(globals.current_path))


list_files = Operation(command_name, command_cb)
