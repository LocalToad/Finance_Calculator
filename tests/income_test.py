import unittest

import Income

import pytest
from unittest.mock import patch, mock_open

class TestIncome(unittest.TestCase):
    dummy_settings = (
        {'name': 'toad', 'salary': False, 'wage': 0, 'hours': 0},
        {'name': 'snake', 'salary': True, 'wage': 2477.12, 'hours': 0}
    )

    @patch('builtins.input', return_value='y')
    def test_incmain_success(self, mock_input):



        # Success Case, index = 0
        index = 0
        result = Income.incmain(index, self.dummy_settings)
        expected = 0
        assert result == expected

        # Success Case, index = 1
        index = 1
        result = Income.incmain(index, self.dummy_settings)
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

    @patch('builtins.input', return_value='n')
    def test_incmain_exit(self, mock_input):
        index = 0
        expected = True
        result = Income.incmain(index, self.dummy_settings)
        assert result == expected

    @patch('Income.inc_write', return_value=True)
    @patch('builtins.input', return_value='edit')
    def test_incmain_edit_user_exit(self, mock_input, mock_inc_write):
        index = 0
        expected = True
        result = Income.incmain(index, self.dummy_settings)
        assert result == expected

    @patch('builtins.input', return_value='something_else')
    def test_incmain_error_404050(self, mock_input):
        index = 0
        expected = 401050
        result = Income.incmain(index, self.dummy_settings)
        assert result == expected

    @patch('builtins.input', side_effect=['wage', 'y', '20'])
    @patch("builtins.open", new_callable=mock_open)
    @patch('pickle.dump')
    def test_inc_write_success(self, mock_dump, mock_file, mock_input):
        # Test feature wage/hours
        index = 0
        expected = False
        result = Income.inc_write(index, self.dummy_settings)

        mock_file.assert_called_once_with("Dicts.txt", "wb")
        mock_dump.assert_called_once()
        assert expected == result



