from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import multiply
from calculator.plugin_loader import register_plugin

# Command class for multiplication operation
class MultiplyCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, multiply)  # Create Calculation object for multiplication

    def execute(self):
        return self.calculation.get_result()  # Execute multiplication and return result

# Register the MultiplyCommand class as a plugin for 'multiply' command
register_plugin('multiply', MultiplyCommand)
