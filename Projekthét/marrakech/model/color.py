from enum import Enum

class Color(Enum):
    EMPTY = 0
    RED = 1
    BLUE = 2
    BROWN = 3
    YELLOW = 4

    def copy(self) -> "Color":
        return Color(self)
