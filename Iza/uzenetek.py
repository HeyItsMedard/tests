from dataclasses import dataclass
from datetime import datetime
@dataclass
class Üzenet:
    
    id: int
    szoveg: str
    ido: datetime
    kuldo: str
    cimzett: str
    olvasott: bool
    def __repr__(self) -> str:
        return(f"{self.ido} KÜLDŐ: {self.kuldo}: {self.szoveg}")
    