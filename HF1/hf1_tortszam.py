"""
Implementáld az alábbi osztályt a példakódnak megfelelően!
"""


class Tortszam:
    def __init__(self, szamlalo, nevezo):
        self.szamlalo = szamlalo
        self.nevezo = nevezo

    def __str__(self) -> str:
        self._egyszerusit()  
        return f'{self.szamlalo}/{self.nevezo}'
    
    def __repr__(self):
        self._egyszerusit()
        return f'{self.szamlalo}/{self.nevezo}'

    def ertek(self):
        return self.szamlalo / self.nevezo

    def szorozva(self, masik: "Tortszam") -> "Tortszam": #v 3.10.8-ban csak sztringként tudja kezelni a classt
        eredmeny = Tortszam(self.szamlalo * masik.szamlalo, self.nevezo * masik.nevezo)
        eredmeny._egyszerusit()
        return eredmeny
        # return Tortszam(self.szamlalo * masik.szamlalo, self.nevezo * masik.nevezo)
    
    #def __mul__(self, other):

    def beszoroz(self, masik: "Tortszam"):
        self.szamlalo *= masik.szamlalo
        self.nevezo *= masik.nevezo
        self._egyszerusit()

    def reciproka(self):
        eredmeny = Tortszam(self.nevezo, self.szamlalo)
        eredmeny._egyszerusit()
        return eredmeny

    def __lt__(self, masik) -> bool:  
        return self.ertek() < masik.ertek()

    def _egyszerusit(self):
        gcd = self._gcd(self.szamlalo, self.nevezo)
        self.szamlalo //= gcd
        self.nevezo //= gcd

    def plusz(self, masik: "Tortszam") -> "Tortszam":
        uj_szamlalo = self.szamlalo * masik.nevezo + masik.szamlalo * self.nevezo
        uj_nevezo = self.nevezo * masik.nevezo
        eredmeny = Tortszam(uj_szamlalo, uj_nevezo)
        eredmeny._egyszerusit()
        return eredmeny

    def hozzaad(self, masik: "Tortszam"):
        uj_szamlalo = self.szamlalo * masik.nevezo + masik.szamlalo * self.nevezo
        uj_nevezo = self.nevezo * masik.nevezo
        self.szamlalo = uj_szamlalo
        self.nevezo = uj_nevezo
        self._egyszerusit()

    @staticmethod
    def _gcd(a, b): #euklidesz
        while b:
            a, b = b, a % b
        return a

if __name__ == "__main__":
    fel = Tortszam(1, 2)
    print("fel: ", fel) # Ki: 1/2
    print("fel: ", fel.ertek())  # Ki: 0.5
    negyed = fel.szorozva(fel)  # nem változtatja az objektumot
    print("negyed: ", negyed)  # Ki: 1/4
    print("fel: ", fel)  # Ki: 1/2

    tort = negyed.szorozva(Tortszam(3, 1))
    print("tort1: ", tort)  # Ki: 3/4
    tort.beszoroz(fel)  # megváltoztatja az objektumot
    print("tort2: ", tort)  # Ki: 3/8
    print("tort: ", tort.ertek())  # Ki: 0.375

    # # A törtek mindig legyenek egyszerusitett alakban!
    # # Ehhez érdemes egy _egyszerusit() privát metódust definiálni
    print(tort.plusz(Tortszam(1, 8)))  # Ki: 1/2
    tort.hozzaad(Tortszam(1, 8))  # megváltoztatja az objektumot
    print("tort ertek megint:", tort.ertek())  # Ki: 0.5

    rec = tort.reciproka()  # nem változtatja az objektumot
    print(rec)  # Ki: 2/1
    
    # # Összehasonlítás
    print(f"{tort.szorozva(rec)} == {Tortszam(1, 1)}")  # Ki: 1/1 == 1/1
    print(tort.szorozva(rec) == Tortszam(1, 1))  # Ki: True (False???)
    print(tort < rec)  # Ki: True
    print(rec < tort)  # Ki: False
    
    tortek = [Tortszam(1, 2), Tortszam(1, 3), Tortszam(1, 4), Tortszam(2, 3), Tortszam(2, 4)]
    tortek.sort()
    print(tortek)  # Ki: [1/4, 1/3, 1/2, 1/2, 2/3]
