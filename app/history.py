# /calculator/history_manager.py
import pandas as pd

class HistoryManager:
    def __init__(self, filename='history.csv'):
        self.filename = filename
        self.df = pd.DataFrame(columns=['a', 'b', 'operation', 'result'])

    def save(self):
        self.df.to_csv(self.filename, index=False)

    def load(self):
        self.df = pd.read_csv(self.filename)

    def clear(self):
        self.df = pd.DataFrame(columns=['a', 'b', 'operation', 'result'])
        self.save()

    def add_record(self, a, b, operation, result):
        self.df = self.df.append({'a': a, 'b': b, 'operation': operation, 'result': result}, ignore_index=True)
        self.save()
