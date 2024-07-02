import os
from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin
from dotenv import load_dotenv
import logging
from app.history import HistoryManager

class App:
    @staticmethod
    def start() -> None:
        App.setup_environment()  # Set up environment variables
        App.setup_logging()  # Set up logging configuration
        App.run()  # Start the application

    @staticmethod
    def setup_environment() -> None:
        load_dotenv()  # Load environment variables from .env file

    @staticmethod
    def setup_logging() -> None:
        # Configure logging with options from environment variables
        logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("calc.log"),  # Log to file
                                logging.StreamHandler()  # Log to console
                            ])
        logger = logging.getLogger(__name__)
        environment = os.getenv("ENVIRONMENT", "development")  # Get environment setting
        logger.info(f"Starting Calculator App in {environment} mode.")

    @staticmethod
    def run() -> None:
        load_plugins("calculator/commands")  # Dynamically load command plugins
        logger = logging.getLogger(__name__)
        history_manager = HistoryManager()  # Initialize history manager
        history_manager.load_history()  # Load command history from CSV file

        while True:
            user_input = input("Enter command (add/subtract/multiply/divide/history/clear/delete) or 'exit' to quit: ").strip().lower()
            if user_input == "exit":
                logger.info("Exiting the app.")
                break
            if user_input == "history":
                print(history_manager.history_df)  # Print command history to console
            elif user_input == "clear":
                history_manager.clear_history()  # Clear command history
                print("History cleared.")
            elif user_input == "delete":
                history_manager.delete_history()  # Delete command history file
                print("History deleted.")
            else:
                App.execute_command(user_input, history_manager, logger)

    @staticmethod
    def execute_command(command: str, history_manager: HistoryManager, logger: logging.Logger) -> None:
        try:
            if command in ('add', 'subtract', 'multiply', 'divide'):
                a = Decimal(input("Enter first number: "))
                b = Decimal(input("Enter second number: "))

                command_class = get_plugin(command)  # Get command plugin dynamically
                if command_class:
                    command_instance = command_class(a, b)  # Instantiate command class
                    result = command_instance.execute()  # Execute command
                    logger.info(f"Executed ({a} {command} {b}) command with result: {result}")  # Log command execution
                    print(f"Result: {result}")  # Print result to console
                    history_manager.add_record(command, a, b, result)  # Add command to history
                else:
                    logger.error(f"Command '{command}' not found.")
                    print(f"Command '{command}' not found.")
            else:
                logger.warning(f"Unknown command: {command}")
                print("Unknown command.")
        except ValueError as ve:
            logger.error(f"Input error: {ve}", exc_info=True)  # Log input error
            print(f"Input error: {ve}")  # Print input error message
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)  # Log unexpected error
            print(f"Unexpected error: {e}")  # Print unexpected error message

if __name__ == "__main__":
    App.start()  # Start the application
