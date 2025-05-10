from abc import ABC, abstractmethod


# Абстрактний базовий клас обробника запитів
class SupportHandler(ABC):
    def __init__(self, name):
        self._next_handler = None
        self.name = name

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, issue_type):
        if self.can_handle(issue_type):
            return self.process(issue_type)
        elif self._next_handler:
            return self._next_handler.handle(issue_type)
        return None

    @abstractmethod
    def can_handle(self, issue_type):
        pass

    @abstractmethod
    def process(self, issue_type):
        pass