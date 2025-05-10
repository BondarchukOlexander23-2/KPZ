class TextDocument:

    def __init__(self, content=""):
        self._content = content

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content

    def add_content(self, new_content):
        self._content += new_content

    def delete_content(self, start, end):
        if 0 <= start < end <= len(self._content):
            self._content = self._content[:start] + self._content[end:]

    def insert_content(self, position, text):
        if 0 <= position <= len(self._content):
            self._content = self._content[:position] + text + self._content[position:]