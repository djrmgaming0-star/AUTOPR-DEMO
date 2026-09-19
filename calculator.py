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


def calculate_discounted_price(price: float, discount_rate: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_rate < 0 or discount_rate > 100:
        raise ValueError("Discount rate must be between 0 and 100")
    return price * (1 - discount_rate / 100.0)
