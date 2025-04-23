from .operation import Operation
from .command_validation_error import (
    TooManyOptions,
    RequiresOptions,
    UnexistingCommand,
    UnexistingOption,
)


class OperationManager:
    operations: dict[str, Operation] = {}

    def add(self, *ops: Operation):
        for op in ops:
            self.operations[op.command_name] = op

    def get_command_names(self) -> list[str]:
        return [op.command_name for op in self.operations.values()]

    def verify_command(self, command_str: str):
        parts = command_str.split(":")
        command_to_verify = parts[0]
        option_to_verify = None

        if len(parts) > 2:
            raise TooManyOptions
        if len(parts) == 2:
            option_to_verify = parts[1]
            if not self.operations[command_to_verify].supports_option(option_to_verify):
                raise UnexistingOption(command_to_verify, option_to_verify)
        else:
            if not command_to_verify in self.get_command_names():
                raise UnexistingCommand(command_to_verify)

    def run_command(self, command_str: str, options: str | None = None):
        self.operations[command_str].run()
