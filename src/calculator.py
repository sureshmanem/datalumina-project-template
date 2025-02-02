# Python code to do mathemtical calculations with tests
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


# Add example tests for above functions
def test_add():
    assert add(2, 3) == 6
    assert add(1, 1) == 2


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(1, 1) == 1


def test_divide():
    assert divide(6, 3) == 2
    assert divide(1, 1) == 1
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
