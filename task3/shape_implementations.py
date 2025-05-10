from shape import Shape


class Circle(Shape):
    """
    Клас для представлення кола.
    """

    def __init__(self, renderer, radius):
        """
        Ініціалізує коло з вказаним рендерером та радіусом.
        """
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        """
        Відображає коло, використовуючи призначений рендерер.
        """
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        """
        Змінює розмір кола.
        """
        self.radius *= factor
        print(f"Circle radius resized to {self.radius}")


class Square(Shape):
    """
    Клас для представлення квадрата.
    """

    def __init__(self, renderer, side_length):
        """
        Ініціалізує квадрат з вказаним рендерером та довжиною сторони.
        """
        super().__init__(renderer)
        self.side_length = side_length

    def draw(self):
        """
        Відображає квадрат, використовуючи призначений рендерер.
        """
        self.renderer.render_square(self.side_length)

    def resize(self, factor):
        """
        Змінює розмір квадрата.
        """
        self.side_length *= factor
        print(f"Square side length resized to {self.side_length}")


class Triangle(Shape):
    """
    Клас для представлення трикутника.
    """

    def __init__(self, renderer, base, height):
        """
        Ініціалізує трикутник з вказаним рендерером, основою та висотою.
        """
        super().__init__(renderer)
        self.base = base
        self.height = height

    def draw(self):
        """
        Відображає трикутник, використовуючи призначений рендерер.
        """
        self.renderer.render_triangle(self.base, self.height)

    def resize(self, factor):
        """
        Змінює розмір трикутника.
        """
        self.base *= factor
        self.height *= factor
        print(f"Triangle base resized to {self.base} and height to {self.height}")