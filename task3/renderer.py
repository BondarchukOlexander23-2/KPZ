from abc import ABC, abstractmethod


class Renderer(ABC):
    """
    Інтерфейс рендерера - клас реалізації в шаблоні Міст.
    Визначає методи для рендерингу різних типів фігур.
    """

    @abstractmethod
    def render_circle(self, radius):
        """
        Відображає коло.
        """
        pass

    @abstractmethod
    def render_square(self, side_length):
        """
        Відображає квадрат.
        """
        pass

    @abstractmethod
    def render_triangle(self, base, height):
        """
        Відображає трикутник
        """
        pass