import re
from task4.text_reader import TextReader


class SmartTextReaderLocker(TextReader):
    """
    Проксі-клас для обмеження доступу до певних файлів
    """
    def __init__(self, reader, pattern):
        self._reader = reader
        self._restriction_pattern = re.compile(pattern)

    def read_text_file(self, filename):
        if self._restriction_pattern.search(filename):
            print("Access denied!")
            return []
        else:
            return self._reader.read_text_file(filename)