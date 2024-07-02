from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add
from calculator.plugin_loader import register_plugin

# Command class for addition operation
class AddCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, add)  # Create Calculation object for addition

    def execute(self):
        return self.calculation.get_result()  # Execute addition and return result

# Register the AddCommand class as a plugin for 'add' command
register_plugin('add', AddCommand)
