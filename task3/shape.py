from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактний базовий клас для всіх фігур - абстракція в шаблоні Міст.
    """

    def __init__(self, renderer):
        """
        Ініціалізує фігуру з вказаним рендерером.
        """
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        """
        Відображає фігуру, використовуючи призначений рендерер.
        """
        pass

    @abstractmethod
    def resize(self, factor):
        """
        Змінює розмір фігури.
        """
        pass

    def set_renderer(self, renderer):
        """
        Змінює рендерер для фігури.
        """
        self.renderer = renderer