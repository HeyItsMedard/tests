from .board import Board
from .directions import Direction, RotationDirection
from .player import Player
from .position import Pos
from .rug import Rug, RugPos
from .balcony import Balcony, init_balconies
from .color import Color


class GameState:
    """A játék aktuális állapotát leíró osztály"""

    def __init__(self) -> None:
        """Inicializálja a játék kezdeti állapotát"""

        self.players = list[Player]()
        self._current_player_index = 0

        self.board = Board()

        self.balconies = init_balconies()

        self.figure_pos = Pos(3, 3)
        self.figure_dir = Direction.UP

        self.top_rugs = list[RugPos]()
        """A teljesen fedetlen szőnyegek pozíciói"""

        self.rugs = list[Rug]()
        """Az összes lerakott szőnyeg (csak a szebb megjelenítés végett)"""

    def add_players(self, players: list[Player]) -> None:
        """Segédfüggvény by Med"""
        self.players = players

    def current_player(self) -> Player:
        """Visszaadja a jelenlegi játékost"""
        return self.players[self._current_player_index]

    def next_player(self) -> None:
        """Átadja a kört a következő játékosnak"""
        self._current_player_index += 1
        self._current_player_index %= len(self.players)

    
    def turn_figure(self, direction: RotationDirection) -> None:
        """A figurát 90 fokkal elfordítja a megadott irányba"""
        if direction == RotationDirection.NONE:
            return
        self.figure_dir = Direction.rotate(self.figure_dir, direction)

    def _step_with_direction(self, pos: Pos, dir: Direction) -> Pos:
        newpos = pos.copy()
        match dir:
            case Direction.LEFT:
                newpos.col -= 1
            case Direction.RIGHT:
                newpos.col += 1    
            case Direction.UP:
                newpos.row -= 1
            case Direction.DOWN:
                newpos.row += 1     
        
        return newpos        


    def step_with_figure(self) -> None:
        """A figura egy mezőt lép a jelenlegi irányába

        Ha a figura lelépne a pályáról, az erkélyt követve visszatér a pályára egy
        szomszédos sorba, vagy a fordító saroknál a kiindulási mezőre, elfordulva.
        """
        oldpos = self.figure_pos.copy()
        newpos = self._step_with_direction(oldpos, self.figure_dir)

        
        if self.board.within_board(newpos): 
            self.figure_pos = newpos
            return
        else:
            # erkélyre léptünk 
            newdir = self.figure_dir.copy()
            # megnézzük melyik erkélyen állunk 
            for balcony in self.balconies:
                if newpos == balcony.pos_1 or newpos == balcony.pos_2:
                    newpos = balcony.other_pos(newpos)
                    newdir = balcony.newdirection(newpos)
                    newpos = self._step_with_direction(newpos, newdir)
                    break
            
            if self.board.within_board(newpos) and newdir != self.figure_dir:
                 # korrektül megtörtént a visszatérés
                self.figure_pos = newpos
                self.figure_dir = newdir
            else:
                # valamit rosszul számoltunk és nem tértünk vissza a játéktérre
                raise ValueError(f"{newpos.row=} {newpos.col=}")


    def move_figure(self, steps: int) -> None:
        """A figura `steps` lépést tesz a jelenlegi irányába

        Ha a figura egy ellenfél szőnyegén áll meg, az aktuális játékos a régió
        méretével megegyező pénzt fizet a tulajdonosnak.
        """
        # lemozogjuk a lépéseket  
        for i in range(steps):
            self.step_with_figure()

        actualcolor = self.board.fields[self.figure_pos.row][self.figure_pos.row]
        # ha nem a saját színünkre vagy üresre léptünk 
        if actualcolor != Color.EMPTY and actualcolor != self.current_player.color:
            for player in self.players:
                # megtaláltuk kinek a színére léptünk 
                if player.color == actualcolor:
                    # kifizetjük tartozás 
                    tartozas = self.board.get_region_area(self.figure_pos)
                    self.current_player.pay_to(player, tartozas)

    def get_valid_rug_places(self) -> list[RugPos]:
        """Visszaadja az összes olyan helyet, ahova szőnyeget lehet tenni

        A szőnyeg egyik mezőjének szomszédosnak kell lennie a figurával.
        Nem takarhat le teljesen egy fedetlen szőnyeget.
        """
        rotdirs = (RotationDirection.LEFT, RotationDirection.NONE, RotationDirection.RIGHT)
        validrugs = list[RugPos]()
        neighborlist = self.figure_pos.neighbors(self.board.rowcount(), self.board.colcount())
        
        # végig iteráljuk a valid szomszédokat
        for neighbor in neighborlist:
            dir = self.figure_pos.direction_to_other(neighbor)
            
            # végigiteráljuk a lehetséges elforgatásokat
            for rotdir in rotdirs:
                rugpos = RugPos(neighbor, dir.rotate(rotdir))           # szőnyeg pozíció
                rugastuple = rugpos.as_tuple()                          # koordinátái
                overlays = False
                if self.board.within_board(rugastuple[0]) and \
                   self.board.within_board(rugastuple[1]):              # mindkét koordináta elfér a táblán
                    for toprugpos in self.top_rugs:                     # átnézzük a teljesen fedetlen szőnyegeket
                        if rugpos.__eq__(toprugpos): 
                            overlays = True             # van átfedés! 
                            break
                    if overlays == False:
                        validrugs.append(rugpos)        # a szőnyeg elfér a táblán és nem volt teljes átfedés

        return validrugs

    def place_rug(self, pos: RugPos) -> None:
        """Az aktuális játékos lerak egy szőnyeget a megadott helyre"""
        rug = Rug(pos, self.current_player.color)
        self.current_player.carpet_count -= 1
        self.rugs.append(rug)
        self.board.place_rug(rug)
        
        # törölni kell a `top_rugs` lefedésre került szőnyegeit
        i = 0 
        while i < len(self.top_rugs):
            if pos.intersects(self.top_rugs[i]):
                self.top_rugs.pop(i)
            else: 
                i += 1

        self.top_rugs.append(pos)

    def is_game_over(self) -> bool:
        """Megadja, hogy vége van-e a játéknak

        A játék akkor ér véget, ha minden játékosnak elfogytak a szőnyegei."""
        rugCount = 0
        for player in self.players:
            rugCount += player.carpet_count

        if rugCount == 0: 
            return True

        return False

    def get_scoreboard(self) -> list[tuple[str, int]]:
        """Visszaadja a játékosok neveit és pontszámait helyezés szerinti sorrendben

        A pontszám a pénz és a fedetlen szőnyegfelület összege.
        Pontegyezés esetén a nagyobb szőnyegfelület számít jobb eredménynek.
        """
        scoreboard = list[tuple[str, int]]()
 
        for player in self.players:
            pontszam = self.board.get_color_count(player.color)
            pontszam += player.money
            scoreboard.append((player.name, pontszam))
 
        return scoreboard
