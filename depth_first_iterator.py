from document_iterator import DocumentIterator

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
