from marrakech.model.board import Board
from marrakech.model.color import Color
from marrakech.model.directions import Direction
from marrakech.model.position import Pos
from marrakech.model.rug import Rug, RugPos


def test_init() -> None:
    board = Board()
    assert len(board.fields) == 7
    for row in board.fields:
        assert len(row) == 7
        for field in row:
            assert field == Color.EMPTY


def test_get() -> None:
    board = Board()
    for i in range(7):
        for j in range(7):
            assert board.get(Pos(i, j)) == Color.EMPTY


def test_set() -> None:
    board = Board()
    for i in range(7):
        for j in range(7):
            assert board.get(Pos(i, j)) == Color.EMPTY
            board._set(Pos(i, j), Color.RED)
            assert board.get(Pos(i, j)) == Color.RED


def test_place_rug() -> None:
    #First board
    board = Board()

    pos = Pos(1,1)
    color = Color.RED
    dir = Direction.RIGHT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)

    board.place_rug(rug)

    assert board.get(Pos(1, 1)) == Color.RED
    assert board.get(Pos(1, 2)) == Color.RED
    # on the sides
    assert board.get(Pos(1, 0)) == Color.EMPTY
    assert board.get(Pos(1, 3)) == Color.EMPTY
    # above and below
    assert board.get(Pos(0, 1)) == Color.EMPTY
    assert board.get(Pos(0, 2)) == Color.EMPTY
    assert board.get(Pos(2, 1)) == Color.EMPTY
    assert board.get(Pos(2, 2)) == Color.EMPTY
    board.place_rug(Rug(RugPos(Pos(2, 2), Direction.UP), Color.BLUE))
    assert board.get(Pos(2, 2)) == Color.BLUE
    assert board.get(Pos(1, 2)) == Color.BLUE
    # on the sides
    assert board.get(Pos(1, 1)) == Color.RED
    assert board.get(Pos(2, 1)) == Color.EMPTY
    assert board.get(Pos(1, 3)) == Color.EMPTY
    assert board.get(Pos(2, 3)) == Color.EMPTY
    # above and below
    assert board.get(Pos(0, 2)) == Color.EMPTY
    assert board.get(Pos(3, 2)) == Color.EMPTY

    #Second board
    board = Board()

    pos = Pos(0,0)
    color = Color.BLUE
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(0,0)
    color = Color.BROWN
    dir = Direction.RIGHT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(0,4)
    color = Color.YELLOW
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)
    
    pos = Pos(2,2)
    color = Color.RED
    dir = Direction.RIGHT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(2,2)
    color = Color.BLUE
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(2,4)
    color = Color.RED
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(3,0)
    color = Color.YELLOW
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)
    
    pos = Pos(4,0)
    color = Color.BROWN
    dir = Direction.RIGHT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(4,4)
    color = Color.RED
    dir = Direction.DOWN
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(5,4)
    color = Color.YELLOW
    dir = Direction.RIGHT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(6,3)
    color = Color.RED
    dir = Direction.LEFT
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)

    pos = Pos(5,0)
    color = Color.BLUE
    dir = Direction.UP
    rugpos = RugPos(pos, dir)
    rug = Rug(rugpos, color)
    board.place_rug(rug)
    
    assert board.get(Pos(0, 0)) == Color.BROWN
    assert board.get(Pos(1, 1)) == Color.EMPTY
    assert board.get(Pos(0, 3)) == Color.EMPTY
    assert board.get(Pos(2, 2)) == Color.BLUE
    assert board.get(Pos(2, 3)) == Color.RED
    assert board.get(Pos(1, 4)) == Color.YELLOW
    assert board.get(Pos(6, 2)) == Color.RED
    assert board.get(Pos(5, 5)) == Color.YELLOW
    assert board.get(Pos(6, 0)) == Color.EMPTY
    assert board.get(Pos(4, 0)) == Color.BLUE
    assert board.get(Pos(5, 3)) == Color.EMPTY




    # assert board.get(Pos(1, 1)) == Color.RED
    # assert board.get(Pos(1, 2)) == Color.RED
    # # on the sides
    # assert board.get(Pos(1, 0)) == Color.EMPTY
    # assert board.get(Pos(1, 3)) == Color.EMPTY
    # # above and below
    # assert board.get(Pos(0, 1)) == Color.EMPTY
    # assert board.get(Pos(0, 2)) == Color.EMPTY
    # assert board.get(Pos(2, 1)) == Color.EMPTY
    # assert board.get(Pos(2, 2)) == Color.EMPTY
    # board.place_rug(Rug(RugPos(Pos(2, 2), Direction.UP), Color.BLUE))
    # assert board.get(Pos(2, 2)) == Color.BLUE
    # assert board.get(Pos(1, 2)) == Color.BLUE
    # # on the sides
    # assert board.get(Pos(1, 1)) == Color.RED
    # assert board.get(Pos(2, 1)) == Color.EMPTY
    # assert board.get(Pos(1, 3)) == Color.EMPTY
    # assert board.get(Pos(2, 3)) == Color.EMPTY
    # # above and below
    # assert board.get(Pos(0, 2)) == Color.EMPTY
    # assert board.get(Pos(3, 2)) == Color.EMPTY

def test_area():
    board= Board()
    board.fields[1][1]=Color.RED
    board.fields[1][2]=Color.RED
    board.fields[2][2]=Color.RED
    board.fields[2][3]=Color.RED
    board.fields[3][4]=Color.RED
    assert board.get_region_area(Pos(2,2))==4
    assert board.get_region_area(Pos(1,2))==4
    assert board.get_region_area(Pos(1,1))==4
    assert board.get_region_area(Pos(3,4))==1

def test_within_board():
    board = Board()
    assert board.within_board(Pos(0,0)) == True
    assert board.within_board(Pos(6,6)) == True
    assert board.within_board(Pos(6,0)) == True
    assert board.within_board(Pos(0,6)) == True
    assert board.within_board(Pos(-1,0)) == False
    assert board.within_board(Pos(0,7)) == False
    assert board.within_board(Pos(7,0)) == False
    assert board.within_board(Pos(0,-1)) == False

def test_get_region_area():
    board = Board()

    #   .OOOO..     sum 15
    #   .O.O.O.
    #   ..OOOO.
    #   ...OO..
    #   ...O...
    #   ...O...
    #   .......

    board.fields[0][1]=Color.RED
    board.fields[0][2]=Color.RED
    board.fields[0][3]=Color.RED
    board.fields[0][4]=Color.RED
    board.fields[1][1]=Color.RED
    board.fields[1][3]=Color.RED
    board.fields[1][5]=Color.RED
    board.fields[2][2]=Color.RED
    board.fields[2][3]=Color.RED
    board.fields[2][4]=Color.RED
    board.fields[2][5]=Color.RED
    board.fields[3][3]=Color.RED
    board.fields[3][4]=Color.RED
    board.fields[4][3]=Color.RED
    board.fields[5][3]=Color.RED
    assert board.get_region_area(Pos(2,2)) == 15
    assert board.get_region_area(Pos(1,1)) == 15
    assert board.get_region_area(Pos(3,4)) == 15


    board.fields[2][3]=Color.YELLOW

    #   .OOOO..     sum 6
    #   .O.O.O.
    #   ..O.OO.
    #   ...OO..     sum 7
    #   ...O...
    #   ...O...
    #   .......
    assert board.get_region_area(Pos(0,2)) == 6
    assert board.get_region_area(Pos(1,3)) == 6
    assert board.get_region_area(Pos(3,4)) == 7
    assert board.get_region_area(Pos(2,4)) == 7