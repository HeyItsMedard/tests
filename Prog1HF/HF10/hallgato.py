import os
import json
import csv

def _load_hallgato(neptun: str) -> dict:
    """Beolvassa és visszaadja egy hallgató adatait.

    Ha a megadott azonosító nem található, AttributeError-t dob.

    Args:
        neptun (str): a hallgató Neptun-azonosítója

    Returns:
        dict: a hallgató adatait tartalmazó szótár
    """
    path = '/workspaces/prog1-23t-hf10-HeyItsMedard/hallgatok'
    name = f'{neptun}.json'
    getfile = os.path.join(path, name)

    if os.path.isfile(getfile):
        with open(getfile, 'r') as db:
            json_data = json.load(db)
            return json_data
    else:
        raise AttributeError("Ez a Neptun-kód nem található.")


def _get_felev_str(start: str, index: int) -> str:
    """Segédfüggvény a félév nevének meghatározásához.

    A félévek elnevezése a következő rendszert követi:
    2021_tavasz
    2021_osz
    2022_tavasz
    2022_osz
    2023_tavasz
    ...

    Args:
        start (str): a referencia félév neve
        index (int): a keresett félév indexe

    Returns:
        str: a keresett félév neve
    """
    match start.split("_"):
        case [ev, "tavasz"]:
            return f"{int(ev) + index // 2}_" + ["tavasz", "osz"][index % 2]
        case [ev, "osz"]:
            return f"{int(ev) + (index + 1) // 2}_" + ["osz", "tavasz"][index % 2]


def _get_felev_index(start: str, felev: str) -> int:
    """Segédfüggvény a félév indexének meghatározásához.

    A félévek elnevezése a következő rendszert követi:
    2021_tavasz
    2021_osz
    2022_tavasz
    2022_osz
    2023_tavasz
    ...

    Args:
        start (str): a referencia félév neve
        felev (str): a keresett félév neve

    Returns:
        int: a keresett félév indexe

    >>> _get_felev_index("2021_tavasz", "2021_osz")
    1
    >>> _get_felev_index("2021_tavasz", "2022_tavasz")
    2
    """
    index = 0
    
    kezdev, kezdevszak = start.split("_")
    kerev, kerevszak = felev.split("_")
    ev_diff = abs(int(kerev) - int(kezdev)) * 2
    if kezdevszak != kerevszak:
        index = 1
    return index + ev_diff


def _get_kurzus_eredmeny(hallgato: str, targy: str, felev: str) -> int:
    """Lekérdezi egy hallgató eredményét egy tárgy adott félévéből.

    Az eredmények a `targyak/[targy]/[felev].csv` fájlokban találhatóak.
    Ha az aláírás oszlopban nem 1-es van, akkor a hallgató nem teljesítette a tárgyat.

    Args:
        hallgato (str): a hallgató Neptun-azonosítója
        targy (str): a keresett tárgy kódja
        felev (str): a keresett félév neve

    Returns:
        int: a kurzus eredménye, vagy 0, ha a hallgató nem teljesítette a tárgyat

    Raises:
        FileNotFoundError: ha a fájl nem található
        AttributeError: ha a hallgató nem található a fájlban
    """
    path_eredmeny = f'/workspaces/prog1-23t-hf10-HeyItsMedard/targyak/{targy}/{felev}.csv'
    #print(path_eredmeny)

    if os.path.isfile(path_eredmeny):
        with open(path_eredmeny, 'r') as db:
            readdb = csv.DictReader(db, delimiter=';') #ötlet: stackoverflow
            for column in readdb: #nyilván sorokat néz, viszont egy oszlopban található elemek kellenek
                if column['hallgató'] == hallgato:
                    if column['aláírás'] == '1':
                        return int(column['érdemjegy'])
                    else:
                        return 0
            raise AttributeError("Ez a Neptun-kód nem található.")
    else:
        raise FileNotFoundError(f'Nem található fájl: {path_eredmeny}')

