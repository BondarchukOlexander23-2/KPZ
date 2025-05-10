from renderer import Renderer


class VectorRenderer(Renderer):
    """
    Рендерер для відображення фігур у векторному форматі.
    """

    def render_circle(self, radius):
        print(f"Малюю коло з радіусом {radius} у векторній графіці (SVG).")

    def render_square(self, side_length):
        print(f"Малюю квадрат зі стороною {side_length} у векторній графіці (SVG).")

    def render_triangle(self, base, height):
        print(f"Малюю трикутник з основою {base} і висотою {height} у векторній графіці (SVG).")


class RasterRenderer(Renderer):

    def render_circle(self, radius):
        print(f"Малюю коло з радіусом {radius} у растровій графіці (PNG/JPEG).")

    def render_square(self, side_length):
        print(f"Малюю квадрат зі стороною {side_length} у растровій графіці (PNG/JPEG).")

    def render_triangle(self, base, height):
        print(f"Малюю трикутник з основою {base} і висотою {height} у растровій графіці (PNG/JPEG).")
