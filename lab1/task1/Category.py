from .Product import Product
class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = set()

    def add_product(self, product: Product):
        if product in self.products:
            print(f"Товар '{product.name}' уже є в категорії '{self.name}'.")
        else:
            self.products.add(product)
            print(f"Товар '{product.name}' додано до категорії '{self.name}'.")

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар '{product.name}' видалено з категорії '{self.name}'.")
        else:
            print(f"Товар '{product.name}' не знайдено в категорії '{self.name}'.")

    def display(self):
        print(f"Категорія: {self.name}")
        print(f"Опис: {self.description}")
        print(f"Кількість товарів: {len(self.products)}")
        print("Товари:")
        for product in self.products:
            print(f"- {product.name}")
