from command_interface import Command

class ReadFileCommand(Command):
    def __init__(self, reader, filename):
        self.reader = reader
        self.filename = filename

    def execute(self):
        return self.reader.read_text_file(self.filename)
