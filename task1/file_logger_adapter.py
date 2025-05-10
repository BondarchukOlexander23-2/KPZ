from datetime import datetime
from ilogger import ILogger
from file_writer import FileWriter


class FileLoggerAdapter(ILogger):
    """
    Адаптер, що дозволяє використовувати FileWriter як ILogger.
    """

    def __init__(self, file_writer):
        self.file_writer = file_writer

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file_writer.write_line(f"{timestamp} [LOG]: {message}")

    def error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file_writer.write_line(f"{timestamp} [ERROR]: {message}")

    def warn(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file_writer.write_line(f"{timestamp} [WARNING]: {message}")