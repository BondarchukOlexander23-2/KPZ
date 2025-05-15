from abc import abstractmethod

from bs4 import BeautifulSoup

from iterator import Iterator

class HtmlIterator(Iterator):
    """
    Базовий клас для ітераторів HTML-документів
    """

    def __init__(self, html_content):
        self._soup = BeautifulSoup(html_content, 'html.parser')
        self._elements = []
        self._position = 0
        self._collect_elements()

    @abstractmethod
    def _collect_elements(self):
        pass

    def has_next(self):
        return self._position < len(self._elements)

    def next(self):
        if not self.has_next():
            raise StopIteration("Немає більше елементів")

        element = self._elements[self._position]
        self._position += 1
        return element
