def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def celsius_to_fahrenheit(celsius: float) -> float:
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise ValueError("Input must be a number")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if not isinstance(fahrenheit, (int, float)) or isinstance(fahrenheit, bool):
        raise ValueError("Input must be a number")
    return (fahrenheit - 32) * 5 / 9
