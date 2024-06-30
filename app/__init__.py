# Modify the setup_logging method in /app/init.py
import os
from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin
from dotenv import load_dotenv
import logging

class App:
    @staticmethod
    def start() -> None:
        App.setup_environment()
        App.setup_logging()
        App.run()

    @staticmethod
    def setup_environment() -> None:
        load_dotenv()

    @staticmethod
    def setup_logging() -> None:
        logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("calc.log"),
                                logging.StreamHandler()
                            ])
        logger = logging.getLogger(__name__)
        environment = os.getenv("ENVIRONMENT", "development")
        logger.info(f"Starting Calculator App in {environment} mode.")

    @staticmethod
    def run() -> None:
        load_plugins("calculator/commands")
        logger = logging.getLogger(__name__)

        while True:
            user_input = input("Enter command (add/subtract/multiply/divide) or 'exit' to quit: ").strip().lower()
            if user_input == "exit":
                logger.info("Exiting the app.")
                break
            App.execute_command(user_input, logger)

    @staticmethod
    def execute_command(command: str, logger: logging.Logger) -> None:
        try:
            if command in ('add', 'subtract', 'multiply', 'divide'):
                a = Decimal(input("Enter first number: "))
                b = Decimal(input("Enter second number: "))

                command_class = get_plugin(command)
                if command_class:
                    command_instance = command_class(a, b)
                    result = command_instance.execute()
                    logger.info(f"Executed ({a} {command} {b}) command with result: {result}")
                    print(f"Result: {result}")
                else:
                    logger.error(f"Command '{command}' not found.")
                    print(f"Command '{command}' not found.")
            else:
                logger.warning(f"Unknown command: {command}")
                print("Unknown command.")
        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)
            print(f"Error: {e}")

if __name__ == "__main__":
    App.start()
