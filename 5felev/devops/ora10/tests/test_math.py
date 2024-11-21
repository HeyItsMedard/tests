import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

@pytest.mark.math
def test_zero_multiply():
    assert 0 * 100 == 0

results = [
    (2, 3, 6), # positive integers
    (1, 99, 99), # identity
    (0, 100, 0), # zero
    (3, -4, -12), # positive by negative
    (-5, -5, 25), # negative by negative
    (2.5, 6.7, 16.75) # floats
]

@pytest.mark.parametrize("a, b, c", results)
def test_multiplication(a, b, c):
    assert a * b == c

for a, b, c in results:
    test_multiplication(a, b, c)

# python -m pytest (5felev/devops/ora10/tests/test_math.py) if not found