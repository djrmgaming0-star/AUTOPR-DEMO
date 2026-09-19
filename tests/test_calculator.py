import unittest
from calculator import add, subtract, multiply, divide, celsius_to_fahrenheit, fahrenheit_to_celsius


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_temperature_validation(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("100")  # type: ignore
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("212")  # type: ignore
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(True)  # type: ignore


if __name__ == "__main__":
    unittest.main()
