from smart_text_reader import SmartTextReader
from smart_text_checker import SmartTextChecker
from smart_text_reader_locker import SmartTextReaderLocker
from read_file_command import ReadFileCommand
from command_invoker import CommandInvoker


def create_test_files():
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Привіт, світ\nЦе тестовий файл\nдля перевірки SmartTextReader")

    with open("system.log", "w", encoding="utf-8") as f:
        f.write("Це лог-файл з обмеженим доступом\nERROR: Помилка підключення\nINFO: Сервер запущено")


def main():
    create_test_files()

    base_reader = SmartTextReader()
    logger_reader = SmartTextChecker(base_reader)
    restricted_reader = SmartTextReaderLocker(logger_reader, r'\.log$')

    invoker = CommandInvoker()

    print("\nТест 1: Звичайний файл")
    invoker.add_command(ReadFileCommand(restricted_reader, "test.txt"))
    result = invoker.run()[0]
    if result:
        print("Вміст як двомірний масив:")
        for row in result:
            print(row)

    print("\nТест 2: Обмежений файл")
    invoker.add_command(ReadFileCommand(restricted_reader, "system.log"))
    invoker.run()

    print("\nТест 3: Файл, якого не існує")
    invoker.add_command(ReadFileCommand(restricted_reader, "non_existent.txt"))
    invoker.run()


if __name__ == "__main__":
    main()
