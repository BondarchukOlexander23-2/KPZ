from text_reader import TextReader


class SmartTextChecker(TextReader):
    """
    Проксі-клас для логування операцій з файлами
    """

    def __init__(self, reader):
        self._reader = reader

    def read_text_file(self, filename):
        """
        Логує операції з файлом і делегує читання файлу до основного читача
        """
        print(f"Відкриття файлу '{filename}'...")
        content = self._reader.read_text_file(filename)

        if content:
            total_lines = len(content)
            total_chars = sum(len(line) for line in content)
            print(f"Файл '{filename}' успішно прочитано")
            print(f"Загальна кількість рядків: {total_lines}")
            print(f"Загальна кількість символів: {total_chars}")
            print(f"Закриття файлу '{filename}'")

        return content