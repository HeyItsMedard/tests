[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12747081)
# Hackathon 2023 ősz

A feladat a Marrakech nevű társasjáték digitális implementációjának elkészítése.
A játékszabályok [itt](jatekszabaly.md) olvashatók.

A játéknak elég a 3 és 4 fős változatát kell elkészíteni.
Nincs titkos információ, így elég, ha egy számítógépen tudnak többen játszani egymás ellen.
Készíthető MI játékos is, a bonyolultságának függvényében figyelembe vesszük az értékelésnél.

A megoldáshoz tetszőleges technológia használható, de a tantervhez illeszkedve, Python használata javasolt.
Ehhez segítségül található a repóban egy lehetséges adatstruktúra és hozzátartozó interfész.

A megjelenítéshez saját grafikát kell készíteni.
A játék tematikája tetszőlegesen változtatható.

## Csapat tagjai

- *Csapattag neve és GitHub felhasználóneve*
- ...

## Beüzemelés és futtatás

*Szükség szerint frissíteni kell ezt a fejezetet a fejlesztés során.*

Telepíteni kell a Python 3.9+ verzióját. Opcionálisan létre lehet hozni egy virtuális környezetet a projektnek: `python -m venv .venv` és aktiválni a parancs által kiírt módon.

Telepíteni kell a felhasznált 3rd-party csomagokat:
```
pip install -r requirements.txt
```

*A felhasznált külső csomagokat adjátok hozzá a `requirements.txt` fájlhoz! Jelenleg néhány fejlesztést és tesztelést segítő eszköz található benne.*

A program elindítása:
```
python -m marrakech
```

## Tesztelés

Az elsős csapattagok még nem biztos, hogy részt tudnak venni a játék leprogramozásában.
A nagyoktól való tanulás és a grafikussal közös munka mellett a feladatuk, hogy teszteljék a már elkészült funkciókat.

Ezt lehet manuálisan is végezni. A megtalált hibákat GitHubon Issue létrehozásával célszerű dokumentálni.

Vagy lehet unit teszteket írni. Ehhez megtalálható pár példa a `tests` mappában.

A tesztfüggvények könnyedén futtathatók VS Code-ból a [Testing](https://code.visualstudio.com/docs/python/testing#_run-tests) fülön, vagy parancssorból:
```
python -m pytest
```

Új tesztek készítésénél arra kell figyelni, hogy a fájl neve és a függvény neve is `test_` prefixszel kezdődjön, és a `tests` mappába kerüljön.

Az ellenőrzés `assert <logic expr>` utasításokkal történik, ahol a `<logic expr>` egy olyan logikai kifejezés, aminek helyes működés esetén igaznak kell lennie.

## Bemutatás

Pénteken kell bemutatni az elkészült munkákat. Ez az elsős csapattagok feladata.

A prezentáció kerüljön fel a repóba, ennek a kötelező elemei:
- Csapattagok és feladataik
- Használt technológiák
- Képernyőképek a kész programról

Szintén kötelező élőben bemutatni a játékot működés közben.

Domborítsátok ki a megoldásotok erősségeit, de arra is kíváncsiak vagyunk, milyen nehézségek merültek fel, és hogy sikerült (vagy nem) megoldani őket.
