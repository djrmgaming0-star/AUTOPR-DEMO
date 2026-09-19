import unittest
from calculator import add, subtract, multiply, divide, calculate_discounted_price

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_calculate_discounted_price_zero(self):
        self.assertEqual(calculate_discounted_price(100.0, 0.0), 100.0)

    def test_calculate_discounted_price_normal(self):
        self.assertEqual(calculate_discounted_price(200.0, 20.0), 160.0)

    def test_calculate_discounted_price_full(self):
        self.assertEqual(calculate_discounted_price(50.0, 100.0), 0.0)

    def test_calculate_discounted_price_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(-10.0, 10.0)

    def test_calculate_discounted_price_invalid_rate(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(100.0, -5.0)
        with self.assertRaises(ValueError):
            calculate_discounted_price(100.0, 105.0)

if __name__ == '__main__':
    unittest.main()
