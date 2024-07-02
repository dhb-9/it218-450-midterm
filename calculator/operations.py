from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b  # Addition operation

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b  # Subtraction operation

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b  # Multiplication operation

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b != 0:
        return a / b  # Division operation
    raise ValueError("Can't divide by 0")  # Raise error for division by zero
