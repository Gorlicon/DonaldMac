class Menu:
    def __init__(self):
        self.burgers = {
            1: "Cheeseburger",
            2: "Chickenburger",
        }

        self.fries = {
            1: ("Frytki", "Małe"),
            2: ("Frytki", "Srednie"),
            3: ("Frytki", "Duże"),
        }

        self.salads = {
            1: ("Sałatka", "Cezar"),
            2: ("Sałatka", "Grecka"),
        }

        self.nuggets = {
            1: ("Nuggetsy", 6),
            2: ("Nuggetsy", 9),
            3: ("Nuggetsy", 20),
        }

    def display_menu(self):
        print("Menu:")
        print("1. Burgery")
        print("2. Frytki")
        print("3. Sałatki")
        print("4. Nuggetsy")
        print("5. Zakończ zamówienie")

    def display_burgers(self):
        print("Burgery:")
        for number, name in self.burgers.items():
            print(f"{number}. {name}")

    def display_fries(self):
        print("Frytki:")
        for number, (name, size) in self.fries.items():
            print(f"{number}. {name} - {size}")

    def display_salads(self):
        print("Sałatki:")
        for number, (name, dressing) in self.salads.items():
            print(f"{number}. {name} {dressing}")

    def display_nuggets(self):
        print("Nuggetsy:")
        for number, (name, quantity) in self.nuggets.items():
            print(f"{number}. {name} ({quantity} kawałków)")

    def get_burger(self, number):
        name = self.burgers.get(number)
        if name:
            return (name,)
        return None

    def get_fries(self, number):
        return self.fries.get(number)

    def get_salad(self, number):
        return self.salads.get(number)

    def get_nuggets(self, number):
        return self.nuggets.get(number)