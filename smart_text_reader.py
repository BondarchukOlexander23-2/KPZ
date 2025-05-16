from text_reader import TextReader


class SmartTextReader(TextReader):
    """
    Основний клас SmartTextReader, який читає текстовий файл
    і перетворює його вміст на двомірний масив
    """

    def read_text_file(self, filename):
        """
        Читає вміст текстового файлу і повертає двомірний масив,
        де зовнішній масив - рядки тексту, а вкладені масиви - символи в рядках
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = []
                for line in file:
                    line = line.rstrip('\n')
                    content.append(list(line))
                return content
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено")
            return []
        except Exception as e:
            print(f"Помилка при читанні файлу '{filename}': {e}")
            return []