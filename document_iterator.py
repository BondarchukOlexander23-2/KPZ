from abc import ABC, abstractmethod
from collections import deque
from bs4 import BeautifulSoup


class Iterator(ABC):
    """
    Абстрактний клас для визначення інтерфейсу ітератора
    """
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class DocumentIterator(Iterator):
    """
    Базовий клас для ітераторів документів
    """
    def __init__(self, content):
        self._content = content
        self._position = None
        self._init_position()

    @abstractmethod
    def _init_position(self):
        pass


class DepthFirstIterator(DocumentIterator):
    """
    Ітератор для обходу вмісту документа в глибину
    """
    def _init_position(self):
        self._position = (0, 0) if self._content and self._content[0] else None
        self._visited = set()

    def has_next(self):
        return self._position is not None

    def next(self):
        if not self.has_next():
            raise StopIteration("Немає більше елементів")

        row, col = self._position
        current_char = self._content[row][col]
        current_position = (row, col)

        # Зберігаємо поточну позицію
        self._visited.add(current_position)

        # Шукаємо наступну позицію
        # Спочатку намагаємося рухатись вниз
        if row + 1 < len(self._content) and (row + 1, col) not in self._visited:
            self._position = (row + 1, col)
        # Інакше рухаємось праворуч
        elif col + 1 < len(self._content[row]) and (row, col + 1) not in self._visited:
            self._position = (row, col + 1)
        # Інакше перевіряємо інші можливі напрямки (вліво та вгору)
        else:
            # Пошук непройденої позиції
            found = False
            for r in range(len(self._content)):
                for c in range(len(self._content[r])):
                    if (r, c) not in self._visited:
                        self._position = (r, c)
                        found = True
                        break
                if found:
                    break
            if not found:
                self._position = None

        return (current_char, row, col)


class BreadthFirstIterator(DocumentIterator):
    """
    Ітератор для обходу вмісту документа в ширину
    """

    def _init_position(self):
        if not self._content or not self._content[0]:
            self._queue = deque()
        else:
            self._queue = deque([(0, 0)])
        self._visited = set()

    def has_next(self):
        return len(self._queue) > 0

    def next(self):
        if not self.has_next():
            raise StopIteration("Немає більше елементів")

        row, col = self._queue.popleft()
        current_char = self._content[row][col]
        current_position = (row, col)

        # Зберігаємо поточну позицію
        self._visited.add(current_position)

        # Вниз
        if row + 1 < len(self._content) and (row + 1, col) not in self._visited and (row + 1, col) not in self._queue:
            self._queue.append((row + 1, col))
        # Праворуч
        if col + 1 < len(self._content[row]) and (row, col + 1) not in self._visited and (
        row, col + 1) not in self._queue:
            self._queue.append((row, col + 1))
        # Вгору
        if row - 1 >= 0 and (row - 1, col) not in self._visited and (row - 1, col) not in self._queue:
            self._queue.append((row - 1, col))
        # Вліво
        if col - 1 >= 0 and (row, col - 1) not in self._visited and (row, col - 1) not in self._queue:
            self._queue.append((row, col - 1))

        return (current_char, row, col)


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


class HtmlDepthFirstIterator(HtmlIterator):
    def _collect_elements(self):
        def collect_dfs(element):
            self._elements.append(element)
            if hasattr(element, 'contents'):
                for child in element.contents:
                    collect_dfs(child)

        collect_dfs(self._soup)


class HtmlBreadthFirstIterator(HtmlIterator):
    """
    Ітератор для обходу HTML-документа в ширину
    """
    def _collect_elements(self):
        queue = deque([self._soup])

        while queue:
            element = queue.popleft()
            self._elements.append(element)

            if hasattr(element, 'contents'):
                for child in element.contents:
                    queue.append(child)


class IterableDocument:
    def __init__(self, content, is_html=False):
        self._content = content
        self._is_html = is_html

    def create_depth_iterator(self):
        if self._is_html:
            return HtmlDepthFirstIterator(self._content)
        else:
            return DepthFirstIterator(self._content)

    def create_breadth_iterator(self):
        if self._is_html:
            return HtmlBreadthFirstIterator(self._content)
        else:
            return BreadthFirstIterator(self._content)