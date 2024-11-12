import pytest
from calculator.calc_class import Calculator

NUMBER_1 = 3.0
NUMBER_2 = 2.0

@pytest.fixture
def calc():
    return Calculator()

def verify_answer(expected, actual, last_answer):
    assert expected == actual
    assert actual == last_answer

def test_last_answer_init(calc):
    assert calc.last_answer == 0.0

def test_add(calc):
    answer = calc.add(NUMBER_1, NUMBER_2) == 5.0
    verify_answer(5.0, answer, calc.last_answer)

def test_subtract(calc):
    answer = calc.subtract(NUMBER_1, NUMBER_2) == 1.0
    verify_answer(1.0, answer, calc.last_answer)

def test_subtract_negative(calc):
    answer = calc.subtract(NUMBER_2, NUMBER_1) == -1.0
    verify_answer(-1.0, answer, calc.last_answer)

def test_multiply(calc):
    answer = calc.multiply(NUMBER_1, NUMBER_2) == 6.0
    verify_answer(6.0, answer, calc.last_answer)

def test_divide(calc):
    answer = calc.divide(NUMBER_1, NUMBER_2) == 1.5
    verify_answer(1.5, answer, calc.last_answer)

def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError) as e:
        calc.divide(NUMBER_1, 0)
    assert 'division by zero' in str(e.value)

@pytest.mark.parametrize(
        "a, b, expected", 
        [(NUMBER_1, NUMBER_2, NUMBER_2), 
         (NUMBER_2, NUMBER_1, NUMBER_2), 
         (NUMBER_1, NUMBER_1, NUMBER_1)])
def test_minimum(calc, a, b, expected):
    answer = calc.minimum(a, b)
    verify_answer(expected, answer, calc.last_answer)

@pytest.mark.parametrize(
        "a, b, expected", 
        [(NUMBER_1, NUMBER_2, NUMBER_1), 
         (NUMBER_2, NUMBER_1, NUMBER_1), 
         (NUMBER_1, NUMBER_1, NUMBER_1)])
def test_maximum(calc, a, b, expected):
    answer = calc.maximum(a, b)
    verify_answer(expected, answer, calc.last_answer)

# check coverage with pytest-cov
# pytest calc error