import pytest

@pytest.mark.accu
def test_accumulator(accu):
    assert accu.count == 0
    # assert accu.add() == 1
    # assert accu.add(2) == 3
    # assert accu.count == 3

@pytest.mark.accu
def test_accu_add_one(accu2):
    assert accu2.add() == 1

@pytest.mark.accu
def test_accu_add_four(accu):
    accu.add(4)
    assert accu.count == 4

@pytest.mark.accu
def test_accu_change_count(accu):
    with pytest.raises(AttributeError, match="property 'count' of 'Accumulator' object has no setter") as e:
        accu.count = 42
        assert accu.count == 42

# python -m pytest (5felev/devops/ora10/tests/test_accu.py) if not found
# ============================= test session starts ==============================
