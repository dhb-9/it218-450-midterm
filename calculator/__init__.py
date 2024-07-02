from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
    
class Calculator:
    history = []  # List to store calculation history

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)  # Create calculation object
        Calculator.history.append(calculation)  # Add calculation to history
        return calculation.get_result()  # Return calculation result

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, subtract)  # Create calculation object
        Calculator.history.append(calculation)  # Add calculation to history
        return calculation.get_result()  # Return calculation result
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, multiply)  # Create calculation object
        Calculator.history.append(calculation)  # Add calculation to history
        return calculation.get_result()  # Return calculation result
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)  # Create calculation object
        Calculator.history.append(calculation)  # Add calculation to history
        return calculation.get_result()  # Return calculation result

    @staticmethod
    def clear_history():
        Calculator.history.clear()  # Clear calculation history

    @staticmethod
    def get_history():
        return Calculator.history  # Return calculation history
