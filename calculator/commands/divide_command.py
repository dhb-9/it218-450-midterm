from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide
from calculator.plugin_loader import register_plugin

# Command class for division operation
class DivideCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, divide)  # Create Calculation object for division

    def execute(self):
        return self.calculation.get_result()  # Execute division and return result

# Register the DivideCommand class as a plugin for 'divide' command
register_plugin('divide', DivideCommand)
