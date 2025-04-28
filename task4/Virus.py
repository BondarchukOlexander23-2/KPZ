import copy

class Virus:
    def __init__(self, weight, age, name, species):
        self.weight = weight
        self.age = age
        self.name = name
        self.species = species
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def clone(self):
        # Глибоке копіювання поточного вірусу разом з усіма дітьми
        return copy.deepcopy(self)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}Вірус {self.name}:")
        print(f"{indent}  Species: {self.species}")
        print(f"{indent}  Age: {self.age} years")
        print(f"{indent}  Weight: {self.weight} nm")
        if self.children:
            print(f"{indent}  Children:")
            for child in self.children:
                child.display(level + 1)


# Створення сімейства вірусів (3 покоління)
def create_virus_family():
    # покоління 1 (батько)
    alpha = Virus(20, 5, "Alpha", "Coxsackie")

    # покоління 2
    beta = Virus(18, 3, "Beta", "Coxsackie")
    gamma = Virus(19, 4, "Gamma", "Coxsackie")

    # покоління 3
    delta = Virus(17, 2, "Delta", "Coxsackie")
    epsilon = Virus(16, 1, "Epsilon", "Coxsackie")
    zeta = Virus(18, 2, "Zeta", "Coxsackie")

    gamma.add_child(delta)
    gamma.add_child(epsilon)
    beta.add_child(zeta)
    alpha.add_child(beta)
    alpha.add_child(gamma)

    return alpha


if __name__ == "__main__":
    print("Створення оригінального сімейства вірусів:")
    original_family = create_virus_family()
    original_family.display()

    print("\nКлонування сімейства вірусів:")
    cloned_family = original_family.clone()
    cloned_family.display()

    # змінив клоноване сімейство, щоб показати, що це окремий об'єкт
    cloned_family.name = "Alpha Clone"
    cloned_family.children[0].name = "Beta Clone"
    cloned_family.children[0].children[0].name = "Zeta Clone"

    print("\nОригінальне сімейство (після змін клону):")
    original_family.display()

    print("\nКлоноване сімейство (після змін):")
    cloned_family.display()

    print("\nПеревірка різних об'єктів:")
    print(f"Оригінальний Alpha: {id(original_family)}")
    print(f"Клонований Alpha: {id(cloned_family)}")
    print(f"Оригінальний Beta: {id(original_family.children[0])}")
    print(f"Клонований Beta: {id(cloned_family.children[0])}")