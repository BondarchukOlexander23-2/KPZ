class Logger:
    """
        Клас Logger виводить повідомлення в консоль різними кольорами.
    """

    GREEN = '\033[32m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

    def log(self, message):
        print(f"{self.GREEN}[LOG]: {message}{self.RESET}")

    def error(self, message):
        """Виводить повідомлення про помилку червоним кольором."""
        print(f"{self.RED}[ERROR]: {message}{self.RESET}")

    def warn(self, message):
        """Виводить попередження жовтим (оранжевим) кольором."""
        print(f"{self.YELLOW}[WARNING]: {message}{self.RESET}")