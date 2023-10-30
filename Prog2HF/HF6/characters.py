from abc import ABC, abstractmethod
import random

DIRECTIONS = "WASD"

class Character(ABC):
    def __init__(self, row: int, col: int) -> None:
        self._row = row
        self._col = col

    def move(self, row: int, col: int) -> None:
        self._row = row
        self._col = col

    def get_adjacent_cell(self, direction: str) -> tuple[int, int]:
        if direction == "W":
            return self._row - 1, self._col
        if direction == "S":
            return self._row + 1, self._col
        if direction == "A":
            return self._row, self._col - 1
        if direction == "D":
            return self._row, self._col + 1
        raise ValueError(f"Unknown direction: {direction}")

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    @abstractmethod
    def __str__(self) -> str:
        ...

class Monster(Character):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.direction = random.choice(DIRECTIONS)
        self.appearance = "⏫"

    def move(self, row: int, col: int) -> None:
        # Egy érték szerint fog irányt váltani
        self.direction = random.choice(DIRECTIONS) if random.random() < 0.2 else self.direction
        if self.direction == "W":
            self.appearance = "⏫"
        elif self.direction == "S":
            self.appearance = "⏬"
        elif self.direction == "A":
            self.appearance = "⏪"
        elif self.direction == "D":
            self.appearance = "⏩"
        super().move(row, col)

    def __str__(self) -> str:
        return self.appearance

class Player(Character):
    def __str__(self) -> str:
        return "🧙"
