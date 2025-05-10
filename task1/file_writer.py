class FileWriter:
    """
      Клас FileWriter забезпечує запис даних у файл.
      """
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, content):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(content)

    def write_line(self, content):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(content + '\n')