import pytest

from marrakech.model.directions import Direction
from marrakech.model.position import Pos
from marrakech.model.rug import RugPos


def test_from_tuple() -> None:
    pos1 = Pos(1, 1)
    pos2 = Pos(1, 2)
    rug_pos = RugPos.from_tuple((pos1, pos2))
    assert rug_pos.start == pos1 or rug_pos.start == pos2
    if rug_pos.start == pos1:
        assert rug_pos.direction == Direction.RIGHT
    else:
        assert rug_pos.direction == Direction.LEFT
    pos3 = Pos(2, 2)
    rug_pos = RugPos.from_tuple((pos2, pos3))
    assert rug_pos.start == pos2 or rug_pos.start == pos3
    if rug_pos.start == pos2:
        assert rug_pos.direction == Direction.DOWN
    else:
        assert rug_pos.direction == Direction.UP


def test_from_tuple_raises() -> None:
    pos1 = Pos(1, 1)
    pos2 = Pos(1, 3)
    with pytest.raises(ValueError):
        RugPos.from_tuple((pos1, pos2))
    with pytest.raises(ValueError):
        RugPos.from_tuple((pos2, pos1))
    with pytest.raises(ValueError):
        RugPos.from_tuple((pos1, pos1))
    pos3 = Pos(2, 2)
    with pytest.raises(ValueError):
        RugPos.from_tuple((pos1, pos3))


def test_as_tuple() -> None:
    pos1 = Pos(1, 1)
    pos2 = Pos(1, 2)
    rug_pos = RugPos(pos1, Direction.RIGHT)
    tup = rug_pos.as_tuple()
    assert tup == (pos1, pos2) or tup == (pos2, pos1)
    pos3 = Pos(2, 2)
    rug_pos = RugPos(pos2, Direction.DOWN)
    tup = rug_pos.as_tuple()
    assert tup == (pos2, pos3) or tup == (pos3, pos2)
