import unittest
from operator import indexOf

import Hard_Expense

class TestHardExpense(unittest.TestCase):
    dummy_settings = {
        '1':["empty", "list"],
        'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
        'toad':[0, 0, 0, 0, 0, 0, 0]
    }

    def test_expense_success(self):
        arr = None
        result = Hard_Expense.expense(None, arr)
        expected = 0
        assert result == expected

        arr = [1,1,1]
        result = Hard_Expense.expense(None, arr)
        expected = 3
        assert result == expected

        arr = [240, 330, 110]
        result = Hard_Expense.expense(None, arr)
        expected = 680
        assert result == expected

    def test_settings_success(self):
        key = None
        result = Hard_Expense.settings(key)
        expected = [0, 0, 0, 0, 0, 0, 0]
        assert result == expected

        key = '1'
        result = Hard_Expense.settings(key, self.dummy_settings)
        expected = ["empty", "list"]
        assert result == expected