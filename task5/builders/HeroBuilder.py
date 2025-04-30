from builders.CharacterBuilder import CharacterBuilder
from Character import Character


class HeroBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character()

    def set_height(self, height: float) -> 'HeroBuilder':
        self.character.height = height
        return self

    def set_build(self, build: str) -> 'HeroBuilder':
        self.character.build = build
        return self

    def set_hair_color(self, color: str) -> 'HeroBuilder':
        self.character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> 'HeroBuilder':
        self.character.eye_color = color
        return self

    def add_clothing(self, clothing: str) -> 'HeroBuilder':
        self.character.clothing.append(clothing)
        return self

    def add_inventory(self, item: str) -> 'HeroBuilder':
        self.character.inventory.append(item)
        return self

    def build(self) -> Character:
        return self.character