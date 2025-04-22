from ..operation import Operation
from ...globals import current_path

command_name = "gcp"


def command_cb():
    print(f"Executing {command_name} at {current_path}")
    # TODO: print current path


get_current_path = Operation(command_name, command_cb)
