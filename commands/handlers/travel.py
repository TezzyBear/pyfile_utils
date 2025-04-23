# TODO: Travel up, down, in (see file content) files
from typing import Literal

from ..command import Command
from ... import globals

command_name = "t"
sub_command_names = ["up", "down", "in", "out"]


# t:down operations
def command_cb(option: Literal["up", "down", "in"], arguments: list[str] | None = None):
    match option:
        case "up":
            globals.current_path = globals.current_path.parent
        case "down":
            path_names = [path.name for path in globals.current_path.iterdir()]

            try:
                folder_name = arguments[0]
                if folder_name in path_names:
                    globals.current_path = globals.current_path / folder_name
                else:
                    raise Exception(f"Folder {folder_name} doesn't exist.")
            except Exception as e:
                print(e)

        case "in":
            pass

        case "out":
            pass


travel = Command(command_name, command_cb)
travel.add_option("up")
travel.add_option("down")
travel.add_option("in")
