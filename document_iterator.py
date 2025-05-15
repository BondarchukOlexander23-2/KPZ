from abc import abstractmethod

from iterator import Iterator

class DocumentIterator(Iterator):
    """
    Базовий клас для ітераторів документів
    """
    def __init__(self, content):
        self._content = content
        self._position = None
        self._init_position()

    @abstractmethod
    def _init_position(self):
        pass
