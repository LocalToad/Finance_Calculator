import unittest

import Income

from unittest.mock import patch, mock_open

class TestIncome(unittest.TestCase):
    dummy_settings = {
        "toad": {'salary': False, 'wage': 0, 'hours': 0},
        "snake": {'salary': True, 'wage': 2477.12, 'hours': 0}
    }

    @patch('builtins.input', return_value='y')
    def test_incmain_success(self, mock_input):

        # Success Case, index = 0
        key = "toad"
        result = Income.incmain(key, self.dummy_settings)
        expected = 0
        assert result == expected

        # Success Case, index = 1
        key = "snake"
        result = Income.incmain(key, self.dummy_settings)
        expected = 2477.12
        assert result == expected

        # Success Case, index = 0, toad wages/hours > 0
        key = "toad"
        settings1 = {"toad": {'salary':False, 'wage':19, 'hours':32}, "snake": {'salary':True, 'wage':2477.12, 'hours':0}}
        settings2 = {"toad": {'salary':False, 'wage':15, 'hours':45}, "snake": {'salary':True, 'wage':2477.12, 'hours':0}}
        settings3 = {"toad": {'salary':False, 'wage':20, 'hours':40}, "snake": {'salary':True, 'wage':2477.12, 'hours':0}}

        expected1 = 608
        expected2 = 675
        expected3 = 800

        result1 = Income.incmain(key, settings1)
        result2 = Income.incmain(key, settings2)
        result3 = Income.incmain(key, settings3)

        assert result1 == expected1
        assert result2 == expected2
        assert result3 == expected3

        #Failure Case, Salary not a boolean
        key = "stroad"
        settings = {"stroad": {'salary':1234, 'wage':0, 'hours':0},
                    "road": {'salary':1234, 'wage':0, 'hours':0},
                    "moad": {'salary':1234, 'wage':0, 'hours':0}}
        result = Income.incmain(key, settings)
        expected = 402001
        assert result == expected

    def test_incmain_missing_args(self):
        # Missing Key, should return Truey value
        key = None
        result = Income.incmain(key, self.dummy_settings)
        expected = True
        assert result == expected

        # Missing settings dict, should return Truey value
        key = "something"
        settings = None
        result = Income.incmain(key, settings)
        assert result == expected

        # settings_dict is something other than a dict, should return Truey value
        key = "something"
        settings = 1234
        result = Income.incmain(key, settings)
        assert result == expected


    @patch('builtins.input', return_value='n')
    def test_incmain_exit(self, mock_input):
        key = "toad"
        expected = True
        result = Income.incmain(key, self.dummy_settings)
        assert result == expected

    @patch('Income.inc_write', return_value=True)
    @patch('builtins.input', return_value='edit')
    def test_incmain_edit_user_exit(self, mock_input, mock_inc_write):
        key = "toad"
        expected = True
        result = Income.incmain(key, self.dummy_settings)
        assert result == expected

    @patch('builtins.input', return_value='something_else')
    def test_incmain_error_404050(self, mock_input):
        key = "toad"
        expected = 401050
        result = Income.incmain(key, self.dummy_settings)
        assert result == expected

    @patch('builtins.input', side_effect=['wage', 'y', '20'])
    @patch("builtins.open", new_callable=mock_open)
    @patch('json.dump')
    def test_inc_write_success(self, mock_dump, mock_file, mock_input):
        # Test feature wage/hours
        key = "toad"
        expected = False
        result = Income.inc_write(key, self.dummy_settings)

        mock_file.assert_called_once_with("Dicts.json", "wb")
        mock_dump.assert_called_once()
        assert expected == result



