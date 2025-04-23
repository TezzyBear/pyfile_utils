# TODO: Create file, add flag or option to add inline -m text or something along thoose lines, within the file
from ..command import Command
from ... import globals

command_name = "cf"


def command_cb(option: None = None, arguments: list[str] | None = None):
    file = arguments[0]
    print(f"Created {file} at: {globals.current_path}")
    (globals.current_path / file).touch()


create_file = Command(command_name, command_cb)
