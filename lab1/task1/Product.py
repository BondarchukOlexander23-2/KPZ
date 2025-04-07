class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def decrease_price(self, amount: float):
        if amount <= 0:
            print("Знижка не може бути від'ємною.")
            return
        self.price = max(0, self.price - amount)
        print(f"Нова ціна товару '{self.name}': {self.price:.2f} грн")

    def display(self):
        print(f"Товар: {self.name}, Ціна: {self.price:.2f} грн")
