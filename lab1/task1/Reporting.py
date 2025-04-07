from .Product import Product
class Reporting:
    def __init__(self):
        self.stock = {}  # dict[Product, int]
        self.income_reports = []
        self.expense_reports = []

    def register_income(self, invoice_number, items: dict[Product, int]):
        self.income_reports.append({"invoice": invoice_number, "items": items})
        for product, quantity in items.items():
            self.stock[product] = self.stock.get(product, 0) + quantity
        print(f"Прибуткова накладна №{invoice_number} зареєстрована.")

    def register_expense(self, invoice_number, items: dict[Product, int]):
        for product, quantity in items.items():
            if self.stock.get(product, 0) < quantity:
                print(f"Недостатньо {product.name} на складі!")
                return
        self.expense_reports.append({"invoice": invoice_number, "items": items})
        for product, quantity in items.items():
            self.stock[product] -= quantity
        print(f"Видаткова накладна №{invoice_number} зареєстрована.")

    def inventory_report(self):
        print("Залишки на складі:")
        for product, quantity in self.stock.items():
            print(f"{product.name}: {quantity}")
