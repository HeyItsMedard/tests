[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10904130)
JSON fájlokban meg vannak adva a márciusi időjárási mérések adatai néhány nagyvároshoz:
`["Sopron", "Gyor", "Szombathely", "Budapest", "Veszprem", "Szekesfehervar", "Zalaegerszeg"]`

Minden fájlban találhatóak a feladat szempontjából mellékes metaadatok, valamint a `"daily"` kulcs alatt időbélyegek és különböző időjárási jellemzők napi mérési adatsorai:

- `"time"`: dátumok (minden városnál azonos)
- `"temperature_2m_max"`: napi maximális hőmérséklet
- `"precipitation_hours"`: napi csapadékos órák száma
- `"windspeed_10m_max"`: napi maximális szélsebesség

### 1. feladat

Hol és melyik napon mérték a legnagyobb szélsebességet, és mennyi volt az értéke?

Példa programkimenet: `Maximális szélsebesség: 41.8 km/h, Sopron, 2023-03-11`

### 2. feladat

Hány olyan nap volt, amikor legalább az egyik városban 1 vagy több órán át hullott csapadék?

Példa programkimenet: `Csapadékos napok száma: 22`

### 3. feladat

Készíts egy `max_temp.csv` fájlt, amely megadja, hogy az egyes napokon mennyi volt a legmagasabb hőmérséklet, és melyik városban mérték.
Ha több városban is egyformán a legmagasabb volt, akkor bármelyikük megfelel.

Példa az eredmény fájl első 4 sorára:

```
2023-03-01;10.1;Budapest
2023-03-02;11.6;Gyor
2023-03-03;12.0;Budapest
2023-03-04;13.3;Sopron
```
