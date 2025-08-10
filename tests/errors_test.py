import errors
import pytest

def test_errors():
    # Toad-provided success test case
    # input: 402001
    # "income.py", "globalvar", "user_settings", None, "Unrecognized Variable type"

    err_code = 402001
    expected = "income.py", "globalvar", "user_settings", None, "Unrecognized Variable type"
    result = errors.errors(err_code)
    assert result == expected

    # Toad-provided success test case
    # input: 402001
    # "income.py", "incmain()", "is_boolean", None, "Unrecognized Variable type"

    err_code = 401011
    expected = "income.py", "function", "incmain()", "isboolean", "Unrecognized Variable type"
    result = errors.errors(err_code)
    assert result == expected

    err_code = 401050
    expected = "income.py", "function", "incmain()", "cmd", "Incorrect Input"
    result = errors.errors(err_code)
    assert result == expected

    err_code = 401080
    expected = "income.py", "function", "incmain()", "a", "Incorrect Input"
    result = errors.errors(err_code)
    assert result == expected

