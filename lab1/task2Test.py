from task1.Category import Category
from task1.Product import Product
from task1.Warehouse import Warehouse
from task1.Reporting import Reporting
from task1.Discount import Discount
from task1.Money import Money
from datetime import date

# === 1. Створення товарів ===
product1 = Product("Молоко", 42.50)
product2 = Product("Хліб", 20.00)
product3 = Product("Сир", 95.00)

# === 2. Категорії ===
dairy = Category("Молочні продукти", "Усі продукти з молока")
bakery = Category("Випічка", "Свіжий хліб, булочки, круасани")

dairy.add_product(product1)
dairy.add_product(product3)
bakery.add_product(product2)

# === 3. Знижка ===
discount = Discount("Весняна знижка", 10)  # 10%
discount.add_product(product1)
discount.add_product(product3)

# Виводимо інформацію
dairy.display()
bakery.display()
discount.display()

# === 4. Склад ===
warehouse1 = Warehouse(product1, "л", 50, date.today())
warehouse2 = Warehouse(product2, "шт", 100, date.today())
warehouse3 = Warehouse(product3, "шт", 30, date.today())

warehouse1.display()
warehouse2.display()
warehouse3.display()

# Оновимо дані
warehouse1.update_quantity(20)
warehouse2.update_price(18.50)

# === 5. Облік — Звіти ===
report = Reporting()

# Завезення
report.register_income("INV-001", {
    product1: 20,
    product2: 50,
    product3: 10
})

# Продаж
report.register_expense("EXP-001", {
    product1: 5,
    product2: 3
})

# Складський звіт
report.inventory_report()

# === 6. Застосування знижки ===
original_price = product1.price
discounted_price = discount.calculate_price(original_price)
print(f"\nЦіна '{product1.name}' зі знижкою: {discounted_price:.2f} грн")

# === 7. Робота з грошима ===
money1 = Money(50, 75)
money2 = Money(20, 60)
total = money1 + money2

print("\nГроші:")
money1.display()
money2.display()
print("Разом:")
total.display()
