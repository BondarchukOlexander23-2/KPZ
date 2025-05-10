import time
from technical_support import TechnicalSupportHandler
from billing_support import BillingSupportHandler
from account_support import AccountSupportHandler
from general_support import GeneralSupportHandler


class SupportSystem:
    def __init__(self):
        technical = TechnicalSupportHandler()
        billing = BillingSupportHandler()
        account = AccountSupportHandler()
        general = GeneralSupportHandler()

        technical.set_next(billing).set_next(account).set_next(general)

        self.handler_chain = technical

    def display_menu(self):
        print("\n===== СИСТЕМА ПІДТРИМКИ КОРИСТУВАЧІВ =====")
        print("Оберіть категорію вашого запиту:")
        print("1. Технічні проблеми (обладнання, підключення, несправності)")
        print("2. Фінансові питання (оплата, рахунки, тарифи)")
        print("3. Питання облікового запису (реєстрація, пароль, профіль)")
        print("4. Загальні питання (інформація, консультація)")
        print("0. Вихід з системи")

    def process_level_choice(self, choice):
        issue_mapping = {
            "1": "технічна проблема",
            "2": "оплата",
            "3": "обліковий запис",
            "4": "інформація"
        }

        if choice in issue_mapping:
            return issue_mapping[choice]
        return None

    def get_detailed_issue(self, category):
        category_details = {
            "технічна проблема": ["несправність", "збій", "підключення"],
            "оплата": ["рахунок", "тариф", "підписка", "гроші"],
            "обліковий запис": ["реєстрація", "пароль", "логін", "профіль"],
            "інформація": ["консультація", "загальне питання", "допомога"]
        }

        if category in category_details:
            details = category_details[category]
            print(f"\nУточніть ваше питання в категорії {category.upper()}:")
            for i, detail in enumerate(details, 1):
                print(f"{i}. {detail.capitalize()}")

            choice = input("Ваш вибір (1-4): ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(details):
                    return details[index]
            except ValueError:
                pass

        return category

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nВаш вибір (0-4): ")

            if choice == "0":
                print("Дякуємо за використання нашої системи підтримки. До побачення!")
                break

            issue_category = self.process_level_choice(choice)
            if not issue_category:
                print("Невірний вибір. Спробуйте знову.")
                continue

            detailed_issue = self.get_detailed_issue(issue_category)

            print("\nОброблюємо ваш запит...")
            time.sleep(1)

            result = self.handler_chain.handle(detailed_issue)

            if result:
                print(f"\n{result}")

                # Запитуємо чи бажає користувач повернутися до головного меню
                continue_choice = input("\nБажаєте повернутися до головного меню? (так/ні): ")
                if continue_choice.lower() not in ["так", "yes", "y", "т"]:
                    print("Дякуємо за використання нашої системи підтримки. До побачення!")
                    break
            else:
                print("\nНа жаль, ми не змогли обробити ваш запит. Спробуйте інший варіант.")