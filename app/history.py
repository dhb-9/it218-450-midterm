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
        self.history_df = pd.concat([self.history_df, new_record], ignore_index=True)
        self.history_df.to_csv(self.filepath, index=False)

    def load_history(self):
        try:
            self.history_df = pd.read_csv(self.filepath)
        except FileNotFoundError:
            self.history_df = pd.DataFrame(columns=["operation", "numA", "numB", "result"])

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=["operation", "numA", "numB", "result"])
        self.history_df.to_csv(self.filepath, index=False)

    def delete_history(self):
        import os
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
