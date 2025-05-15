class SmartElement:
    def __init__(self, name, text='', attributes=None):
        self.name = name
        self.text = text
        self.attributes = attributes or {}
        self.children = []
        self.hooks = {
            'on_created': None,
            'on_inserted': None,
            'on_removed': None,
            'on_text_rendered': None,
            'on_styles_applied': None
        }

    def set_hook(self, hook_name, command):
        if hook_name in self.hooks:
            self.hooks[hook_name] = command

    def add_child(self, child):
        self.children.append(child)

    def trigger(self, hook_name):
        command = self.hooks.get(hook_name)
        if command:
            command.execute(self)

    def render(self, level=0):
        indent = "  " * level
        print(f"{indent}<{self.name}>")
        self.trigger('on_text_rendered')
        self.trigger('on_styles_applied')
        for child in self.children:
            child.render(level + 1)
        print(f"{indent}</{self.name}>")
