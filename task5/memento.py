class Memento:

    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content