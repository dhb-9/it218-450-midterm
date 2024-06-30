# Update /app/init.py to integrate history management
import os
from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin
from dotenv import load_dotenv
import logging
from app.history import HistoryManager

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
        history_manager = HistoryManager()
        history_manager.load_history()

        while True:
            user_input = input("Enter command (add/subtract/multiply/divide/history/clear/delete) or 'exit' to quit: ").strip().lower()
            if user_input == "exit":
                logger.info("Exiting the app.")
                break
            if user_input == "history":
                print(history_manager.history_df)
            elif user_input == "clear":
                history_manager.clear_history()
                print("History cleared.")
            elif user_input == "delete":
                history_manager.delete_history()
                print("History deleted.")
            else:
                App.execute_command(user_input, history_manager, logger)

    @staticmethod
    def execute_command(command: str, history_manager: HistoryManager, logger: logging.Logger) -> None:
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
                    history_manager.add_record(command, a, b, result)
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
