from pathlib import Path

from .commands.command_validation_error import CommandValidationError
from .commands import CommandManager
from .commands.handlers import (
    create_file,
    delete_file,
    exit,
    get_current_path,
    list_files,
    travel,
)

from . import globals


def main():
    globals.current_path = Path.cwd()

    operation_manager = CommandManager()
    operation_manager.add(
        create_file,
        delete_file,
        exit,
        get_current_path,
        list_files,
        travel,
    )

    print("PyFile started...")
    while globals.run_loop:
        try:
            input_command = input("pyfu>>>" + str(globals.current_path.resolve()) + ">")
            operation_manager.verify_command(input_command)
            operation_manager.run_command(input_command)
        except CommandValidationError as e:
            print(f"Invalid command: {e}")
