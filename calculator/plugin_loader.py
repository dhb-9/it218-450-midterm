import importlib
import os

# Dictionary to hold registered plugins
plugins = {}

def register_plugin(command_name, command_class):
    plugins[command_name] = command_class

def load_plugins(plugin_folder):
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"calculator.commands.{module_name}")
            # Construct class name by capitalizing each word separated by underscore
            class_name = ''.join(word.capitalize() for word in module_name.split('_'))
            # Retrieve the command class from the module
            command_class = getattr(module, class_name)
            # Register the command with the plugin loader
            register_plugin(module_name, command_class)

def get_plugin(command_name):
    return plugins.get(command_name)
