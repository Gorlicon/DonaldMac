import time

class FoodBuilder:
    def __init__(self):
        self.order = []

    def add_burger(self, name):
        self.order.append(f"{name}")
        print("Przygotowywanie burgera...")
        time.sleep(3)

    def add_fries(self, name, size):
        self.order.append(f"{name} {size}")
        print("Smażenie frytek...")
        time.sleep(3)
        print("Pakowanie frytek...")
        time.sleep(1)

    def add_salad(self, name, dressing):
        self.order.append(f"{name} {dressing}")
        print("Przygotowywanie sałatki...")
        time.sleep(3)

    def add_nuggets(self, name, quantity):
        self.order.append(f"{name} {quantity}")
        print("Smażenie nuggetsów...")
        time.sleep(3)
        print("Pakowanie frytek...")
        time.sleep(1)

    def get_order(self):
        return self.order

    def clear_order(self):
        self.order = []