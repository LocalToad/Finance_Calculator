import unittest

import Income

import pytest
from unittest.mock import patch

class TestIncome(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    def test_incmain_success(self, mock_input):



        dummy_settings

        # Success Case, index = 0
        index = 0
        result = Income.incmain(index, Income.user_settings)
        expected = 0
        assert result == expected

        # Success Case, index = 1
        index = 1
        result = Income.incmain(index, Income.user_settings)
        expected = 2477.12
        assert result == expected

        # Success Case, index = 0, toad wages/hours > 0
        index = 0
        settings1 = ({'name':'toad', 'salary':False, 'wage':19, 'hours':32}, {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0})
        settings2 = ({'name':'toad', 'salary':False, 'wage':15, 'hours':45}, {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0})
        settings3 = ({'name':'toad', 'salary':False, 'wage':20, 'hours':40}, {'name':'snake', 'salary':True, 'wage':2477.12, 'hours':0})

        expected1 = 608
        expected2 = 675
        expected3 = 800

        result1 = Income.incmain(index, settings1)
        result2 = Income.incmain(index, settings2)
        result3 = Income.incmain(index, settings3)

        assert result1 == expected1
        assert result2 == expected2
        assert result3 == expected3

        #Failure Case, Salary not a boolean
        index = 0
        settings = ({'name':'stroad', 'salary':1234, 'wage':0, 'hours':0},
                    {'name':'road', 'salary':1234, 'wage':0, 'hours':0},
                    {'name':'moad', 'salary':1234, 'wage':0, 'hours':0})
        result = Income.incmain(index, settings)
        expected = 402001
        assert result == expected



