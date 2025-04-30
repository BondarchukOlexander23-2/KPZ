from builders.HeroBuilder import HeroBuilder
from builders.EnemyBuilder import EnemyBuilder
from Character import Character


class CharacterDirector:
    def construct_hero(self, builder: HeroBuilder) -> Character:
        return (builder
                .set_height(180)
                .set_build("athletic")
                .set_hair_color("blonde")
                .set_eye_color("blue")
                .add_clothing("armor")
                .add_clothing("cape")
                .add_inventory("sword")
                .add_inventory("shield")
                .build())

    def construct_enemy(self, builder: EnemyBuilder) -> Character:
        return (builder
                .set_height(190)
                .set_build("muscular")
                .set_hair_color("black")
                .set_eye_color("red")
                .add_clothing("dark armor")
                .add_clothing("spiked helmet")
                .add_inventory("axe")
                .add_inventory("chains")
                .build())