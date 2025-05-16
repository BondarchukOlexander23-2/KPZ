from visitor import Visitor


class AuditVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Audit] Обробка <div> з вмістом: {element.content}")

    def visit_paragraph(self, element):
        print(f"[Audit] Обробка <p> з текстом: {element.text}")

    def visit_span(self, element):
        print(f"[Audit] Обробка <span> з текстом: {element.text}")
