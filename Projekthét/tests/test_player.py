import pytest
from marrakech.model.player import Player, create_players
from marrakech.model.color import Color

def test_create_players():
    playerlist: []
    playerlist = create_players(("Akos","Lóri","Attila","Ádi"))
    assert playerlist[0].carpet_count == 12
    for player in playerlist:
         assert player.money == 30


    szin_count= 4*[0]
    for i in range(len(playerlist)):
         szin= playerlist[i].color
         match szin:
            case Color.RED:
                szin_count[0]+=1
            case Color.BLUE:
                 szin_count[1]+=1
            case Color.YELLOW:
                szin_count[2]+=1
            case Color.BROWN:
                 szin_count[3]+=1
    for i in szin_count:
        assert szin_count[i] == 1 or szin_count[i] == 0
       



            # def pay_to(self, other: "Player", amount: int) -> None:
    #    """Pénz fizetése egy másik játékosnak

    #    Ha nincs elég pénze, akkor annyit fizet, amennyit tud.
    #    """
            # if not isinstance(other, Player):
                # raise TypeError("Nem megfelelő játékos")

        # eltároljuk a fizetendőt, és ha több, mint a saját pénzünk akkor a saját pénzünkre állítjuk
        # realAmountToPay = amount
        # if amount > self.money:
        #    realAmountToPay = self.money

        # átadjuk a pénzt a másik játékosnak 
        # self.money -= realAmountToPay
        # other.money += realAmountToPay

def test_pay_to():
    playerlist: []
    playerlist = create_players(("Akos","Lóri","Attila","Ádi"))
    playerlist[0].pay_to(playerlist[1],8)
    playerlist[1].pay_to(playerlist[2],15)
    playerlist[0].pay_to(playerlist[3],25)
    assert playerlist[0].money==0
    assert playerlist[1].money==23
    assert playerlist[2].money==45
    assert playerlist[3].money==52
    allmoney=0
    for i in range(len(playerlist)):
        allmoney += playerlist[i].money
    assert allmoney==120




                 

