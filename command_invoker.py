class CommandInvoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def run(self):
        results = []
        for command in self._commands:
            result = command.execute()
            results.append(result)
        return results
