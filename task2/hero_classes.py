from hero import Hero


class Warrior(Hero):
    """
    Клас Воїна - спеціалізується на фізичній атаці та захисті.
    """

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.base_health = 100 + (level * 10)
        self.base_attack = 10 + (level * 2)
        self.base_defense = 8 + (level * 1.5)
        self.base_magic_power = 2 + (level * 0.5)

    def get_name(self):
        return self.name

    def get_health(self):
        return self.base_health

    def get_attack(self):
        return self.base_attack

    def get_defense(self):
        return self.base_defense

    def get_magic_power(self):
        return self.base_magic_power

    def get_description(self):
        return f"Воїн {self.name} (рівень {self.level})\n" \
               f"Здоров'я: {self.get_health()}\n" \
               f"Атака: {self.get_attack()}\n" \
               f"Захист: {self.get_defense()}\n" \
               f"Магічна сила: {self.get_magic_power()}"


class Mage(Hero):
    """
    Клас Мага - спеціалізується на магічній силі.
    """

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.base_health = 70 + (level * 6)
        self.base_attack = 4 + (level * 1)
        self.base_defense = 4 + round((level * 0.8), 2)
        self.base_magic_power = 15 + (level * 3)

    def get_name(self):
        return self.name

    def get_health(self):
        return self.base_health

    def get_attack(self):
        return self.base_attack

    def get_defense(self):
        return self.base_defense

    def get_magic_power(self):
        return self.base_magic_power

    def get_description(self):
        return f"Маг {self.name} (рівень {self.level})\n" \
               f"Здоров'я: {self.get_health()}\n" \
               f"Атака: {self.get_attack()}\n" \
               f"Захист: {self.get_defense()}\n" \
               f"Магічна сила: {self.get_magic_power()}"


class Paladin(Hero):
    """
    Клас Паладіна - клас з гарним захистом та початковими магічними здібностями.
    """

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.base_health = 90 + (level * 8)
        self.base_attack = 8 + (level * 1.5)
        self.base_defense = 10 + (level * 2)
        self.base_magic_power = 8 + (level * 1.5)

    def get_name(self):
        return self.name

    def get_health(self):
        return self.base_health

    def get_attack(self):
        return self.base_attack

    def get_defense(self):
        return self.base_defense

    def get_magic_power(self):
        return self.base_magic_power

    def get_description(self):
        return f"Паладін {self.name} (рівень {self.level})\n" \
               f"Здоров'я: {self.get_health()}\n" \
               f"Атака: {self.get_attack()}\n" \
               f"Захист: {self.get_defense()}\n" \
               f"Магічна сила: {self.get_magic_power()}"