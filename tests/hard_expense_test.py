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
        index = None
        result = Hard_Expense.settings(index)
        expected = {
                    'snake':[522, 30, 185, 175, 140.32, 168.16, 39.45],
                    'toad':[0, 0, 0, 0, 0, 0, 0]
                    }
        assert result == expected

        index = 0
        result = Hard_Expense.settings(self.dummy_settings[index])
        expected = ["empty", "list"]
        assert result == expected