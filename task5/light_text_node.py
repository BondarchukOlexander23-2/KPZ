from light_node import LightNode
import html


class LightTextNode(LightNode):


    def __init__(self, text):
        self.text = text

    def get_outer_html(self):
        return html.escape(self.text)

    def get_inner_html(self):
        return self.get_outer_html()

    def __str__(self):
        return f"TextNode: '{self.text}'"