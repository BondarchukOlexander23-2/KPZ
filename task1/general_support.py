from support_handler import SupportHandler


class GeneralSupportHandler(SupportHandler):
    def __init__(self):
        super().__init__("Загальна підтримка")

    def can_handle(self, issue_type):
        return issue_type in ["інформація", "консультація", "загальне питання", "допомога"]

    def process(self, issue_type):
        return f"Ваш запит '{issue_type}' був оброблений відділом {self.name}. Ми надамо вам загальну консультацію."