import random
import text_view
from characters import Character, Monster, Player, DIRECTIONS
import os

class Board:
    def __init__(self, size: int) -> None:
        self._size = size
        self._cells: list[list[Character | None]] = [[None] * size for _ in range(size)]
        self._player: Player | None = Player(0, 0)
        self._cells[0][0] = self._player
        self._monsters = list[Monster]()
        
        while len(self._monsters) < size:
            row = random.randrange(size)
            col = random.randrange(size)
            if row < size // 2 and col < size // 2:
                # no monsters spawn in the upper left quadrant
                continue
            if not self._cells[row][col]:
                monster = Monster(row, col)
                self._cells[row][col] = monster
                self._monsters.append(monster)

    def get_cells(self) -> list[list[Character | None]]:
        return self._cells

    def move_player(self, direction: str) -> None:
        if self._player is None:
            return
        direction = direction.upper()
        if direction not in DIRECTIONS:
            if direction == 'Q':
                self.end_game()
            return
        row, col = self._player.get_adjacent_cell(direction)
        if not (0 <= row < self._size and 0 <= col < self._size):
            return
        self._cells[self._player.row][self._player.col] = None
        if self._cells[row][col] is not None:
            self.end_game()
            return
        self._player.move(row, col)
        self._cells[row][col] = self._player

    def is_game_won(self) -> bool:
        return self._player is not None and self._cells[-1][-1] == self._player

    def is_game_over(self) -> bool:
        return self._player is None or self.is_game_won()

    def end_game(self) -> None:
        self._player = None

    def move_monsters(self) -> None:
        for monster in self._monsters:
            row, col = monster.get_adjacent_cell(monster.direction)
            if not (0 <= row < self._size and 0 <= col < self._size):
                monster.direction = random.choice(DIRECTIONS)
                continue
            if self._cells[row][col] is not None:
                if isinstance(self._cells[row][col], Player):
                    self.end_game()
                else:
                    monster.direction = random.choice(DIRECTIONS)
                continue
            self._cells[monster.row][monster.col] = None
            monster.move(row, col)
            self._cells[row][col] = monster
    
    def update_leaderboard(self, player_name: str, play_time: int) -> list[tuple[str, float]]:
        leaderboard_file = "leaderboard.txt"

        try:
            with open(leaderboard_file, "r") as file:
                leaderboard = [line.strip().split(" - ") for line in file]
        except FileNotFoundError:
            leaderboard = []

        # Rendezzük a ranglistát és tartsuk meg az elért időt ha a legjobb 10-ben van
        leaderboard.append((player_name, play_time))

        leaderboard.sort(key=lambda entry: float(entry[1]))

        leaderboard = leaderboard[:10]

        with open(leaderboard_file, "w") as file:
            for entry in leaderboard:
                file.write(f"{entry[0]} - {entry[1]}\n")

        return leaderboard
    
    def win_animation(self):
        for row in range(self._size):
            for col in range(self._size):
                if isinstance(self._cells[row][col], Monster):
                    self._cells[row][col].appearance = "💀"  
        self.print_updated_board()
    
    def lose_animation(self):
        for row in range(self._size):
            for col in range(self._size):
                self._cells[row][col] = "👹"  # A pálya többi területét is ogre karakterekkel töltjük fel
                    
        # Frissítjük a játéktáblát
        self.print_updated_board()

    def print_updated_board(self): # winnek és lossnak
        os.system("cls" if os.name == "nt" else "clear")
        print(text_view.render(self._cells))