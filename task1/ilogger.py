from abc import ABC, abstractmethod


class ILogger(ABC):
    """
    Інтерфейс для логерів.
    """

    @abstractmethod
    def log(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def warn(self, message):
        pass