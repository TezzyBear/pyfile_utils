class CommandValidationError(Exception):
    """Base class for all command validation errors."""

    pass


class TooManyOptions(CommandValidationError):
    def __init__(self, message="Too many options provided."):
        super().__init__(message)


class RequiresOptions(CommandValidationError):
    def __init__(self, message="This command requires options."):
        super().__init__(message)


class UnexistingCommand(CommandValidationError):
    def __init__(self, command):
        super().__init__(f"Command '{command}' does not exist.")


class UnexistingOption(CommandValidationError):
    def __init__(self, command, option):
        super().__init__(
            f"Option '{option}' doesn't exist for the command '{command}'."
        )
