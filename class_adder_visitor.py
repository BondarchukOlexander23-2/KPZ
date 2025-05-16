from visitor import Visitor


class ClassAdderVisitor(Visitor):
    def visit_div(self, element):
        print(f"[Class] <div> не має класів.")

    def visit_paragraph(self, element):
        element.class_list.append("text-block")
        print(f"[Class] Додано клас до <p>: text-block")

    def visit_span(self, element):
        print(f"[Class] <span> не підтримує класів.")
