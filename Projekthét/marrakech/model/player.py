from dataclasses import dataclass
from .color import Color
import random
@dataclass
class Player:
    color: Color
    money: int
    carpet_count: int
    name: str

    def pay_to(self, other: "Player", amount: int) -> None:
        """Pénz fizetése egy másik játékosnak

        Ha nincs elég pénze, akkor annyit fizet, amennyit tud.
        """
        if not isinstance(other, Player):
            raise TypeError("Nem megfelelő játékos")

        # eltároljuk a fizetendőt, és ha több, mint a saját pénzünk akkor a saját pénzünkre állítjuk
        realAmountToPay = amount
        if amount > self.money:
            realAmountToPay = self.money

        # átadjuk a pénzt a másik játékosnak 
        self.money -= realAmountToPay
        other.money += realAmountToPay


def create_players(player_data: list[str]) -> list[Player]:
    players = []
    carpet_count = 12 if len(player_data)== 4 else 15
    available_colors = [Color.RED, Color.BLUE, Color.BROWN, Color.YELLOW]
    random.shuffle(available_colors)
    for i in range(len(player_data)):
        # Létrehozunk egy Player objektumot és hozzáadjuk a players listához
        player = Player(name=player_data[i], color=available_colors[i], money=120 // len(player_data), carpet_count=carpet_count)
        players.append(player)
    
    return players