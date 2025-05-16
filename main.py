from html_elements import Div, Paragraph, Span, Visitor

class StyleVisitor(Visitor):
    def visit_div(self, element):
        element.style = "border: 1px solid black;"
        print(f"[Style] Застосовано стиль до <div>: {element.style}")

    def visit_paragraph(self, element):
        print(f"[Style] Абзац не потребує стилю.")

    def visit_span(self, element):
        element.style = "color: blue;"
        print(f"[Style] Застосовано стиль до <span>: {element.style}")

class ClassAdderVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Class] <div> не має класів.")

    def visit_paragraph(self, element):
        element.class_list.append("text-block")
        print(f"[Class] Додано клас до <p>: text-block")

    def visit_span(self, element):
        print(f"[Class] <span> не підтримує класів.")

class VisibilityTogglerVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Visibility] <div> завжди видимий.")

    def visit_paragraph(self, element):
        print(f"[Visibility] <p> завжди видимий.")

    def visit_span(self, element):
        element.visible = not element.visible
        print(f"[Visibility] Статус видимості <span>: {element.visible}")

class RenderVisitor(Visitor):
    def visit_div(self, element):
        print(f"<div style='{element.style}'>{element.content}</div>")

    def visit_paragraph(self, element):
        class_attr = " ".join(element.class_list)
        print(f"<p class='{class_attr}'>{element.text}</p>")

    def visit_span(self, element):
        if element.visible:
            print(f"<span style='{element.style}'>{element.text}</span>")
        else:
            print(f"<!-- span приховано -->")

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

class AuditVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Audit] Обробка <div> з вмістом: {element.content}")

    def visit_paragraph(self, element):
        print(f"[Audit] Обробка <p> з текстом: {element.text}")

    def visit_span(self, element):
        print(f"[Audit] Обробка <span> з текстом: {element.text}")

if __name__ == "__main__":
    elements = [
        Div("Контейнер для вмісту"),
        Paragraph("Це приклад абзацу."),
        Span("важливе слово")
    ]

    visitors = [
        StyleVisitor(),
        ClassAdderVisitor(),
        VisibilityTogglerVisitor(),
        RenderVisitor(),
        TextCounterVisitor(),
        AuditVisitor()
    ]

    for visitor in visitors:
        print(f"\n--- {visitor.__class__.__name__} ---")
        for el in elements:
            el.accept(visitor)
        if isinstance(visitor, TextCounterVisitor):
            visitor.report()
