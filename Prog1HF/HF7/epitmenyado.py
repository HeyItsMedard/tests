# 1. feladat
"""Olvassa be és tárolja el az utca.txt állományban talált adatokat!

A fájl első sorában a három adósávhoz tartozó négyzetméterenként fizetendő összeg
található A, B, C sorrendben, egy-egy szóközzel elválasztva.

A többi sorban egy-egy építmény adatai szerepelnek egy-egy szóközzel elválasztva.
Az első a telek tulajdonosának ötjegyű adószáma; egy tulajdonosnak több telke is lehet.
A második adat az utca neve, amely nem tartalmazhat szóközt.
A harmadik adat a házszám, majd az adósáv megnevezése, végül az építmény alapterülete.
"""
from string import ascii_uppercase as abc
def beolvas(filename):
    with open("utca.txt") as f:
        first_line = f.readline()
        tax = {abc[kulcs]: int(ertek) for kulcs, ertek in enumerate(first_line.split())}
        data = f.readlines()
        #kulcs: adoszam, ertek: lakas adatai - comprehension túl hosszú
        tulajok = dict[str, list[dict[str, str | int]]]()
        for line in data:
            oszlopok = ['utca', 'hsz', 'sav', 'terulet']
            adatok = (line.split())
            adoszam = adatok[0]
            telek = {oszlopok[idx]: ertekek for idx, ertekek in enumerate(adatok[1:])}
            telek['terulet'] = int(telek['terulet'])
            if adoszam not in tulajok:
                tulajok[adoszam] = []
            tulajok[adoszam].append(telek)
    return tax, tulajok
tax, tulajok = beolvas("utca.txt")
#print(tulajok)
# 2. feladat
def kiir_telekszam():
    """Hány telek adatai találhatók az állományban?
    Az eredményt írassa ki a mintának megfelelően a képernyőre!

    >>> kiir_telekszam()
    2. feladat. A mintában 543 telek szerepel.
    """
    print(f"2. feladat. A mintában {sum(len(telkek) for telkek in tulajok.values())} telek szerepel.")

# 3. feladat
def kiir_tulaj_epuletei(tulaj_adoszam: str):
    """Írassa ki a mintához hasonlóan, hogy melyik utcában, milyen házszám alatt van
    építménye!
    Ha a megadott azonosító nem szerepel az adatállományban, akkor írassa ki a „Nem
    szerepel az adatállományban.” hibaüzenetet!

    >>> kiir_tulaj_epuletei("68396")
    Harmat utca 22
    Szepesi utca 17
    """
    found = False
    for key, val in tulajok.items():
        if tulaj_adoszam in key:
            for haz in val:
                print(haz['utca'], "utca", haz['hsz'])
            found = True
    if not found:
        print("Nem szerepel az adatállományban.")

# 4. feladat
def ado(adosav: str, alapterulet: int) -> int:
    """Meghatározza egy adott építmény után fizetendő adót.

    Args:
        adosav (str): "A", "B" vagy "C" adósáv
        alapterulet (int): Az építmény alapterülete [m^2]

    Returns:
        int: Az építmény után fizetendő adó [Ft]

    Az A sávba azok a telkek kerültek, amelyek 300 méternél közelebb vannak a tóhoz.
    A B sáv az előzőn túl 600 méter távolságig terjed, a többi telek a C sávba tartozik.
    Az építmény után négyzetméterenként fizetendő összeg sávonként eltérő, azonban,
    ha az így kiszámított összeg nem éri el a 10.000 Ft-ot, akkor az adott építmény után
    nem kell adót fizetni.
    """
    calc = 0
    if adosav in tax:
        calc = tax[adosav] * alapterulet
        if calc > 10000:
            return int(calc)
        else:
            return int(0)

# 5. feladat
def kiir_savonkenti_osszesites():
    """Határozza meg, hogy hány építmény esik az egyes adósávokba, és mennyi az adó
    összege adósávonként!
    Az eredményt a mintának megfelelően írassa ki a képernyőre!

    >>> kiir_savonkenti_osszesites()
    5. feladat
    A sávba 165 telek esik, az adó 20805600 Ft.
    B sávba 144 telek esik, az adó 13107000 Ft.
    C sávba 234 telek esik, az adó 3479600 Ft.
    """
    #akár külön dict{sav: val, db: val, ado: val}
    print("5. feladat")
    for key in tax.keys():
        count = 0
        sumado = 0
        for kulcs in tulajok:
            for adatok in tulajok[kulcs]:
                if adatok['sav'] == key:
                    count += 1
                    ter = adatok['terulet']
                    sumado += (ado(key, ter))
        print(f"{key} sávba {count} telek esik, az adó {sumado} Ft.")

    #telek = {kulcsok[idx]: ertekek for idx, ertekek in enumerate(tulajok[1:])}
    


# 6. feladat
def kiir_heterogen_utcak():
    """Bár az utcák többé-kevésbé párhuzamosak a tó partjával, az egyes porták távolsága
    a parttól az utcában nem feltétlenül ugyanannyi. Emiatt néhány utcában - az ottani
    tulajdonosok felháborodására - egyes telkek eltérő sávba esnek.
    Listázza ki a képernyőre, hogy melyek azok az utcák, ahol a telkek sávokba sorolását
    emiatt felül kell vizsgálni!
    Feltételezheti, hogy minden utcában van legalább két telek.

    >>> kiir_heterogen_utcak()
    6. feladat. A több sávba sorolt utcák:
    Besztercei
    Gyurgyalag
    Icce
    Kurta
    Rezeda
    Szepesi
    """
    print("6. feladat. A több sávba sorolt utcák:")
    utcak = {}
    for values in tulajok.values():
        for value in values:
            if value["utca"] not in utcak:
                utcak[value["utca"]] = value["sav"]
            elif value["utca"] in utcak and utcak[value["utca"]] != value["sav"]:
                utcak[value["utca"]] += value["sav"]
    for key, value in utcak.items():
        if len(value) >= 2:
            print(key)


# 7. feladat
def export_fizetendo_adok(output_filename: str):
    r"""Határozza meg a fizetendő adót tulajdonosonként!
    A tulajdonos adószámát és a fizetendő összeget írassa ki a mintának megfelelően a
    paraméterben megadott nevű állományba!
    A fájlban minden tulajdonos adatai új sorban szerepeljenek, a tulajdonos adószámát
    egy szóközzel elválasztva kövesse az általa fizetendő adó teljes összege.

    Args:
        output_filename (str): A kimeneti fájl elérési útja

    >>> export_fizetendo_adok("fizetendo.txt")
    >>> result = open("fizetendo.txt").readlines()
    >>> len(result)
    519
    >>> result[:3]
    ['38522 18000\n', '86379 0\n', '79906 12300\n']
    """
    with open(output_filename, 'w') as f:
        for key, val in tulajok.items(): 
            sumtax = 0   
            for item in val:
                sumtax += ado(item['sav'], item['terulet'])
            f.write(f"{key} {sumtax}\n")

if __name__ == "__main__":
    kiir_telekszam()
    kiir_tulaj_epuletei(input("3. feladat. Egy tulajdonos adószáma: "))
    kiir_savonkenti_osszesites()
    kiir_heterogen_utcak()
    export_fizetendo_adok("fizetendo.txt")
