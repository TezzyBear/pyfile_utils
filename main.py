from os.path import dirname

from .operations.command_validation_error import CommandValidationError
from .operations import OperationManager
from .operations.commands.exit import exit
from .operations.commands.get_current_path import get_current_path
from .operations.commands.list_files import list_files
from .operations.commands.travel import travel
from . import globals


def main():
    globals.current_path = dirname(__file__)

    operation_manager = OperationManager()
    operation_manager.add(exit, get_current_path, list_files, travel)

    available_commands = operation_manager.get_command_names()

    print("PyFile started...")
    while globals.run_loop:
        try:
            command = input("pyfu>>>" + globals.current_path + ">")
            operation_manager.verify_command(command)
            operation_manager.run_command(command)
        except CommandValidationError as e:
            print(f"Invalid command: {e}")
