from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, element):
        pass

class OnCreatedCommand(Command):
    def execute(self, element):
        print(f"[OnCreated] Створено елемент <{element.name}>")

class OnInsertedCommand(Command):
    def execute(self, element):
        print(f"[OnInserted] Вставлено <{element.name}> у документ")

class OnRemovedCommand(Command):
    def execute(self, element):
        print(f"[OnRemoved] Видалено <{element.name}> з документа")

class OnTextRenderedCommand(Command):
    def execute(self, element):
        print(f"[OnTextRendered] Вміст елемента <{element.name}>: '{element.text}'")

class OnStylesAppliedCommand(Command):
    def execute(self, element):
        print(f"[OnStylesApplied] Стилі для <{element.name}>: {element.attributes.get('style', 'none')}")
