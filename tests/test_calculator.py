from calculator import add, subtract, multiply, divide, validate_employee_email


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_validate_employee_email():
    assert validate_employee_email("test@example.com") is True
    assert validate_employee_email("user.name@sub.domain.org") is True
    assert validate_employee_email("plainaddress") is False
    assert validate_employee_email("@domain.com") is False
    assert validate_employee_email("localpart@") is False
    assert validate_employee_email("too@many@ats.com") is False
    assert validate_employee_email("") is False
