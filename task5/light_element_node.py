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
        self.event_listeners = {}  # New dictionary to store event listeners

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

    # New method to add event listeners
    def add_event_listener(self, event_type, callback_function):
        """
        Adds an event listener to the element for a specified event type

        Args:
            event_type (str): The event type to listen for (e.g., "click", "mouseover", etc.)
            callback_function (callable): The function to execute when the event occurs

        Returns:
            LightElementNode: The current element for method chaining
        """
        if event_type not in self.event_listeners:
            self.event_listeners[event_type] = []

        self.event_listeners[event_type].append(callback_function)
        return self

    # New method to trigger events
    def trigger_event(self, event_type, event_data=None):
        """
        Triggers all callbacks registered for the specified event type

        Args:
            event_type (str): The event type to trigger
            event_data (dict, optional): Data to pass to the callback functions

        Returns:
            bool: True if at least one event was triggered, False otherwise
        """
        if event_type in self.event_listeners and self.event_listeners[event_type]:
            for callback in self.event_listeners[event_type]:
                callback(self, event_data)
            return True
        return False

    # New method to remove event listeners
    def remove_event_listener(self, event_type, callback_function=None):
        """
        Removes an event listener or all listeners for a specified event type

        Args:
            event_type (str): The event type to remove the listener(s) from
            callback_function (callable, optional): The specific callback to remove.
                              If None, removes all callbacks for the event type.

        Returns:
            LightElementNode: The current element for method chaining
        """
        if event_type in self.event_listeners:
            if callback_function is None:
                self.event_listeners[event_type] = []
            else:
                self.event_listeners[event_type] = [
                    cb for cb in self.event_listeners[event_type]
                    if cb != callback_function
                ]
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

        # Add event listeners as inline JS (for HTML output)
        for event_type, callbacks in self.event_listeners.items():
            if callbacks:  # Only add if there are callbacks
                # For HTML output, we just show that there's a listener attached
                result += f' on{event_type}="/* Event listener attached */"'

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