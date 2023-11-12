from dataclasses import dataclass

from .color import Color
from .directions import Direction
from .position import Pos


@dataclass
class RugPos:
    """Egy szőnyeg pozícióját leíró osztály

    A `start` megadja az egyik felének a koordinátáit, a `direction` pedig azt, hogy a
    szőnyeg másik fele ettől milyen irányban van.
    """

    start: Pos
    direction: Direction

    def intersects(self, other: "RugPos") -> bool:
        """Megadja, hogy fedésben van-e egymással a két szőnyeg"""
        
        if not isinstance(other, RugPos):
            return False
        tup1 = self.as_tuple()
        tup2 = other.as_tuple()

        if  tup1[0] == tup2[0] or tup1[0] == tup2[1] or \
            tup1[1] == tup2[0] or tup1[1] == tup2[1]:
            return True
        else:
            return False

    def as_tuple(self) -> tuple[Pos, Pos]:
        """Visszaadja a szőnyeg két mezőjének koordinátáit"""
 
        second_pos = self.start.copy()
        match self.direction:
            case Direction.UP:
                second_pos.row -= 1
            case Direction.DOWN:
                second_pos.row += 1
            case Direction.LEFT:
                second_pos.col -= 1
            case Direction.RIGHT:
                second_pos.col += 1            

        return (self.start, second_pos)

    @staticmethod
    def from_tuple(positions: tuple[Pos, Pos]) -> "RugPos":
        """Létrehoz egy `RugPos` objektumot a két mező koordinátáiból

        Ha a két mező nem szomszédos, akkor `ValueError` kivételt dob.
        """
        rugDirection: Direction
        row_diff = positions[1].row - positions[0].row
        col_diff = positions[1].col - positions[0].col
        
        if abs(row_diff) + abs(col_diff) != 1:
            raise ValueError

        if row_diff != 0:
            if row_diff > 0: 
                rugDirection = Direction.DOWN
            else:
                rugDirection = Direction.UP
        else:
            if col_diff > 0:
                rugDirection = Direction.RIGHT
            else:
                rugDirection = Direction.LEFT
        
        return RugPos(positions[0], rugDirection)

    def __eq__(self, other: object) -> bool:
        """Két `RugPos` objektum akkor egyenlő, ha teljesen fedik egymást"""
        if not isinstance(other, RugPos):
            return False
        tup1 = self.as_tuple()
        tup2 = other.as_tuple()
        if tup1 == tup2:
            return True
        if tup1 == (tup2[1], tup2[0]):
            return True
        return False


@dataclass
class Rug:
    """Egy szőnyeg adatait leíró osztály"""

    pos: RugPos
    color: Color
