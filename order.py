import time
from menu import Menu
from food_builder import FoodBuilder

class Order:
    def __init__(self):
        self.menu = Menu()
        self.builder = FoodBuilder()

    def start_order(self):
        self.menu.display_menu()
        choice = self.get_valid_choice("Wybierz co chcesz zamówić: ", [1, 2, 3, 4, 5])
        if choice == 1:
            self.menu.display_burgers()
            self.add_burger()
        elif choice == 2:
            self.menu.display_fries()
            self.add_fries()
        elif choice == 3:
            self.menu.display_salads()
            self.add_salad()
        elif choice == 4:
            self.menu.display_nuggets()
            self.add_nuggets()
        elif choice == 5:
            self.end_order()

    def get_valid_choice(self, prompt, valid_choices):
        while True:
            choice = input(prompt)
            if choice.isdigit() and int(choice) in valid_choices:
                return int(choice)
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def add_burger(self):
        choice = self.get_valid_choice("Wybierz burgera: ", self.menu.burgers.keys())
        burger = self.menu.get_burger(choice)
        if burger:
            self.builder.add_burger(*burger)
            print("Dodawanie burgera do zamówienia...")
            time.sleep(1)
        self.continue_order()

    def add_fries(self):
        choice = self.get_valid_choice("Wybierz frytki: ", self.menu.fries.keys())
        fries = self.menu.get_fries(choice)
        if fries:
            self.builder.add_fries(*fries)
            print("Dodawanie frytek do zamówienia...")
            time.sleep(1)
        self.continue_order()

    def add_salad(self):
        choice = self.get_valid_choice("Wybierz sałatkę: ", self.menu.salads.keys())
        salad = self.menu.get_salad(choice)
        if salad:
            self.builder.add_salad(*salad)
            print("Dodawanie sałatki do zamówienia...")
            time.sleep(1)
        self.continue_order()

    def add_nuggets(self):
        choice = self.get_valid_choice("Wybierz ilość nuggetsów: ", self.menu.nuggets.keys())
        nuggets = self.menu.get_nuggets(choice)
        if nuggets:
            self.builder.add_nuggets(*nuggets)
            print("Dodawanie nuggetsów do zamówienia...")
            time.sleep(1)
        self.continue_order()

    def continue_order(self):
        print("\n")
        self.start_order()

    def end_order(self):
        order = self.builder.get_order()
        print("Twoje zamówienie:")
        for item in order:
            print(item)
        self.builder.clear_order()
