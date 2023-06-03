class FoodItem:
    class FoodItem:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    class Burger(FoodItem):
        def __init__(self, name):
            super().__init__(name)

    class Fries(FoodItem):
        def __init__(self, name, size):
            super().__init__(name)
            self.size = size


    class Salad(FoodItem):
        def __init__(self, name, dressing):
            super().__init__(name)
            self.dressing = dressing


    class Nuggets(FoodItem):
        def __init__(self, name, quantity):
            super().__init__(name)
            self.quantity = quantity