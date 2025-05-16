from visitor import Visitor


class TextCounterVisitor(Visitor):
    def __init__(self):
        self.total_chars = 0

    def visit_div(self, element):
        self.total_chars += len(element.content)

    def visit_paragraph(self, element):
        self.total_chars += len(element.text)

    def visit_span(self, element):
        self.total_chars += len(element.text)

    def report(self):
        print(f"[Count] Загальна кількість символів: {self.total_chars}")
