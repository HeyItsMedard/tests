from marrakech.model.game_state import GameState
from marrakech.model.position import Pos
from marrakech.model.directions import Direction
from marrakech.model.rug import RugPos, Rug
from marrakech.model.player import Player
from marrakech.model.color import Color


def test_step_with_firure():
    state =  GameState()
    
    # corner top right
    state.figure_pos = Pos(0,6)
    state.figure_dir = Direction.UP
    state.step_with_figure()
    assert state.figure_pos.row == 0 and state.figure_pos.col == 6 and state.figure_dir == Direction.LEFT

    state.figure_pos = Pos(0,6)
    state.figure_dir = Direction.RIGHT
    state.step_with_figure()
    assert state.figure_pos.row == 0 and state.figure_pos.col == 6 and state.figure_dir == Direction.DOWN

    # corner bottom left
    state.figure_pos = Pos(6,0)
    state.figure_dir = Direction.DOWN
    state.step_with_figure()
    assert state.figure_pos.row == 6 and state.figure_pos.col == 0 and state.figure_dir == Direction.RIGHT

    state.figure_pos = Pos(6,0)
    state.figure_dir = Direction.LEFT
    state.step_with_figure()
    assert state.figure_pos.row == 6 and state.figure_pos.col == 0 and state.figure_dir == Direction.UP

    #Edge of the board
    state.figure_pos = Pos(2,6)
    state.figure_dir = Direction.RIGHT
    state.step_with_figure()
    assert state.figure_pos.row == 1 and state.figure_pos.col == 6 and state.figure_dir == Direction.LEFT

    state.figure_pos = Pos(6,3)
    state.figure_dir = Direction.DOWN
    state.step_with_figure()
    assert state.figure_pos.row == 6 and state.figure_pos.col == 4 and state.figure_dir == Direction.UP

    state.figure_pos = Pos(3,0)
    state.figure_dir = Direction.LEFT
    state.step_with_figure()
    assert state.figure_pos.row == 2 and state.figure_pos.col == 0 and state.figure_dir == Direction.RIGHT

    state.figure_pos = Pos(0,2)
    state.figure_dir = Direction.UP
    state.step_with_figure()
    assert state.figure_pos.row == 0 and state.figure_pos.col == 3 and state.figure_dir == Direction.DOWN


    state.step_with_figure()    
    state.step_with_figure()    
    state.step_with_figure()

def test_place_rug():
    state = GameState()

    state.figure_pos = Pos(2,1)

    players = []
    players.append(Player(Color(Color.RED), 40, 15, "Aladár"))
    players.append(Player(Color(Color.YELLOW), 40, 15, "Béla"))
    state.add_players(players)

    # placing two rugs with actual player 
    color1 = state.current_player().color.copy()
    state.place_rug(RugPos(Pos(1,1), Direction.UP))         # 1,1  0,1
    state.place_rug(RugPos(Pos(0,2), Direction.RIGHT))      # 0,2  0,3
    found = False

    # should be in top rugs list now
    for rugpos in state.top_rugs:
        if rugpos == RugPos(Pos(2,0), Direction.RIGHT):
            found = True
    assert found == True

    state.next_player()

    color2 = state.current_player().color.copy()
    state.place_rug(RugPos(Pos(1,3), Direction.UP))         # 1,3  0,3

    # should not be in top rugs by now 
    found = False
    for rugpos in state.top_rugs:
        if rugpos == RugPos(Pos(0,2), Direction.RIGHT):
            found = True
    assert found == False


def test_get_valid_rugplaces():
    state = GameState()

    state.figure_pos = Pos(1,2)
    
    players = []
    players.append(Player(Color(Color.RED), 40, 15, "Aladár"))
    players.append(Player(Color(Color.YELLOW), 40, 15, "Béla"))
    state.add_players(players)

    # placing two rugs with actual player 
    color1 = state.current_player().color.copy()
    state.place_rug(RugPos(Pos(1,1), Direction.UP))         # 1,1  0,1
    state.place_rug(RugPos(Pos(1,3), Direction.UP))         # 1,3  0,3

    valirdrugs = []
    state.next_player()
    valirdrugs = state.get_valid_rug_places()

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(0,2), Direction.RIGHT)):
            found = True
    assert found == True                                    # should be a valid rug

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(1,3), Direction.UP)):
            found = True
    assert found == False                                    # should not be a valid rug

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(0,1), Direction.DOWN)):
            found = True
    assert found == False                                    # should not be a valid rug


    color2 = state.current_player().color.copy()
    state.place_rug(RugPos(Pos(0,2), Direction.RIGHT))      # 0,2  0,3

    valirdrugs = state.get_valid_rug_places()

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(0,2), Direction.RIGHT)):
            found = True
    assert found == False                                    # should not be a valid: rug full carpet there

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(0,2), Direction.UP)):
            found = True
    assert found == False                                    # should not be a valid: rug goes off table

    found = False
    for validrug in valirdrugs:
        if validrug.__eq__(RugPos(Pos(1,3), Direction.UP)):
            found = True
    assert found == True                                    # should be a valid rug: half covered pieces

