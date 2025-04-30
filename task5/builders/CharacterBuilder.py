from abc import ABC, abstractmethod
from Character import Character


class CharacterBuilder(ABC):
    @abstractmethod
    def set_height(self, height: float) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def set_build(self, build: str) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def set_hair_color(self, color: str) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def set_eye_color(self, color: str) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def add_clothing(self, clothing: str) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def add_inventory(self, item: str) -> 'CharacterBuilder':
        pass

    @abstractmethod
    def build(self) -> Character:
        pass