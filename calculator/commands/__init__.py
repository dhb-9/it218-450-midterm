from .add_command import AddCommand
from .subtract_command import SubtractCommand
from .multiply_command import MultiplyCommand
from .divide_command import DivideCommand
from ..plugin_loader import register_plugin

# Register each command
register_plugin('add', AddCommand)
register_plugin('subtract', SubtractCommand)
register_plugin('multiply', MultiplyCommand)
register_plugin('divide', DivideCommand)
