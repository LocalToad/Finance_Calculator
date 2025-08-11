import unittest
from operator import indexOf

import Hard_Expense

class TestHardExpense(unittest.TestCase):
    dummy_settings = (
        None,
        ["empty", "list"]
    )


    def test_incmain_success(self):
        index = 0
        result = Hard_Expense.settings(self.dummy_settings[index])
        expected = [522, "array"]
        assert result == expected

        index = 1
        result = Hard_Expense.settings(self.dummy_settings[index])
        expected = ["empty", "list"]
        assert result == expected