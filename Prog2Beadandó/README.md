HIGHER OR LOWER - MAGYAR YOUTUBE EDITION v2
=== 

A játék az előző félévi beadandónak egy továbbfejlesztett változata lesz, a Higher or Lower internetes játék alapján elkészítve. 

## Short-term ötletek dióhéjban

### YouTube API

Segítségével videók friss adatainak integrálása a játékba - json fájlok leváltása.  
A fejlesztés során tisztázódik, hogyan lehet hatékonyan integrálni az adatokat a játékba. Több lehetséges megközelítés lehet a videók friss adatainak beszerzésére, például...
- Playlistből (privát vagy publikus, előbbi esetén a játékhoz készítek saját listákat témák szerint, OAuth Token) beolvasva - legoptimálisabb ✔
- Téma szerint (nehéz felülvizsgálni, milyen tartalmakat fog visszaadni)
- Nézettség szerint stb.

A videókból főként a cím, tartalomgyártó és a nézettség lesz fontos a játékban. Esetleg további információk, mint a thumbnail, használhatóak lehetnek a játékélmény fokozására (hasonlóan a Higher or Lowernél, példával szemléltetve lentebb).

![Example](example.JPG)

### Flask

A konzolt a következőképpen váltom le:
- Webes felület: A Flask lehetővé teszi egy felhasználóbarát webes felület készítését a játék számára. A játékot szolgáltató Flask alkalmazás kezelheti a kéréseket és adhatja vissza a megfelelő válaszokat.
- Menük és interaktív elemek: A Flask segítségével könnyen kialakíthatók menürendszerek és interaktív elemek, például gombok és rubrikák, amelyek lehetővé teszik a játékosokkal való hatékony kommunikációt.
- Dinamikus tartalom: A Flask lehetőséget nyújt a dinamikus tartalom megjelenítésére, a tartalmakról lentebb lehet olvasni Long-term ötleteknél.

### SQLAlchemy 

SQL Adatbázis használata highscore rekordok tárolására és kezelésére, illetve további adatgyűjtéshez (erről szintén lentebb lehet olvasni Long-term ötleteknél).
Leváltaná a json fájlokat.

### További változtatások

A kódomat struktúráltabbá teszem azzal, hogy különálló class-okba szervezem. Ez nemcsak a kód átláthatóságát javítja, de lehetővé teszi a funkcionalitások logikai csoportosítását és az egyszerűbb karbantartást.✔

A továbbfejlesztésből kimaradhatnak olyan régebbi feature-ök, mint a téma, videó, tartalomgyártó hozzáadása és szerkesztése, vagy a nehézségi szint.

## Long-term ötletek 

Ezen ötletek megvalósítása időben túlnyúlhat a v2-ben (vizsgaidőszakban) elkészítendő követelmények megvalósításán.

- Modern design: "Minimum viable product" elv szerint, kezdetben a fókusz a játék működésén van, a kinézetének modernizálását későbbi fázisban tervezem végrehajtani – időfüggően. Cél, hogy valamelyest hasonlítson is az eredeti játékra.
- Elérhetőség: kaphasson saját domaint, amin elérhető lenne a játék.
- További statisztikák, mint például az összes játékos átlag pontszáma, egyéni high-score kimutatása, jelenlegi score kimutatása, összes játszott kör, ezeknek összefüggéséről diagram, legnépszerűbb kategória, játszott idő, stb. - akár Matplotlib használatával, ezek tovább gazdagíthatják a játékélményt.  
- Új játékmód: "Igaz, vagy Dazis?" - honorálva a Cringebait Podcast és csatorna tevékenységét, ez a játék a podcastjeikben fordult elő. A játék célja, hogy 3 videócím közül ki kell találni, melyik a hamis. Ez a játék hasonlóan addig tarthatna, amíg egy rossz guess-t nem ad a játékos, akárcsak a Higher or Lowernél. (Nehézség, hogy hamis címeket kézzel kéne készíteni, vagy valamilyen módszerrel generáltatni.) A játékmód elkészítése jelenleg jövőbeli lehetőségként áll fenn.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kedfMXW7)  
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13266045)

