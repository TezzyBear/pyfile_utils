import re

from .command import Command
from .command_validation_error import (
    TooManyOptions,
    RequiresOptions,
    UnexistingCommand,
    UnexistingOption,
)


class CommandManager:
    commands: dict[str, Command] = {}

    def add(self, *ops: Command):
        for op in ops:
            self.commands[op.command_name] = op

    def get_command_names(self) -> list[str]:
        return [op.command_name for op in self.commands.values()]

    def extract_command(self, raw_command: str) -> str:
        match = re.match(r"^([^:\s]+)", raw_command)
        return match.group(1) if match else None

    def extract_option(self, raw_command: str) -> str:
        match = re.match(r"^[^:\s]+:(\S+)", raw_command)
        return match.group(1) if match else None

    def extract_arguments(self, raw_command: str) -> list[str]:
        match = re.match(r"^[^:\s]+(?::\S+)?\s*(.*)", raw_command)
        return match.group(1).split() if match and match.group(1) else []

    def verify_command(self, raw_command: str):

        command_to_verify = self.extract_command(raw_command)
        option_to_verify = self.extract_option(raw_command)

        if not command_to_verify in self.get_command_names():
            raise UnexistingCommand(command_to_verify)

        if option_to_verify:
            if not self.commands[command_to_verify].supports_option(option_to_verify):
                raise UnexistingOption(command_to_verify, option_to_verify)

    def run_command(self, raw_command: str):

        command = self.extract_command(raw_command)
        option = self.extract_option(raw_command)
        arguments = self.extract_arguments(raw_command)

        runArgs = {}

        if option:
            runArgs["option"] = option
        if len(arguments) > 0:
            runArgs["arguments"] = arguments

        self.commands[command].run(runArgs)
