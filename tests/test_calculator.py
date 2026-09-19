from calculator import add, subtract, multiply, divide, percentage


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_percentage():
    assert percentage(50, 200) == 100.0
    assert percentage(10, 50) == 5.0
