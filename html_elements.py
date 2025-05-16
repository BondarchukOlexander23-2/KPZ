from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Інтерфейс для відвідувачів
class Visitor(ABC):
    @abstractmethod
    def visit_div(self, element): pass

    @abstractmethod
    def visit_paragraph(self, element): pass

    @abstractmethod
    def visit_span(self, element): pass

# Елементи
class Div(Element):
    def __init__(self, content):
        self.tag = "div"
        self.content = content
        self.style = ""

    def accept(self, visitor):
        visitor.visit_div(self)

class Paragraph(Element):
    def __init__(self, text):
        self.tag = "p"
        self.text = text
        self.class_list = []

    def accept(self, visitor):
        visitor.visit_paragraph(self)

class Span(Element):
    def __init__(self, text):
        self.tag = "span"
        self.text = text
        self.visible = True
        self.style = ""

    def accept(self, visitor):
        visitor.visit_span(self)
