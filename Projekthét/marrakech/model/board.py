from .color import Color
from .position import Pos
from .rug import Rug


class Board:
    def __init__(self) -> None:
        self.fields = [[Color.EMPTY for _ in range(7)] for _ in range(7)]
        """7x7 pálya, kezdetben teljesen üres"""

    def __repr__(self) -> str:
        return "\n".join(map(str, self.fields))

    def get(self, pos: Pos) -> Color:
        return self.fields[pos.row][pos.col]

    def _set(self, pos: Pos, color: Color) -> None:
        self.fields[pos.row][pos.col] = color

    def place_rug(self, rug: Rug) -> None:
        for pos in rug.pos.as_tuple():
            if self.within_board(pos) == False:
                raise ValueError
            self._set(pos, rug.color)

    def get_region_area(self, pos: Pos) -> int:
        """Visszaadja a megadott pozíciót lefedő szőnyegrégió méretét

        A régió az azonos színű szőnyegek összefüggő területe.
        Ha a megadott mező üres, akkor 0-t ad vissza.
        """
        """
        Elvi vázlat: 
        1. A paraméterben kapott pozíciót betesszük a vizsgálandó pozíciók listájába
        2. Addig vizsgáljuk a jó szomszédok listáját, amíg a végére érünk 
            Lekérjük a pályán lehetséges közvetlen szomszédait
            A végigiteráljuk a szomszédokat:
                - ha jó a színe 
                - ha nem szerepel a jószomszéd listában
                akkor felvesszük a lista végére
            Tovább iteráljuk a listát
         """
        
        goodcolor = self.get(pos)                   # ez lesz a jó szín 
        if goodcolor == Color.EMPTY: return 0       # ha nincs szín, kilépünk 
        area = list[Pos]()                                   # az összetartozó jó színű koordináták
        area.append(pos)                            # inicializálás

        i = 0
        while i < len(area): 
            neighborlist = area[i].neighbors(self.rowcount(), self.colcount())
            for neighbor in neighborlist:
                if self.get(neighbor) == goodcolor and neighbor not in list(area):  
                        area.append(neighbor)
            i += 1 
        
        return len(area)
    
    def get_color_count(self, color: Color) -> int:
        """
        Megszámolja hogy az adott színből mennyi szerepel a táblán
        végig iterálva annak sorait és oszlopait
        """
        count = 0 
        for row in range(self.rowcount()):
            for col in range(self.colcount()):
                if self.fields[row][col] == color: count += 1

        return count
    
    def within_board(self, pos: Pos) -> bool:
        if pos.row in range(self.rowcount()) and pos.col in range(self.colcount()):
            return True
        else:
            return False
    
    def rowcount(self) -> int:
        return len(self.fields)
    
    def colcount(self) -> int:
        rows = self.rowcount
        if rows == 0: 
            return 0      
        else:
            return len(self.fields[0])       # feltételezzük, mindegyik sor ugyanolyan hosszú
    
