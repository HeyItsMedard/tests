
def print_kurzuseredmeny():
    """Bekéri a tárgy kódját és a félév nevét, majd kiírja a kurzus eredményeit.

    A kurzuseredményeket a következő formában írja ki:
    Tárgy neve: <tárgynév>
    Félév: <félév>
    Létszám: <létszám> fő
    Aláírást szerzett: <aláírás==1> fő
    Bukási arány: <százalék>%
    Átlag: <sum(érdemjegy)/létszám>
    Vizsgajegyek:
        <darab> elégtelen (1)
        <darab> elégséges (2)
        <darab> közepes (3)
        <darab> jó (4)
        <darab> jeles (5)
    """
    # TODO: tárgykód bekérése
    # ha nem található, akkor hibaüzenet és visszatérés
    print("Tárgykód nem található.")
    # TODO: félév bekérése
    # ha nem található, akkor hibaüzenet és visszatérés
    print("Félév nem található.")
    # TODO: kurzuseredmények beolvasása
    # ha az oszlopok nem megfelelőek, akkor hibaüzenet és visszatérés
    print("Hibás oszlopok a fájlban.")
    # TODO: kurzuseredmények kiszámítása
    # ha a létszám 0, akkor az átlag legyen 0.0
    # TODO: kurzuseredmények kiírása
