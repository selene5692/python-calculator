import pytest
from src.calc import add, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide_by_zero():
    # expect app to explitly raise a ValueError if user divides by zero
    with pytest.raises(ValueError):
        divide(10, 0)
