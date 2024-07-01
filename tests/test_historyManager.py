# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, invalid-name
import unittest
import os
from app.history import HistoryManager

class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager("test_history.csv")
        self.history_manager.clear_history()

    def tearDown(self):
        self.history_manager.delete_history()

    def test_add_record(self):
        self.history_manager.add_record("add", 1, 2, 3)
        self.history_manager.load_history()
        self.assertEqual(len(self.history_manager.history_df), 1)
        self.assertEqual(self.history_manager.history_df.iloc[0]["result"], 3)

    def test_clear_history(self):
        self.history_manager.add_record("add", 1, 2, 3)
        self.history_manager.clear_history()
        self.history_manager.load_history()
        self.assertEqual(len(self.history_manager.history_df), 0)

    def test_delete_history(self):
        self.history_manager.add_record("add", 1, 2, 3)
        self.history_manager.delete_history()
        self.assertFalse(os.path.exists("test_history.csv"))

if __name__ == '__main__':
    unittest.main()
