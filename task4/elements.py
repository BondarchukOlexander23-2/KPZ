from state import VisibleState

class Element:
    def __init__(self, name, text=''):
        self.name = name
        self.text = text
        self.children = []
        self.state = VisibleState()

    def add_child(self, child):
        self.children.append(child)

    def set_state(self, state):
        self.state = state

    def propagate_state(self, state):
        self.set_state(state)
        for child in self.children:
            child.propagate_state(state)

    def render(self, level=0):
        self.state.render(self, level)
