


class Felhasznalo:
    def __init__(self, felhasznalo, jelszo, nev):
        self.felhasznalo = felhasznalo
        self.jelszo = jelszo
        self.nev = nev
        self.uzenetek = []
    def __repr__(self) -> str:
        return(f"{self.felhasznalo},{self.jelszo},{self.nev},{self.uzenetek}")