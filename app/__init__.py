import os
from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin
from dotenv import load_dotenv
import logging

class App:
    @staticmethod
    def start() -> None:
        load_dotenv()
        environment = os.getenv("ENVIRONMENT")
        
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("calc.log"),
                                logging.StreamHandler()
                            ])
        
        logger = logging.getLogger(__name__)
        logger.info(f"Starting Calculator App in {environment} mode.")
        
        load_plugins("calculator/commands")
        
        while True:
            user_input = input("Enter command (add/subtract/multiply/divide) or 'exit' to quit: ").strip().lower()
            if user_input == "exit":
                logger.info("Exiting the app.")
                break

            try:
                if user_input in ('add', 'subtract', 'multiply', 'divide'):
                    a = Decimal(input("Enter first number: "))
                    b = Decimal(input("Enter second number: "))
                    
                    command_class = get_plugin(user_input)
                    if command_class:
                        command = command_class(a, b)
                        result = command.execute()
                        logger.info(f"Executed ({a} {user_input} {b}) command with result: {result}")
                        print(f"Result: {result}")
                    else:
                        logger.error(f"Command '{user_input}' not found.")
                        print(f"Command '{user_input}' not found.")
                else:
                    logger.warning(f"Unknown command: {user_input}")
                    print("Unknown command.")
            except Exception as e:
                logger.error(f"Error: {e}", exc_info=True)
                print(f"Error: {e}")

if __name__ == "__main__":
    App.start()
