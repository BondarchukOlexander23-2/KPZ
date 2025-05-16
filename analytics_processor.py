from html_element_processor import HtmlElementProcessor


class AnalyticsProcessor(HtmlElementProcessor):
    def __init__(self):
        self.stats = {"created": 0, "removed": 0}

    def on_created(self, element):
        self.stats["created"] += 1
        super().on_created(element)

    def on_removed(self, element):
        self.stats["removed"] += 1
        super().on_removed(element)

    def report(self):
        print(f"[Analytics] Створено: {self.stats['created']}, Видалено: {self.stats['removed']}")
