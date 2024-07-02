from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import subtract
from calculator.plugin_loader import register_plugin

# Command class for subtraction operation
class SubtractCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, subtract)  # Create Calculation object for subtraction

    def execute(self):
        return self.calculation.get_result()  # Execute subtraction and return result

# Register the SubtractCommand class as a plugin for 'subtract' command
register_plugin('subtract', SubtractCommand)
