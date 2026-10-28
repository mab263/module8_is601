
import logging

import pytest

from app.operations.operations import add, subtract, multiply, divide


def test_add(caplog):
    with caplog.at_level(logging.INFO):
        assert add(2, 3) == 5
    assert "Addition performed" in caplog.text


def test_subtract(caplog):
    with caplog.at_level(logging.INFO):
        assert subtract(5, 3) == 2
    assert "Subtraction performed" in caplog.text


def test_multiply(caplog):
    with caplog.at_level(logging.INFO):
        assert multiply(4, 3) == 12
    assert "Multiplication performed" in caplog.text


def test_divide(caplog):
    with caplog.at_level(logging.INFO):
        assert divide(6, 3) == 2
    assert "Division performed" in caplog.text


def test_divide_by_zero(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            divide(5, 0)
    assert "Division by zero attempted" in caplog.text

