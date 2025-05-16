from visitor import Visitor


class VisibilityTogglerVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Visibility] <div> завжди видимий.")

    def visit_paragraph(self, element):
        print(f"[Visibility] <p> завжди видимий.")

    def visit_span(self, element):
        element.visible = not element.visible
        print(f"[Visibility] Статус видимості <span>: {element.visible}")
