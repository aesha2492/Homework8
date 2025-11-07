import pytest
from decimal import Decimal
from app import operations as ops
from app.operations import CalculatorError

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, "3"), ("2.5", 0.5, "3.0"), (-1, 1, "0")
])
def test_add(a, b, expected):
    assert ops.add(a, b) == Decimal(expected)

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, "3"), ("2.5", 0.5, "2.0"), (-1, -1, "0")
])
def test_subtract(a, b, expected):
    assert ops.subtract(a, b) == Decimal(expected)

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, "12"), ("2.5", 2, "5.0"), (-2, 3, "-6")
])
def test_multiply(a, b, expected):
    assert ops.multiply(a, b) == Decimal(expected)

@pytest.mark.parametrize("a,b,expected", [
    (8, 2, "4"), ("2.5", 0.5, "5.0")
])
def test_divide(a, b, expected):
    # Depending on inputs, Decimal may render "5" or "5.0";
    # comparing Decimals numerically avoids representation issues.
    assert ops.divide(a, b) == Decimal(expected)

def test_divide_by_zero():
    with pytest.raises(CalculatorError):
        ops.divide(1, 0)
