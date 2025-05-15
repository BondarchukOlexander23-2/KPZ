from collections import deque

from document_iterator import DocumentIterator

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
