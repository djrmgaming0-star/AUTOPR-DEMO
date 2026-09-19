import unittest
from calculator import add, subtract, multiply, divide, calculate_tax


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_calculate_tax_normal(self):
        self.assertEqual(calculate_tax(100.0, 0.2), 120.0)

    def test_calculate_tax_zero(self):
        self.assertEqual(calculate_tax(100.0, 0.0), 100.0)

    def test_calculate_tax_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_tax(-10.0, 0.2)

    def test_calculate_tax_negative_rate(self):
        with self.assertRaises(ValueError):
            calculate_tax(100.0, -0.05)


if __name__ == '__main__':
    unittest.main()
