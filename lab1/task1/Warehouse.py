from datetime import date, timedelta
from .Product import Product
class Warehouse:
    def __init__(self, product: Product, unit: str, quantity: int, last_delivery_date: date):
        self.product = product
        self.unit = unit
        self.quantity = quantity
        self.last_delivery_date = last_delivery_date

    def update_price(self, new_price: float):
        if new_price <= 0:
            print("Ціна не може бути від'ємною або нульовою.")
            return
        self.product.price = new_price
        print(f"Нова ціна товару '{self.product.name}': {self.product.price:.2f} грн")

    def update_quantity(self, amount: int):
        if self.quantity + amount < 0:
            print(f"Недостатньо товару '{self.product.name}' на складі!")
            return
        self.quantity += amount
        if amount > 0:
            self.last_delivery_date = date.today()
        print(f"Кількість товару '{self.product.name}' оновлено: {self.quantity} {self.unit}")

    def display(self):
        print(f"Товар: {self.product.name}")
        print(f"Одиниця виміру: {self.unit}")
        print(f"Ціна: {self.product.price:.2f} грн")
        print(f"Кількість: {self.quantity}")
        print(f"Дата останнього завозу: {self.last_delivery_date.strftime('%d.%m.%Y')}")
