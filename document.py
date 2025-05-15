class SmartDocument:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        element.trigger('on_created')
        self.elements.append(element)
        element.trigger('on_inserted')

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            element.trigger('on_removed')

    def render(self):
        print("<document>")
        for el in self.elements:
            el.render(level=1)
        print("</document>")
