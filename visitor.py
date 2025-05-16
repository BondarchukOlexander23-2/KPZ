from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_div(self, element): pass

    @abstractmethod
    def visit_paragraph(self, element): pass

    @abstractmethod
    def visit_span(self, element): pass
