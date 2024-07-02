from decimal import Decimal
from typing import Callable

# Class to represent an arithmetic calculation
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a  # First operand
        self.b = b  # Second operand
        self.operation = operation  # Arithmetic operation function

    def get_result(self):
        return self.operation(self.a, self.b)  # Perform arithmetic operation and return result
