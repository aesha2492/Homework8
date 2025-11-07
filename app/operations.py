from decimal import Decimal, InvalidOperation

class CalculatorError(ValueError):
    pass

def _to_decimal(x):
    try:
        return Decimal(str(x))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise CalculatorError(f"Invalid number: {x}") from e

def add(a, b):
    a, b = _to_decimal(a), _to_decimal(b)
    return a + b

def subtract(a, b):
    a, b = _to_decimal(a), _to_decimal(b)
    return a - b

def multiply(a, b):
    a, b = _to_decimal(a), _to_decimal(b)
    return a * b

def divide(a, b):
    a, b = _to_decimal(a), _to_decimal(b)
    if b == 0:
        raise CalculatorError("Division by zero")
    return a / b