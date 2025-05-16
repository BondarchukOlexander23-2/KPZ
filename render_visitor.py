from visitor import Visitor


class RenderVisitor(Visitor):
    def visit_div(self, element):
        print(f"<div style='{element.style}'>{element.content}</div>")

    def visit_paragraph(self, element):
        class_attr = " ".join(element.class_list)
        print(f"<p class='{class_attr}'>{element.text}</p>")

    def visit_span(self, element):
        if element.visible:
            print(f"<span>{element.text}</span>")
        else:
            print(f"<!-- span приховано -->")
