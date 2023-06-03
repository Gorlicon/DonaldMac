from unittest import TestCase, mock
import unittest
from unittest.mock import patch
from io import StringIO
from order import Order
from menu import Menu
from food_builder import FoodBuilder

class TestOrder(unittest.TestCase):

#zamawianie cheeseburgera
    def test_cheeseburger(self):
        menu = Menu()
        builder = FoodBuilder()
        burger = menu.get_burger(1)
        if burger:
            builder.add_burger(*burger)

        order = builder.get_order()
        self.assertIn("Cheeseburger", order)

#zamawianie średnich frytek
    def test_fries(self):
        menu = Menu()
        builder = FoodBuilder()
        fries = menu.get_fries(2)
        if fries:
            builder.add_fries(*fries)

        order = builder.get_order()
        self.assertIn("Frytki Srednie", order)

#zamawianie Sałatki Ceasar
    def test_salads(self):
        menu = Menu()
        builder = FoodBuilder()

        salad = menu.get_salad(1)
        if salad:
            builder.add_salad(*salad)

        order = builder.get_order()
        self.assertIn("Sałatka Cezar", order)

#zamawianie 20 nuggetsów
    def test_nuggetsy(self):
        menu = Menu()
        builder = FoodBuilder()

        nuggets = menu.get_nuggets(3)
        if nuggets:
            builder.add_nuggets(*nuggets)

        order = builder.get_order()
        self.assertIn("Nuggetsy 20", order)

#automatyczne wprowadzanie danych
    def test_automatic(self):
        menu = Menu()
        order = Order()

        with mock.patch('sys.stdout', new=StringIO()) as fake_output:
            with mock.patch('builtins.input', side_effect=['1', '1', '5']):
                order.start_order()

        # Sprawdzanie, czy zamówienie zawiera "Cheeseburger"
        order_builder = order.builder
        order_builder.order = order_builder.get_order()
        output = fake_output.getvalue()
        self.assertIn("Cheeseburger", output, "Zamówienie nie zawiera Cheeseburger")

        # Wyświetlanie menu
        print("\nWyświetlanie menu:")
        print(output)

#sprawdzanie czy aplikacja zabezpieczona przed blednymi inputami
    def test_invalid(self):
        order = Order()

        invalid_inputs = ['6', '1234567890988776', '-1', '0', 'NULL', 'slowo']

        # Przechwytywanie danych wejściowych i wyjściowych
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', side_effect=invalid_inputs + ['5']):
                try:
                    order.start_order()
                except SystemExit:
                    pass

        # Sprawdzanie, czy nie ma błędów
        output = fake_output.getvalue()
        self.assertNotIn("Traceback", output, "Wystąpił błąd podczas wykonywania aplikacji")

        # Wyświetlanie menu
        print("\nWyświetlanie menu:")
        print(output)


    def test_order3(self):
        order = Order()
        user_input = ['1', '1', '2', '2', '2', '1', '5']

        with patch('sys.stdout', new=StringIO()) as mock_output:
            with patch('builtins.input', side_effect=user_input):
                order.start_order()

        order_output = mock_output.getvalue()
        order_items = order_output.split('\n')
        order_items_count = len(order_items) - 51  #Pominięcie nadmiarowych linijek tekstu (menu, informacje o zamowienie itp.)
        self.assertEqual(order_items_count, 3)

if __name__ == '__main__':
    unittest.main()