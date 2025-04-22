from os.path import dirname

from .operations import OperationManager
from .operations.commands.get_current_path import get_current_path
from .operations.commands.list_files import list_files
from . import globals


def main():
    globals.current_path = dirname(__file__)

    operation_manager = OperationManager()
    operation_manager.add(list_files, get_current_path)

    available_commands = operation_manager.get_command_names()

    print("PyFile started...")
    while True:
        command = input("pyfu >>> " + globals.current_path + ">")
        if command in available_commands:
            operation_manager.run_command(command)
        else:
            print("Command is Unavailable")
