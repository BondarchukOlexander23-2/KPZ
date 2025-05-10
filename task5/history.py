class History:

    def __init__(self):
        self._history = []
        self._current_index = -1

    def push(self, memento):
        if self._current_index < len(self._history) - 1:
            self._history = self._history[:self._current_index + 1]

        self._history.append(memento)
        self._current_index = len(self._history) - 1

    def undo(self):
        if self._current_index > 0:
            self._current_index -= 1
            return self._history[self._current_index]
        return None

    def redo(self):
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
            return self._history[self._current_index]
        return None

    def can_undo(self):
        return self._current_index > 0

    def can_redo(self):
        return self._current_index < len(self._history) - 1