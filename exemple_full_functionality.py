from document_iterator import IterableDocument
from extended_text_reader import SmartIterableTextReader
from smart_text_checker import SmartTextChecker
from smart_text_reader_locker import SmartTextReaderLocker
import re


def create_test_files():
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Привіт, світ\n")
        f.write("Це тестовий файл\n")
        f.write("для перевірки SmartTextReader")

    with open("system.log", "w", encoding="utf-8") as f:
        f.write("Це лог-файл з обмеженим доступом\n")
        f.write("ERROR: Помилка підключення\n")
        f.write("INFO: Сервер запущено")

    with open("test.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Тестова HTML-сторінка</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Заголовок сторінки</h1>
    <div class="content">
        <p>Перший параграф</p>
        <p>Другий параграф</p>
        <ul>
            <li>Пункт 1</li>
            <li>Пункт 2</li>
            <li>Пункт 3</li>
        </ul>
    </div>
    <footer>
        Підвал сторінки
    </footer>
</body>
</html>""")


def test_text_iterator():
    print("\n=== Тестування ітераторів для текстових файлів ===")

    reader = SmartIterableTextReader()
    content = reader.read_text_file("test.txt")

    document = IterableDocument(content)

    print("\nОбхід в глибину:")
    depth_iterator = document.create_depth_iterator()

    while depth_iterator.has_next():
        char, row, col = depth_iterator.next()
        print(f"Символ '{char}' на позиції [{row}, {col}]")
        if row == 0 and col == 9:
            print("...")
            break

    print("\nОбхід в ширину:")
    breadth_iterator = document.create_breadth_iterator()

    while breadth_iterator.has_next():
        char, row, col = breadth_iterator.next()
        print(f"Символ '{char}' на позиції [{row}, {col}]")
        if row == 0 and col == 9:
            print("...")
            break


def test_html_iterator():
    print("\n=== Тестування ітераторів для HTML-файлів ===")

    reader = SmartIterableTextReader()

    if reader.is_html_file("test.html"):
        print("\nФайл test.html є HTML-документом")

        document = reader.create_iterable_document("test.html")

        print("\nОбхід HTML в глибину (перші 5 елементів):")
        depth_iterator = document.create_depth_iterator()

        count = 0
        while depth_iterator.has_next() and count < 5:
            element = depth_iterator.next()
            if hasattr(element, 'name') and element.name:
                print(f"Елемент: <{element.name}>")
            elif element.strip():
                print(f"Текст: {element.strip()[:30]}...")
            count += 1
        print("...")

        print("\nОбхід HTML в ширину (перші 5 елементів):")
        breadth_iterator = document.create_breadth_iterator()

        count = 0
        while breadth_iterator.has_next() and count < 5:
            element = breadth_iterator.next()
            if hasattr(element, 'name') and element.name:
                print(f"Елемент: <{element.name}>")
            elif element.strip():
                print(f"Текст: {element.strip()[:30]}...")
            count += 1
        print("...")
    else:
        print("Файл test.html не є HTML-документом")


def main():
    create_test_files()

    base_reader = SmartIterableTextReader()
    logger_reader = SmartTextChecker(base_reader)
    restricted_reader = SmartTextReaderLocker(logger_reader, r'\.log$')

    print("\nТест 1: Звичайний файл")
    content = restricted_reader.read_text_file("test.txt")
    if content:
        print("Вміст як двомірний масив:")
        for row in content:
            print(row)

    print("\nТест 2: Обмежений файл")
    restricted_reader.read_text_file("system.log")

    print("\nТест 3: Файл, якого не існує")
    restricted_reader.read_text_file("non_existent.txt")

    test_text_iterator()
    test_html_iterator()

    print("\n=== Демонстрація інтеграції ітераторів з існуючою системою ===")
    document = base_reader.create_iterable_document("test.txt")

    print("\nПідрахунок кількості символів за допомогою ітератора:")
    depth_iterator = document.create_depth_iterator()

    char_count = 0
    while depth_iterator.has_next():
        depth_iterator.next()
        char_count += 1

    print(f"Загальна кількість символів: {char_count}")


if __name__ == "__main__":
    main()