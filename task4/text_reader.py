from abc import ABC, abstractmethod

class TextReader(ABC):
    """
    Абстрактний клас для визначення інтерфейсу читача текстових файлів
    """

    @abstractmethod
    def read_text_file(self, filename):
        pass