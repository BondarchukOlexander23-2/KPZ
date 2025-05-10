from smart_text_reader import SmartTextReader
from smart_text_checker import SmartTextChecker
from smart_text_reader_locker import SmartTextReaderLocker


def create_test_files():

    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Привіт, світ\n")
        f.write("Це тестовий файл\n")
        f.write("для перевірки SmartTextReader")

    with open("system.log", "w", encoding="utf-8") as f:
        f.write("Це лог-файл з обмеженим доступом\n")
        f.write("ERROR: Помилка підключення\n")
        f.write("INFO: Сервер запущено")


def main():
    create_test_files()

    base_reader = SmartTextReader()

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


if __name__ == "__main__":
    main()