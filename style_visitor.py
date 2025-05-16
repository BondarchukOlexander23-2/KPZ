from visitor import Visitor


class StyleVisitor(Visitor):
    def visit_div(self, element):
        element.style = "border: 1px solid black;"
        print(f"[Style] Застосовано стиль до <div>: {element.style}")

    def visit_paragraph(self, element):
        print(f"[Style] Абзац не потребує стилю.")

    def visit_span(self, element):
        element.style = "color: blue;"
        print(f"[Style] Застосовано стиль до <span>: {element.style}")
