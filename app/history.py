import pandas as pd

class HistoryManager:
    def __init__(self, filepath="history.csv"):
        self.filepath = filepath
        self.history_df = pd.DataFrame(columns=["operation", "numA", "numB", "result"])

    def add_record(self, operation, numA, numB, result):
        new_record = pd.DataFrame({
            "operation": [operation],
            "numA": [numA],
            "numB": [numB],
            "result": [result]
        })
        self.history_df = pd.concat([self.history_df, new_record], ignore_index=True)  # Append new record to history
        self.history_df.to_csv(self.filepath, index=False)  # Save history to CSV file

    def load_history(self):
        try:
            self.history_df = pd.read_csv(self.filepath)  # Load history from CSV file
        except FileNotFoundError:
            self.history_df = pd.DataFrame(columns=["operation", "numA", "numB", "result"])  # Handle missing file

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=["operation", "numA", "numB", "result"])  # Clear history DataFrame
        self.history_df.to_csv(self.filepath, index=False)  # Save empty history to CSV file

    def delete_history(self):
        import os
        if os.path.exists(self.filepath):
            os.remove(self.filepath)  # Delete history CSV file if it exists
