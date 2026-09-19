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


def validate_employee_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if email.count('@') != 1:
        return False
    local_part, domain = email.split('@', 1)
    if not local_part or not domain:
        return False
    return True
