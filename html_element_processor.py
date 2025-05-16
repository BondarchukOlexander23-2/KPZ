from abc import ABC, abstractmethod

class HtmlElementProcessor(ABC):
    """
    Абстрактний клас, який задає шаблонний метод життєвого циклу HTML-елемента
    """

    def process_element(self, element):
        self.on_created(element)
        self.on_inserted(element)
        self.on_styles_applied(element)
        self.on_class_list_applied(element)
        self.on_text_rendered(element)
        self.on_removed(element)

    def on_created(self, element):
        print(f"[Created] Елемент <{element['tag']}> створено.")

    def on_inserted(self, element):
        print(f"[Inserted] Елемент <{element['tag']}> вставлено в DOM.")

    def on_styles_applied(self, element):
        print(f"[Styles] Стилі застосовано: {element.get('style', 'немає')}")

    def on_class_list_applied(self, element):
        classes = element.get('class', [])
        print(f"[ClassList] Класи: {', '.join(classes) if classes else 'відсутні'}")

    def on_text_rendered(self, element):
        print(f"[Text] Вміст: {element.get('text', '')}")

    def on_removed(self, element):
        print(f"[Removed] Елемент <{element['tag']}> видалено з DOM.")
