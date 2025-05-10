from renderer_implementations import VectorRenderer, RasterRenderer
from shape_implementations import Circle, Square, Triangle


def main():
    """
    Основна функція, яка демонструє роботу шаблону проектування Міст.
    """
    print("Графічний редактор з використанням шаблону Міст")
    print("=" * 50)

    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    print("\n1. Створення фігур з різними рендерерами:")

    circle_vector = Circle(vector_renderer, 5)
    square_raster = Square(raster_renderer, 4)
    triangle_vector = Triangle(vector_renderer, 6, 8)

    print("\n2. Відображення фігур з початковими рендерерами:")

    circle_vector.draw()
    square_raster.draw()
    triangle_vector.draw()

    print("\n3. Зміна розміру фігур:")

    circle_vector.resize(2)
    square_raster.resize(1.5)
    triangle_vector.resize(0.5)

    print("\n4. Відображення фігур після зміни розміру:")

    circle_vector.draw()
    square_raster.draw()
    triangle_vector.draw()

    print("\n5. Зміна рендерерів фігур:")

    print("Зміна рендерера для кола з векторного на растровий:")
    circle_vector.set_renderer(raster_renderer)

    print("Зміна рендерера для квадрата з растрового на векторний:")
    square_raster.set_renderer(vector_renderer)

    print("\n6. Відображення фігур з новими рендерерами:")

    circle_vector.draw()
    square_raster.draw()
    triangle_vector.draw()

    print("\n7. Створення та відображення додаткових фігур:")

    circle_raster = Circle(raster_renderer, 3)
    square_vector = Square(vector_renderer, 7)
    triangle_raster = Triangle(raster_renderer, 10, 5)

    circle_raster.draw()
    square_vector.draw()
    triangle_raster.draw()

    print("\nДемонстрація завершена!")


if __name__ == "__main__":
    main()