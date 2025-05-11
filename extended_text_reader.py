from text_reader import TextReader
from bs4 import BeautifulSoup
import re


class SmartIterableTextReader(TextReader):
    """
    Розширений клас SmartTextReader, який підтримує ітерації через свій вміст
    та має можливість розпізнавати HTML-документи
    """

    def __init__(self):
        from document_iterator import IterableDocument
        self.IterableDocument = IterableDocument

    def read_text_file(self, filename):
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

    def read_html_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено")
            return ""
        except Exception as e:
            print(f"Помилка при читанні файлу '{filename}': {e}")
            return ""

    def is_html_file(self, filename):
        if filename.lower().endswith(('.html', '.htm')):
            return True

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read(1024)
                return bool(re.search(r'<!DOCTYPE\s+html|<html', content, re.IGNORECASE))
        except:
            return False

    def create_iterable_document(self, filename):
        is_html = self.is_html_file(filename)

        if is_html:
            content = self.read_html_file(filename)
        else:
            content = self.read_text_file(filename)

        return self.IterableDocument(content, is_html)