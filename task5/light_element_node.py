from light_node import LightNode
from enum import Enum, auto


class DisplayType(Enum):
    BLOCK = auto()
    INLINE = auto()


class ClosingType(Enum):
    SELF_CLOSING = auto()
    WITH_CLOSING = auto()


class LightElementNode(LightNode):
    def __init__(self, tag_name, display_type=DisplayType.BLOCK,
                 closing_type=ClosingType.WITH_CLOSING):
        self.tag_name = tag_name
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = []
        self.children = []
        self.attributes = {}

    def add_class(self, css_class):
        if css_class not in self.css_classes:
            self.css_classes.append(css_class)
        return self

    def add_attribute(self, name, value):
        self.attributes[name] = value
        return self

    def add_child(self, child):
        if isinstance(child, LightNode):
            self.children.append(child)
        return self

    def add_text(self, text):
        from light_text_node import LightTextNode
        self.add_child(LightTextNode(text))
        return self

    def get_child_count(self):
        return len(self.children)

    def _generate_opening_tag(self):
        result = f"<{self.tag_name}"

        if self.css_classes:
            class_str = " ".join(self.css_classes)
            result += f' class="{class_str}"'

        for attr_name, attr_value in self.attributes.items():
            result += f' {attr_name}="{attr_value}"'

        if self.closing_type == ClosingType.SELF_CLOSING:
            result += " />"
        else:
            result += ">"

        return result

    def get_inner_html(self):
        result = ""
        for child in self.children:
            result += child.get_outer_html()
        return result

    def get_outer_html(self):
        opening_tag = self._generate_opening_tag()

        if self.closing_type == ClosingType.SELF_CLOSING:
            return opening_tag

        inner_content = self.get_inner_html()

        if self.display_type == DisplayType.BLOCK:
            formatted_content = "\n" + inner_content + "\n" if inner_content else ""
            return f"{opening_tag}{formatted_content}</{self.tag_name}>"
        else:
            return f"{opening_tag}{inner_content}</{self.tag_name}>"

    def __str__(self):
        return f"Element: <{self.tag_name}> with {self.get_child_count()} children"