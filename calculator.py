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


def calculate_tax(price: float, tax_rate: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return price * (1 + tax_rate)
