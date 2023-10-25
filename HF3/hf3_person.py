from dataclasses import dataclass, field
from datetime import date

"""Feladat:
Készíts egy Person dataclass-t, ami a következő attribútumokkal rendelkezik:
    Születési dátum
    Keresztnév
    Vezetéknév
    Középső név (nevek), default: ""
    Könyvek listája, default: []
Legyen két számított property-je:
    age: a személy hány éves (lenne) ma
    full_name: a személy teljes neve (kereszt + középső + vezeték, szóközzel elválasztva)
Legyen egy setter metódusa a full_name-nek, ami átállítja a keresztnevet, a középső neveket és a vezetéknevet.
(A keresztnév az első név, a vezetéknév az utolsó név, a középső nevek pedig a többi név.)
"""

@dataclass
class Person:
    dob: date
    first_name: str
    last_name: str
    middle_name: str = field(default= "")
    books: list[str] = field(default_factory=list)

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name: str) -> None:
        splitted_fn = name.split()
        self.first_name = splitted_fn[0]
        self.middle_name = " ".join(splitted_fn[1:-1])
        self.last_name = splitted_fn[:-1]

    @property
    def age(self, current_date=date.today()): 
        year = current_date.year - self.dob.year
        # print(f"{current_date.month} < {self.dob.month} or {self.dob.month} == {current_date.month} and {current_date.day} < {self.dob.day}")
        if current_date.month < self.dob.month or self.dob.month == current_date.month and current_date.day < self.dob.day:
            return year - 1
        else:
            return year
        
if __name__ == "__main__":
    grrm = Person(date(1948, 9, 20), "George", "Martin", "Raymond")
    print(grrm.full_name)  # George Raymond Martin
    print(grrm.age)  # 74 - vicces sztori, néztem miért rossz a kimenet. Tegnap volt a születésnapja... már 75 éves.
    grrm.books.append("Dying of the Light")
    print(grrm)
    # Person(dob=datetime.date(1948, 9, 20), first_name='George', last_name='Martin', middle_name='Raymond', books=['Dying of the Light'])

    grrm.full_name = "George Raymond Richard Martin"
    print(grrm.full_name)
    print(grrm.middle_name)  # Raymond Richard
    grrm.books.append("A Game of Thrones")
    print(grrm)
    # Person(dob=datetime.date(1948, 9, 20), first_name='George', last_name='Martin', middle_name='Raymond Richard', books=['Dying of the Light', 'A Game of Thrones'])

    tolkien = Person(date(1892, 1, 3), "John", "Tolkien", "Ronald Reuel")
    print(tolkien.full_name)  # John Ronald Reuel Tolkien
    print(tolkien)
    # Person(dob=datetime.date(1892, 1, 3), first_name='John', last_name='Tolkien', middle_name='Ronald Reuel', books=[])
