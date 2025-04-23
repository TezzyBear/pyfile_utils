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

    def verify_command(self, raw_command: str):
        parts = raw_command.split(":")
        command_to_verify = parts[0]
        option_to_verify = None

        if len(parts) > 2:
            raise TooManyOptions
        if len(parts) == 2:
            option_to_verify = parts[1].split(" ")[0]
            if not self.commands[command_to_verify].supports_option(option_to_verify):
                raise UnexistingOption(command_to_verify, option_to_verify)
        else:
            if not command_to_verify in self.get_command_names():
                raise UnexistingCommand(command_to_verify)

    def run_command(self, raw_command: str):
        raw_command_parts = raw_command.split(":")
        runArgs = {}

        if len(raw_command_parts) == 2:

            options = raw_command_parts[1].split(" ")[0]
            params = {}

            for i, param in enumerate(raw_command_parts[1].split(" ")[1:]):
                params[f"param{i}"] = param

            runArgs["options"] = options
            if len(params) > 0:
                runArgs["params"] = params

        self.commands[raw_command_parts[0]].run(**runArgs)
