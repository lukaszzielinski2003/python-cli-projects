import pytest
from cli_calculator.core.calculator import Calculator


def test_add():
    assert Calculator.add(2, 3) == 5


def test_subtract():
    assert Calculator.subtract(5, 3) == 2


def test_multiply():
    assert Calculator.multiply(5, 2) == 10


def test_divide():
    assert Calculator.divide(9, 3) == 3
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)


def test_power():
    assert Calculator.power(2, 3) == 8
