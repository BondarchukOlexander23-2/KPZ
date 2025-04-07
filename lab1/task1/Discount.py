from datetime import date, timedelta
from .Product import Product
class Discount:
    def __init__(self, name: str, percent: float, start_date: date = None, end_date: date = None):
        self.name = name
        self.percent = max(0, min(100, percent))
        self.start_date = start_date or date.today()
        self.end_date = end_date or (date.today() + timedelta(days=30))
        self.applicable_products = []

    def add_product(self, product: Product):
        if product not in self.applicable_products:
            self.applicable_products.append(product)
            print(f"Товар '{product.name}' додано до акції '{self.name}'")
        else:
            print(f"Товар '{product.name}' вже бере участь в акції '{self.name}'")

    def is_active(self):
        today = date.today()
        return self.start_date <= today <= self.end_date

    def calculate_price(self, original_price: float):
        if self.is_active():
            discount_amount = original_price * (self.percent / 100)
            return original_price - discount_amount
        return original_price

    def display(self):
        status = "Активна" if self.is_active() else "Неактивна"
        print(f"Акція: {self.name}")
        print(f"Знижка: {self.percent}%")
        print(f"Статус: {status}")
        print(f"Період: {self.start_date.strftime('%d.%m.%Y')} - {self.end_date.strftime('%d.%m.%Y')}")
        print(f"Товари, що беруть участь у акції ({len(self.applicable_products)}):")
        for product in self.applicable_products:
            print(f"- {product.name}")
