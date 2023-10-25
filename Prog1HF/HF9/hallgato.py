
def _load_hallgato(neptun: str) -> dict:
    """Beolvassa és visszaadja egy hallgató adatait.

    Ha a megadott azonosító nem található, AttributeError-t dob.

    Args:
        neptun (str): a hallgató Neptun-azonosítója

    Returns:
        dict: a hallgató adatait tartalmazó szótár
    """
    return {}  # TODO


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
    return 0  # TODO


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
    return 0  # TODO


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
    return 0  # TODO


def print_hallgato_atlag(osszes_felev: bool = True) -> None:
    """Kiírja a hallgató féléves vagy kumulatív átlagát.

    Az átlag a felvett tárgyak kreditértékével kerül súlyozásra.
    A nem teljesített tárgyak 0-nak számítanak, függetlenül attól, hogy a nem teljesítés
    oka az aláírás hiánya, a vizsgákról való hiányzás, vagy az 1-es érdemjegy.

    Args:
        osszes_felev (bool, optional): ha False, akkor megkérdezi a félévet, különben az
            összes félév tárgyának átlagát számolja ki. Alapértelmezetten True.
    """
    # TODO
    # hallgató neptun kódjának bekérése
    # hallgató adatainak beolvasása
    # ha nem található, akkor hibaüzenet és visszatérés
    print("Ez a Neptun-kód nem található.")

    # TODO
    # ha nem kell az összes félév, akkor félév bekérése
    # ha szám, akkor sorszám alapján, ha nem, akkor név alapján keresés

    # TODO
    # súlyozott átlag kiszámítása
    # ha egy tárgy eredményeinek lekérdezésekor kivétel dobódik, írja ki a hibaüzenetet,
    # és hagyja ki a tárgyat a számításból
    # a ZeroDivisionError elkapásával kezelje le, ha a nevező 0, és az átlag legyen 0.0

    # TODO
    # átlag kiírása
