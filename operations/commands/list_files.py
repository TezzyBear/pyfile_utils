from os import walk

from ..operation import Operation
from ... import globals

command_name = "ls"


def command_cb():

    print(f"Executing {command_name} at {globals.current_path}:")
    _, dirs, paths = next(walk(globals.current_path))
    for dir in dirs:
        print(f"{dir}/")
    for path in paths:
        print(path)


list_files = Operation(command_name, command_cb)
