from builders.HeroBuilder import HeroBuilder
from builders.EnemyBuilder import EnemyBuilder
from Director import CharacterDirector


def main():
    director = CharacterDirector()

    hero_builder = HeroBuilder()
    hero = director.construct_hero(hero_builder)
    print("=== Hero ===")
    print(hero)

    enemy_builder = EnemyBuilder()
    enemy = director.construct_enemy(enemy_builder)
    print("\n=== Enemy ===")
    print(enemy)


if __name__ == "__main__":
    main()