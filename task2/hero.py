from abc import ABC, abstractmethod


class Hero(ABC):
    """
    Абстрактний базовий клас для всіх героїв у грі.
    """

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def get_attack(self):
        pass

    @abstractmethod
    def get_defense(self):
        pass

    @abstractmethod
    def get_magic_power(self):
        pass

    @abstractmethod
    def get_description(self):
        pass