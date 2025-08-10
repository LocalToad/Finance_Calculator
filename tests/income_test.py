import Income

import pytest


def test_incmain():


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

    #Failure Case, Salary not a boolean
    index = 0
    settings = ({'name':'stroad', 'salary':1234, 'wage':0, 'hours':0},
                {'name':'road', 'salary':1234, 'wage':0, 'hours':0},
                {'name':'moad', 'salary':1234, 'wage':0, 'hours':0})
    result = Income.incmain(index, settings)
    expected = 402001
    assert result == expected
