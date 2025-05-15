from abc import ABC, abstractmethod
class Iterator(ABC):
    """
    Абстрактний клас для визначення інтерфейсу ітератора
    """
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

