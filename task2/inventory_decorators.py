from hero import Hero


class InventoryDecorator(Hero):
    """
    Базовий клас-декоратор для предметів інвентарю.
    """

    def __init__(self, hero):
        self.decorated_hero = hero

    def get_name(self):
        return self.decorated_hero.get_name()

    def get_health(self):
        return self.decorated_hero.get_health()

    def get_attack(self):
        return self.decorated_hero.get_attack()

    def get_defense(self):
        return self.decorated_hero.get_defense()

    def get_magic_power(self):
        return self.decorated_hero.get_magic_power()

    def get_description(self):
        return self.decorated_hero.get_description()


# Декоратори зброї
class Sword(InventoryDecorator):
    """Меч збільшує атаку."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Меч"
        self.attack_bonus = 5 * quality

    def get_attack(self):
        return super().get_attack() + self.attack_bonus

    def get_description(self):
        return super().get_description() + (f"\nЕкіпіровано: {self.name} "
                                            f"(+{self.attack_bonus} до атаки)")


class MagicStaff(InventoryDecorator):
    """Магічний посох збільшує магічну силу."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Магічний посох"
        self.magic_bonus = 8 * quality

    def get_magic_power(self):
        return super().get_magic_power() + self.magic_bonus

    def get_description(self):
        return super().get_description() + (f"\nЕкіпіровано: {self.name}"
                                            f" (+{self.magic_bonus} до магічної сили)")


class Warhammer(InventoryDecorator):
    """Бойовий молот збільшує атаку і трохи захист."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Бойовий молот"
        self.attack_bonus = 7 * quality
        self.defense_bonus = 2 * quality

    def get_attack(self):
        return super().get_attack() + self.attack_bonus

    def get_defense(self):
        return super().get_defense() + self.defense_bonus

    def get_description(self):
        return super().get_description() + \
            (f"\nЕкіпіровано: {self.name} (+{self.attack_bonus} до атаки,"
             f" +{self.defense_bonus} до захисту)")


# Декоратори одягу
class LeatherArmor(InventoryDecorator):
    """Шкіряна броня збільшує захист."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Шкіряна броня"
        self.defense_bonus = 5 * quality

    def get_defense(self):
        return super().get_defense() + self.defense_bonus

    def get_description(self):
        return super().get_description() + (f"\nЕкіпіровано: {self.name}"
                                            f" (+{self.defense_bonus} до захисту)")


class Robe(InventoryDecorator):
    """Мантія збільшує магічну силу і додає трохи здоров'я."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Мантія мага"
        self.magic_bonus = 5 * quality
        self.health_bonus = 10 * quality

    def get_magic_power(self):
        return super().get_magic_power() + self.magic_bonus

    def get_health(self):
        return super().get_health() + self.health_bonus

    def get_description(self):
        return super().get_description() + \
            (f"\nЕкіпіровано: {self.name} (+{self.magic_bonus}"
             f" до магічної сили, +{self.health_bonus} до здоров'я)")


class PlateArmor(InventoryDecorator):
    """Латна броня значно збільшує захист, але зменшує швидкість атаки."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Латна броня"
        self.defense_bonus = 10 * quality
        self.attack_penalty = -1 * quality

    def get_defense(self):
        return super().get_defense() + self.defense_bonus

    def get_attack(self):
        return max(1, super().get_attack() + self.attack_penalty)

    def get_description(self):
        return super().get_description() + \
            (f"\nЕкіпіровано: {self.name} (+{self.defense_bonus} до захисту,"
             f" {self.attack_penalty} до атаки)")


# Декоратори артефактів
class AmuletOfPower(InventoryDecorator):
    """Амулет сили збільшує силу атаки та магічну."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Амулет сили"
        self.attack_bonus = 3 * quality
        self.magic_bonus = 3 * quality

    def get_attack(self):
        return super().get_attack() + self.attack_bonus

    def get_magic_power(self):
        return super().get_magic_power() + self.magic_bonus

    def get_description(self):
        return super().get_description() + \
            (f"\nЕкіпіровано: {self.name} (+{self.attack_bonus} до атаки, "
             f"+{self.magic_bonus} до магічної сили)")


class RingOfHealth(InventoryDecorator):
    """Перстень здоров'я збільшує максимальну кількість здоров'я."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Перстень здоров'я"
        self.health_bonus = 20 * quality

    def get_health(self):
        return super().get_health() + self.health_bonus

    def get_description(self):
        return super().get_description() + (f"\nЕкіпіровано: {self.name} "
                                            f"(+{self.health_bonus} до здоров'я)")


class CrownOfWisdom(InventoryDecorator):
    """Корона влади та мудрості збільшує магічну силу і трохи захист."""

    def __init__(self, hero, quality=1):
        super().__init__(hero)
        self.quality = quality
        self.name = "Корона мудрості"
        self.magic_bonus = 6 * quality
        self.defense_bonus = 2 * quality

    def get_magic_power(self):
        return super().get_magic_power() + self.magic_bonus

    def get_defense(self):
        return round(super().get_defense() + self.defense_bonus, 2)

    def get_description(self):
        return super().get_description() + \
            (f"\nЕкіпіровано: {self.name} (+{self.magic_bonus} до магічної сили,"
             f" +{self.defense_bonus} до захисту)")