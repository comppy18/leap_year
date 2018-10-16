import pytest
from leap_year import is_leap_year

@pytest.fixture(params=[2000, 1996, 1600])
def true_values(request):
    return request.param

def test_true_values(true_values):
    assert is_leap_year(true_values) == True

@pytest.fixture(params=[1999, 1998, 1900, 1800])
def false_values(request):
    return request.param

def test_false_values(false_values):
    assert is_leap_year(false_values) == False
