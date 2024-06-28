# pylint: disable=missing-module-docstring, missing-function-docstring
from decimal import Decimal

from calculator import Calculator

def test_add():
    Calculator.clear_history()
    result = Calculator.add(Decimal('5'), Decimal('5'))
    assert result == Decimal('10')

def test_subtract():
    Calculator.clear_history()
    result = Calculator.subtract(Decimal('5'), Decimal('5'))
    assert result == Decimal('0')

def test_multiply():
    Calculator.clear_history()
    result = Calculator.multiply(Decimal('5'), Decimal('5'))
    assert result == Decimal('25')

def test_divide():
    Calculator.clear_history()
    result = Calculator.divide(Decimal('5'), Decimal('5'))
    assert result == Decimal('1')
