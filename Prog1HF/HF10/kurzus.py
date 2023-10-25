import os
import csv
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
    # tárgykód bekérése
    targykod = input("Kérjük, adja meg a tárgy kódját: ").upper()
    if not os.path.isdir(f"/workspaces/prog1-23t-hf10-HeyItsMedard/targyak/{targykod}/"):
        print("Tárgykód nem található.")
        return
    # félév bekérése
    szemeszter = input("Kérjük, adja meg a félévet: ")
    path_felev = f"/workspaces/prog1-23t-hf10-HeyItsMedard/targyak/{targykod}/{szemeszter}.csv"
    jegyek, hallgatok, alairasok, bukasok  = 0, 0, 0, 0
    lista_jegyek = [0] * 5

    if os.path.isfile(path_felev):
        try:
            with open(path_felev, 'r') as db:
                # kurzuseredmények beolvasása
                readdb = csv.DictReader(db, delimiter=';') #ötlet: stackoverflow
                for column in readdb: #nyilván sorokat néz, viszont egy oszlopban található elemek kellenek
                    try:
                        #kurzuseredmények kiszámítása
                        if column['aláírás'] == '1':
                            if int(column['érdemjegy']) > 1:
                                jegyek += int(column['érdemjegy'])
                                alairasok += 1
                                hallgatok += 1
                                lista_jegyek[int(column['érdemjegy'])-1] += 1
                            else:
                                alairasok += 1
                                jegyek += 1
                                hallgatok += 1
                                lista_jegyek[0] += 1
                                bukasok += 1
                        elif column['aláírás'] == '0': #nem kapott aláírást - felvette a tárgyat de nem jut vizsgáig(?)
                                hallgatok += 1
                                lista_jegyek[0] += 1
                    except ValueError:
                        # ha az oszlopok nem megfelelőek, akkor hibaüzenet és visszatérés - visszatérés? ("-" és üres értékek)
                        print("Hibás oszlopok a fájlban.")
                        bukas += 1
                        lista_jegyek[0] += 1
        # ha nem található, akkor hibaüzenet és visszatérés
        except FileNotFoundError:
            print("Félév nem található.")
            return
    
    atlag = 0
    # ha a létszám 0, akkor az átlag legyen 0.0
    if hallgatok == 0:
        atlag = 0.0
    else:
        atlag = float(jegyek/hallgatok)
    
    # kurzuseredmények kiírása
    print(f"""
    Tárgy neve: {targykod}
    Félév: {szemeszter}
    Létszám: {hallgatok} fő
    Aláírást szerzett: {alairasok} fő
    Bukási arány: {float(bukasok/hallgatok)*100}%
    Átlag: {atlag}
    Vizsgajegyek:
        {lista_jegyek[0]} elégtelen (1)
        {lista_jegyek[1]} elégséges (2)
        {lista_jegyek[2]} közepes (3)
        {lista_jegyek[3]} jó (4)
        {lista_jegyek[4]} jeles (5)
    """)
print_kurzuseredmeny()