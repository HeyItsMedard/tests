import pytest
from calculator.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0

def test_add():
    assert add(NUMBER_1, NUMBER_2) == 5.0

def test_subtract():
    assert subtract(NUMBER_1, NUMBER_2) == 1.0

def test_subtract_negative():
    assert subtract(NUMBER_2, NUMBER_1) == -1.0

def test_multiply():
    assert multiply(NUMBER_1, NUMBER_2) == 6.0

def test_divide():
    assert divide(NUMBER_1, NUMBER_2) == 1.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)

@pytest.mark.parametrize("a, b, expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_1, NUMBER_1, NUMBER_1)
])
def test_minimum(a, b, expected):
    assert minimum(a, b) == expected
    
@pytest.mark.parametrize("a, b, expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1)
])
def test_maximum(a, b, expected):
    assert maximum(a, b) == expected
    
def test_maximum_greater():
    assert maximum(NUMBER_1, NUMBER_2) == NUMBER_1

def test_maximum_lesser():
    assert maximum(NUMBER_1, NUMBER_2) == NUMBER_1

def test_max_equals():
    assert maximum(NUMBER_1, NUMBER_1) == NUMBER_1

