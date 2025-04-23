# TODO: Travel up, down, in (see file content) files
from typing import Literal

from ..command import Command
from ... import globals

command_name = "t"
sub_command_names = ["up", "down", "in"]


# t:down operations
def command_cb(dir: Literal["up", "down", "in"], params: dict | None = None):
    match dir:
        case "up":
            globals.current_path = globals.current_path.parent
        case "down":
            path_names = [path.name for path in globals.current_path.iterdir()]

            try:
                if params.get("param0") in path_names:
                    globals.current_path = globals.current_path / params.get("param0")
                else:
                    raise Exception(f"Folder {params.get("param0")} doesn't exist")
            except Exception as e:
                print(e)

        case "in":
            pass


travel = Command(command_name, command_cb)
travel.add_option("up")
travel.add_option("down")
travel.add_option("in")
