import pytest
from app.operations import add, subtract, multiply, divide


def test_add_init():
    assert add(2, 3) == 5


def test_subtract_init():
    assert subtract(5, 3) == 2


def test_multiply_init():
    assert multiply(4, 3) == 12


def test_divide_init():
    assert divide(10, 2) == 5


def test_divide_by_zero_init():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)