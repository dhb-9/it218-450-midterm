# pylint: disable=missing-module-docstring, missing-function-docstring, invalid-name
from decimal import Decimal
import pytest

from faker import Faker # type: ignore

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator import Calculator

fake = Faker()

### init.py test
def test_addition():
    calculation = Calculation(Decimal('5'), Decimal('5'), add)
    assert calculation.get_result() == Decimal('10')


## calculation.py test
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculator_operations(a, b, operation, expected):
    Calculator.clear_history()
    calculation = Calculation(a, b, operation)
    result = calculation.get_result()
    assert result == expected


def test_calculator_divideby0():
    with pytest.raises(ValueError, match="Can't divide by 0"):
        Calculator.divide(Decimal('5'), Decimal('0'))


## history test
def test_history(): ## looked up
    Calculator.clear_history()
    Calculator.add(1, 1)
    Calculator.subtract(5, 2)
    history = Calculator.get_history()
    assert len(history) == 2
    assert isinstance(history[0], Calculation)
    assert isinstance(history[1], Calculation)
    assert history[0].get_result() == 2
    assert history[1].get_result() == 3

def test_clear_history():
    Calculator.clear_history()
    Calculator.add(1, 1)
    Calculator.clear_history()
    assert len(Calculator.history) == 0


## faker imported
def test_fake_addition():
    a = fake.random_int()
    b = fake.random_int()
    calculation = Calculation(Decimal(a), Decimal(b), add)
    assert calculation.get_result() == a + b
