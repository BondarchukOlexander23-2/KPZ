from support_handler import SupportHandler


class TechnicalSupportHandler(SupportHandler):
    def __init__(self):
        super().__init__("Технічна підтримка")

    def can_handle(self, issue_type):
        return issue_type in ["технічна проблема", "несправність", "збій", "підключення"]

    def process(self, issue_type):
        return f"Ваш запит '{issue_type}' був оброблений відділом {self.name}. Ми допоможемо вам вирішити технічну проблему."