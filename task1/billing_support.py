from support_handler import SupportHandler


class BillingSupportHandler(SupportHandler):
    def __init__(self):
        super().__init__("Фінансова підтримка")

    def can_handle(self, issue_type):
        return issue_type in ["оплата", "рахунок", "тариф", "підписка", "гроші"]

    def process(self, issue_type):
        return f"Ваш запит '{issue_type}' був оброблений відділом {self.name}. Ми допоможемо вам з фінансовими питаннями."