class Character:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = []
        self.inventory = []

    def __str__(self):
        return (f"Character:\n"
                f"  Height: {self.height} cm\n"
                f"  Build: {self.build}\n"
                f"  Hair color: {self.hair_color}\n"
                f"  Eye color: {self.eye_color}\n"
                f"  Clothing: {', '.join(self.clothing)}\n"
                f"  Inventory: {', '.join(self.inventory)}")