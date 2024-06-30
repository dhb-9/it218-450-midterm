from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import subtract
from calculator.plugin_loader import register_plugin

class SubtractCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, subtract)

    def execute(self):
        return self.calculation.get_result()

# Register the command with the plugin loader
register_plugin('subtract', SubtractCommand)
