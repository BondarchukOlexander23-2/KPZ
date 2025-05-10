import os
from logger import Logger
from file_writer import FileWriter
from file_logger_adapter import FileLoggerAdapter


def main():
    # Демонстрація консольного логера
    print("Консольний логер")
    console_logger = Logger()
    console_logger.log("Це інформаційне повідомлення")
    console_logger.warn("Це попередження")
    console_logger.error("Це повідомлення про помилку")

    print("\nФайловий логер")
    # Створюємо шлях до файлу логів
    log_path = "application.log"

    if os.path.exists(log_path):
        os.remove(log_path)

    file_writer = FileWriter(log_path)
    file_logger = FileLoggerAdapter(file_writer)

    file_logger.log("Запис до файлу: інформаційне повідомлення")
    file_logger.warn("Запис до файлу: попередження")
    file_logger.error("Запис до файлу: повідомлення про помилку")

    abs_path = os.path.abspath(log_path)
    print(f"Повідомлення записані у файл: {abs_path}")

    # Виводимо вміст файлу логів
    print("\nВміст файлу логів")
    with open(log_path, 'r', encoding='utf-8') as file:
        print(file.read())

    print("\nПрограма завершена.")


if __name__ == "__main__":
    main()