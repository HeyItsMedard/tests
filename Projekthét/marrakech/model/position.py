from dataclasses import dataclass
from .directions import Direction


@dataclass
class Pos:
    """A pálya egy mezőjének koordinátái

    A bal felső sarok koordinátái (0, 0)
    """

    row: int
    col: int
    def copy(self) -> "Pos":
        return Pos(self.row, self.col)

    def as_tuple(self) -> tuple[int, int]:
        return (self.row, self.col)

    def distance(self, other: "Pos") -> int:
        """Megadja a két mező Manhattan-távolságát"""
        return abs(self.row - other.row) + abs(self.col - other.col)

    def neighbors(self, rowcount: int, colcount: int) -> list["Pos"]:
        """Megadja a mező érvényes szomszédait a 7x7-es pályán"""
        neighborList = [] 
        if self.row + 1 in range (rowcount):
            neighborList.append(Pos(self.row +1, self.col)) 
        if self.row - 1 in range (rowcount):
            neighborList.append(Pos(self.row -1, self.col)) 
        if self.col + 1 in range (colcount):
            neighborList.append(Pos(self.row, self.col + 1)) 
        if self.col - 1 in range (colcount):
            neighborList.append(Pos(self.row, self.col - 1)) 

        return neighborList
    
    def direction_to_other(self, other: "Pos") -> Direction:
        if self.distance(other) != 1 :
            raise ValueError
        
        dir: Direction
        if self.col > other.col: 
            dir = Direction.LEFT
        elif self.col < other.col:
            dir = Direction.RIGHT
        elif self.row > other.row: 
            dir = Direction.UP
        elif self.row < other.row:
            dir = Direction.DOWN

        return dir


