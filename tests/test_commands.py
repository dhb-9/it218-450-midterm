# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, invalid-name
import unittest
from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin

class TestCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load plugins (commands) before running tests
        load_plugins("calculator/commands")

    def test_add_command(self):
        # Test AddCommand
        AddCommand = get_plugin('add')
        command = AddCommand(Decimal('3'), Decimal('5'))
        result = command.execute()
        self.assertEqual(result, Decimal('8'))

    def test_subtract_command(self):
        # Test SubtractCommand
        SubtractCommand = get_plugin('subtract')
        command = SubtractCommand(Decimal('10'), Decimal('3'))
        result = command.execute()
        self.assertEqual(result, Decimal('7'))

    def test_multiply_command(self):
        # Test MultiplyCommand
        MultiplyCommand = get_plugin('multiply')
        command = MultiplyCommand(Decimal('2'), Decimal('4'))
        result = command.execute()
        self.assertEqual(result, Decimal('8'))

    def test_divide_command(self):
        # Test DivideCommand
        DivideCommand = get_plugin('divide')
        command = DivideCommand(Decimal('10'), Decimal('2'))
        result = command.execute()
        self.assertEqual(result, Decimal('5'))

    def test_divide_by_zero(self):
        # Test DivideCommand with division by zero
        DivideCommand = get_plugin('divide')
        command = DivideCommand(Decimal('10'), Decimal('0'))
        with self.assertRaises(ValueError, msg="Should raise ValueError for division by zero"):
            command.execute()

if __name__ == '__main__':
    unittest.main()
