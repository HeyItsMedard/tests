from .position import Pos
from .directions import Direction

class Balcony:
    pos_1: Pos
    pos_2: Pos

    def __init__(self, pos1: Pos, pos2: Pos):
        self.pos_1 = pos1.copy()
        self.pos_2 = pos2.copy()

    def newdirection(self, pos: Pos) -> Direction:
        if pos !=  self.pos_1 and  pos != self.pos_2:
            raise ValueError
        else:
            return back_to_board_direction(pos)

    def other_pos(self, pos: Pos) -> Pos:
        if pos == self.pos_1:
            return self.pos_2
        elif pos == self.pos_2:
            return self.pos_1
        else: raise ValueError 

def back_to_board_direction(pos: Pos) -> Direction:
    if pos.row < 0: 
        return Direction.DOWN
    elif pos.row > 6: 
        return Direction.UP    
    elif pos.col < 0:
        return Direction.RIGHT
    elif pos.col > 6:
        return Direction.LEFT
    else: raise ValueError


def init_balconies() -> list[Balcony]:
    blaconyList = list[Balcony]()
    blaconyList.append(Balcony(Pos(0, -1),Pos(1, -1)))    # before first column
    blaconyList.append(Balcony(Pos(2, -1),Pos(3, -1)))
    blaconyList.append(Balcony(Pos(4, -1),Pos(5, -1)))
    blaconyList.append(Balcony(Pos(6, -1),Pos(7, 0)))     # corner
    blaconyList.append(Balcony(Pos(7, 1),Pos(7, 2)))      # below last row
    blaconyList.append(Balcony(Pos(7, 3),Pos(7, 4)))
    blaconyList.append(Balcony(Pos(7, 5),Pos(7, 6)))
    blaconyList.append(Balcony(Pos(6, 7),Pos(5, 7)))      # after last column
    blaconyList.append(Balcony(Pos(4, 7),Pos(3, 7)))
    blaconyList.append(Balcony(Pos(2, 7),Pos(1, 7)))
    blaconyList.append(Balcony(Pos(0, 7),Pos(-1, 6)))     # corner
    blaconyList.append(Balcony(Pos(-1, 5),Pos(-1, 4)))    # above first column 
    blaconyList.append(Balcony(Pos(-1, 3),Pos(-1, 2)))
    blaconyList.append(Balcony(Pos(-1, 1),Pos(-1, 0)))    

    return blaconyList


# testing fillup 
"""
b = init_balconies()
for balc in b:
    print(balc.firstpos, balc.lastpos)
"""
