
A feladat egy ötöslottó sorsoló rendszer elkészítése.

A `szelvenyek.json` fájlban találhatók a sorsolásban résztvevő **Játékos**ok és a **Szelvény**eik.
Minden Játékoshoz tárolva van egy *név* és a hozzátartozó *szelvények* tömbje (egy játékosnak több szelvénye is lehet).
Minden **Szelvény** egy pontosan 5 különböző számot tartalmazó lista.

Készíts egy `sorsol()` függvényt, ami véletlenszerűen generál 5 *különböző* nyerőszámot 1 és 20 között, és visszaadja őket eredményül.

Készíts egy `kiertekel(szelveny, nyeroszamok)` függvényt, ami a paraméterben kap egy **Szelvényt** és a kisorsolt nyerőszámokat, és visszaadja, hogy hány találatos a szelvény, vagyis hány egyezés van a két számsorban.
A számok sorrendje tetszőleges lehet, nem szabad befolyásolnia a függvény eredményét.

A `nyeremeny.txt` 6 db, egy-egy egész számot tartalmazó sorból áll, melyek megadják, hogy hány Ft nyeremény jár 0, 1, 2, 3, 4, illetve 5 találatért, szelvényenként.


A fenti fájlok és függvények segítségével készíts egy programot, amely:
1. Kisorsolja és megjeleníti a nyerőszámokat.
2. Kiírja a nyertesek nevét és össznyereményét a `nyertesek.txt` fájlba. (Lásd a példafájlt.) Aki nem nyert semmit, azt ne!
3. Kiírja a képernyőre, hogy hány db 5-, 4-, 3- és 2-találatos szelvény volt összesen.

Példa kimenet:
```
A mai nyerőszámok: 5, 7, 10, 17, 19
1 db 5-találatos szelvény
2 db 4-találatos szelvény
28 db 3-találatos szelvény
127 db 2-találatos szelvény
```