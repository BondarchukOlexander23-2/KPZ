class Money:
    def __init__(self, whole: int, cents: int):
        self.whole = whole
        self.cents = cents
        self.normalize()

    def normalize(self):
        if self.cents >= 100:
            self.whole += self.cents // 100
            self.cents %= 100

    def set_amount(self, whole: int, cents: int):
        self.whole = whole
        self.cents = cents
        self.normalize()

    def display(self):
        print(f"{self.whole} гривень і {self.cents} копійок")

    def as_float(self):
        return self.whole + (self.cents / 100)

    def __add__(self, other):
        total_cents = self.whole * 100 + self.cents + other.whole * 100 + other.cents
        return Money(total_cents // 100, total_cents % 100)

