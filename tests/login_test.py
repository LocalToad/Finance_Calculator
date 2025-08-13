import unittest

import login
from unittest.mock import patch


class TestLogin(unittest.TestCase):

    @patch("builtins.input", return_value='toad')
    def test_login_success(self, input_mock):
        dummy_user_keys = ('toad', 'snake')
        expected = 'toad'
        result = login.login(dummy_user_keys)
        assert result == expected

    @patch("builtins.input", return_value='exit')
    def test_login_exit(self, input_mock):
        dummy_user_keys = ('toad', 'snake')
        expected = 'exit'
        result = login.login(dummy_user_keys)
        assert result == expected

    @patch("builtins.input", return_value='shitfuck')
    def test_login_err(self, input_mock):
        dummy_user_keys = ('toad', 'snake')
        expected = False
        result = login.login(dummy_user_keys)
        assert result == expected