def _get_targy_krediterteke(targy: str) -> int:
    """Lekérdezi egy tárgy kreditértékét.

    A kreditértékek a `targyak/[targy]/adatok.json` fájl "kredit" kulcsánál található.

    Args:
        targy (str): a keresett tárgy kódja

    Returns:
        int: a tárgy kreditértéke

    Raises:
        FileNotFoundError: ha a fájl nem található
        KeyError: ha a fájlban nem található a "kredit" kulcs
    """
    path_kredit = f'/workspaces/prog1-23t-hf10-HeyItsMedard/targyak/{targy}/adatok.json'
    if os.path.isfile(path_kredit):
        with open(path_kredit, 'r') as db:
            json_data = json.load(db)
            if "kredit" in json_data:
                return json_data["kredit"]
            else:
                raise KeyError('Hiányzó "kredit" kulcsérték.')
    else:
        raise FileNotFoundError(f'Nem található fájl: {path_kredit}')

def _get_kreditek(kezdes, index, by_neptun, targy):
    sumkredit, valkredit = 0, 0
    szemeszter = _get_felev_str(kezdes, index)  #hanyadik félév
    eredmeny = _get_kurzus_eredmeny(by_neptun, targy, szemeszter) #tárgyból kapott jegy
    if eredmeny != None:
        # try:
            sumkredit = _get_targy_krediterteke(targy)
            #print(type(eredmeny), type(sumkredit))
            valkredit = eredmeny*sumkredit
            return sumkredit, valkredit
    else:
        print(f"{by_neptun} nem szerzett jegyet {targy} tárgyból.")
        return None

def print_hallgato_atlag(osszes_felev: bool = True) -> None:
    """Kiírja a hallgató féléves vagy kumulatív átlagát.

    Az átlag a felvett tárgyak kreditértékével kerül súlyozásra.
    A nem teljesített tárgyak 0-nak számítanak, függetlenül attól, hogy a nem teljesítés
    oka az aláírás hiánya, a vizsgákról való hiányzás, vagy az 1-es érdemjegy.

    Args:
        osszes_felev (bool, optional): ha False, akkor megkérdezi a félévet, különben az
            összes félév tárgyának átlagát számolja ki. Alapértelmezetten True.
    """
    # hallgató neptun kódjának bekérése
    by_neptun = input("Kérjük, adja meg a hallgató Neptun kódját: ").upper()
    # hallgató adatainak beolvasása
    try:
        hallgato =_load_hallgato(by_neptun)
    except AttributeError: # ha nem található, akkor hibaüzenet és visszatérés
        print(("Ez a Neptun-kód nem található."))
        return
    kezdes = f'{hallgato["kezdés"][:4]}_{hallgato["kezdés"][4:]}'
    sumkredit, valkredit = 0, 0
    # ha nem kell az összes félév, akkor félév bekérése
    if not osszes_felev:
        felev = input("Kérjük, adja meg a félévet: ")
        # ha szám, akkor sorszám alapján, ha nem, akkor név alapján keresés
        if felev.isdigit():
            index = int(felev) - 1
        else:
            index = _get_felev_index(kezdes, felev) #pl. 0 mert azonos
        # eddig van: neptun kód, hallgató adatai, félév
        for targy in hallgato["félévek"][index]: #pl. 1. félévet nézi
            kredszamok = _get_kreditek(kezdes, index, by_neptun, targy)
            if kredszamok is not None:
                sumkredit += kredszamok[0]
                valkredit += kredszamok[1]
    else:
        for index, felev in enumerate(hallgato["félévek"]): #összes félév, 0. [TÁRGY1, TÁRGY2...]
            for targy in felev: #TÁRGY1, TÁRGY2
                kredszamok = _get_kreditek(kezdes, index, by_neptun, targy)
                if kredszamok is not None:
                    sumkredit += kredszamok[0]
                    valkredit += kredszamok[1]

    # súlyozott átlag kiszámítása
    try:
        sulyatlag = valkredit/sumkredit
    # a ZeroDivisionError elkapásával kezelje le, ha a nevező 0, és az átlag legyen 0.0
    except ZeroDivisionError:
        sulyatlag = 0.0
    # átlag kiírása
    print(f"Súlyátlag: {sulyatlag}")
