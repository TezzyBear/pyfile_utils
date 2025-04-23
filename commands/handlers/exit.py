from ..command import Command
from ... import globals

command_name = "exit"


def command_cb():
    print(f"Exiting pyfile_utils.")
    globals.run_loop = False


exit = Command(command_name, command_cb)
