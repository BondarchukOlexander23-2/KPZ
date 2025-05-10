from hero_classes import Warrior, Mage, Paladin
from inventory_decorators import (
    Sword, MagicStaff, Warhammer,
    LeatherArmor, Robe, PlateArmor,
    AmuletOfPower, RingOfHealth, CrownOfWisdom
)


def display_hero_info(hero):
    """Виводить інформацію про героя."""
    print("\n" + "=" * 50)
    print(hero.get_description())
    print("=" * 50)


def main():
    print("Вітаємо у РПГ системі героїв з декораторами інвентарю!")

    # Створення героїв
    warrior = Warrior("Арагорн", level=5)
    mage = Mage("Гендальф", level=7)
    paladin = Paladin("Утер", level=4)

    # Початкові характеристики
    print("\nПОЧАТКОВІ ХАРАКТЕРИСТИКИ ГЕРОЇВ:")
    display_hero_info(warrior)
    display_hero_info(mage)
    display_hero_info(paladin)

    print("\nЕКІПІРУЄМО ГЕРОЇВ:")

    # Екіпіруємо воїна
    equipped_warrior = Sword(warrior, quality=2)
    equipped_warrior = PlateArmor(equipped_warrior)
    equipped_warrior = RingOfHealth(equipped_warrior)

    # Екіпіруємо мага
    equipped_mage = MagicStaff(mage, quality=3)
    equipped_mage = Robe(equipped_mage, quality=2)
    equipped_mage = CrownOfWisdom(equipped_mage)
    equipped_mage = AmuletOfPower(equipped_mage)

    # Екіпіруємо паладіна з багатьма предметами одночасно
    equipped_paladin = Warhammer(paladin)
    equipped_paladin = LeatherArmor(equipped_paladin)
    equipped_paladin = PlateArmor(equipped_paladin)
    equipped_paladin = AmuletOfPower(equipped_paladin)
    equipped_paladin = RingOfHealth(equipped_paladin, quality=2)

    # Характеристики після екіпірування
    print("\nХАРАКТЕРИСТИКИ ПІСЛЯ ЕКІПІРУВАННЯ:")
    display_hero_info(equipped_warrior)
    display_hero_info(equipped_mage)
    display_hero_info(equipped_paladin)

    # Додаткова демонстрація: заміна спорядження
    print("\nЗАМІНА СПОРЯДЖЕННЯ:")
    print("Замінюємо меч воїна на бойовий молот...")
    warrior_with_hammer = Warhammer(warrior, quality=3)
    warrior_with_hammer = PlateArmor(warrior_with_hammer)
    warrior_with_hammer = RingOfHealth(warrior_with_hammer)

    display_hero_info(warrior_with_hammer)

    print("\nПрограма завершена!")


if __name__ == "__main__":
    main()