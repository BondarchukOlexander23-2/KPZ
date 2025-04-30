from builders.CharacterBuilder import CharacterBuilder
from Character import Character


class EnemyBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character()

    def set_height(self, height: float) -> 'EnemyBuilder':
        self.character.height = height
        return self

    def set_build(self, build: str) -> 'EnemyBuilder':
        self.character.build = build
        return self

    def set_hair_color(self, color: str) -> 'EnemyBuilder':
        self.character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> 'EnemyBuilder':
        self.character.eye_color = color
        return self

    def add_clothing(self, clothing: str) -> 'EnemyBuilder':
        self.character.clothing.append(clothing)
        return self

    def add_inventory(self, item: str) -> 'EnemyBuilder':
        self.character.inventory.append(item)
        return self

    def build(self) -> Character:
        return self.character