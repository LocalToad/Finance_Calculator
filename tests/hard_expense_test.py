import unittest
from operator import indexOf

import Hard_Expense

class TestHardExpense(unittest.TestCase):
    dummy_settings = {
        '1':["empty", "list"],
        'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
        'toad':[0, 0, 0, 0, 0, 0, 0]
    }


    def test_incmain_success(self):
        key = None
        result = Hard_Expense.settings(key)
        expected = [0, 0, 0, 0, 0, 0, 0]
        assert result == expected

        key = '1'
        result = Hard_Expense.settings(key, self.dummy_settings)
        expected = ["empty", "list"]
        assert result == expected