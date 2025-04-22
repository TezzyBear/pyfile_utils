from .operation import Operation


class OperationManager:
    operations: dict[str, Operation] = {}

    def add(self, *ops: Operation):
        for op in ops:
            self.operations[op.command_name] = op

    def get_command_names(self) -> list[str]:
        return [op.command_name for op in self.operations.values()]

    def run_command(self, command_str: str):
        self.operations[command_str].run()
