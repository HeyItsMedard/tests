from enum import Enum


class RotationDirection(Enum):
    LEFT = -1
    NONE = 0
    RIGHT = 1


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def copy(self) -> "Direction":
        return Direction(self.value)

    def rotate(self, direction: "RotationDirection") -> "Direction":
        """Visszaadja a megadott irányba elforgatott irányt"""
        return Direction((self.value + direction.value) % 4)
