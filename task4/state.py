from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def render(self, element, level=0):
        pass

class VisibleState(State):
    def render(self, element, level=0):
        indent = '  ' * level
        print(f"{indent}<{element.name}>")
        if element.text:
            print(f"{indent}  {element.text}")
        for child in element.children:
            child.render(level + 1)
        print(f"{indent}</{element.name}>")

class HiddenState(State):
    def render(self, element, level=0):
        indent = '  ' * level
        print(f"{indent}<!-- {element.name} is hidden -->")

class DisabledState(State):
    def render(self, element, level=0):
        indent = '  ' * level
        print(f"{indent}<{element.name} disabled='true'>")
        if element.text:
            print(f"{indent}  {element.text}")
        for child in element.children:
            child.render(level + 1)
        print(f"{indent}</{element.name}>")

class LoadingState(State):
    def render(self, element, level=0):
        indent = '  ' * level
        print(f"{indent}<{element.name}>")
        print(f"{indent}  [Завантаження...]")
        print(f"{indent}</{element.name}>")
