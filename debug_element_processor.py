import time

from html_element_processor import HtmlElementProcessor

class DebugElementProcessor(HtmlElementProcessor):
    def on_created(self, element):
        print(f"[DEBUG] Створення елемента <{element['tag']}> о {time.time()}")
        super().on_created(element)

    def on_removed(self, element):
        print(f"[DEBUG] Видалення елемента <{element['tag']}> о {time.time()}")
        super().on_removed(element)
