from ..operation import Operation
from ... import globals

command_name = "exit"


def command_cb():
    print(f"Exiting pyfile_utils.")
    globals.run_loop = False


exit = Operation(command_name, command_cb)
