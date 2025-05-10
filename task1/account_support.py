from support_handler import SupportHandler


class AccountSupportHandler(SupportHandler):
    def __init__(self):
        super().__init__("Підтримка облікових записів")

    def can_handle(self, issue_type):
        return issue_type in ["обліковий запис", "реєстрація", "пароль", "логін", "профіль"]

    def process(self, issue_type):
        return (f"Ваш запит '{issue_type}' був оброблений відділом {self.name}."
                f" Ми допоможемо вам з питаннями облікового запису.")