from text_document import TextDocument
from memento import Memento
from history import History


class TextEditor:

    def __init__(self):
        self._document = TextDocument()
        self._history = History()
        self._save_state()

    def _save_state(self):
        memento = Memento(self._document.get_content())
        self._history.push(memento)

    def get_content(self):
        return self._document.get_content()

    def set_content(self, content):
        self._document.set_content(content)
        self._save_state()

    def add_content(self, new_content):
        self._document.add_content(new_content)
        self._save_state()

    def delete_content(self, start, end):
        self._document.delete_content(start, end)
        self._save_state()

    def insert_content(self, position, text):
        self._document.insert_content(position, text)
        self._save_state()

    def undo(self):
        memento = self._history.undo()
        if memento:
            self._document.set_content(memento.get_saved_content())
            return True
        return False

    def redo(self):
        memento = self._history.redo()
        if memento:
            self._document.set_content(memento.get_saved_content())
            return True
        return False

    def can_undo(self):
        return self._history.can_undo()

    def can_redo(self):
        return self._history.can_redo()