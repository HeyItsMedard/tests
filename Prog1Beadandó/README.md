HIGHER OR LOWER -  MAGYAR YOUTUBE EDITION
=== 

A játék alapkoncepciója a híres Higher Or Lower internetes játék alapján készült.

Az egyedi csavar benne, hogy ezúttal a magyar YouTube tartalmainak nézettségeit vesszük figyelembe az internetes keresések helyett.  
A játékosok tesztelhetik tudásukat és érzéküket, milyen videó vajon mennyi nézettséget generálhatott.  
Egy olyan platformon, ahol nagyon sokat számít az, mennyire eladható és fogyasztható egy tartalom, ez az érzék nélkülözhetetlen. 

**FONTOS!** A programhoz szükséges:  
- pip install inputimeout (időzítő)
- pip install playsound (hang) -> Easter Eggnek, alapból ki van kommentelve minden ehhez kapcsolódó line (random nem olvas be néha audiót)  

A program elindításához a main.py fájlt kell futtatni.

## Játék

Az 1. menüpont kiválasztása után témát lehet választani. Ki miben érzi magát erősnek, magának válogatja.  
Alapvetően elérhető témák között trending és zene is. (Ezeket, ha lehet, ne töröljük vagy módosítgassuk, csak a tartalmát.)  
A trendingből készítettem egy demo verziót, melyben csak 10 videó van, ezzel könnyen tesztelve a játékot.   
Üresen létrehoztam egy gaming json-t is, amiben a felhasználó kedve szerint bővítget, tesztelhet ugyanúgy.  

Egy szám beírása után a játékos eldöntheti, hogy szeretne nehéz fokozatban játszani (igen/nem válasszal).  
A különbség a normál fokozattól, hogy a tartalomgyártók neve egyszer sem jelenik meg, a játékos fel kell mérje magának a tartalom címe alapján, kitől jöhet, illetve hogyan teljesíthetett.   
Emellett egy 10 másodperces időzítő tovább nehezíti játékosunk dolgát, ezalatt esélytelen, hogy utánanézzen a helyes válasznak.

Ezalól kivétel a zene, ahol az előadó és szám címe szerepelni fog ugyanúgy (de időzítővel).

Említésre méltó, hogy a végső eredmények témának és nehézségnek megfelelően külön top 10-es highscore listát kap.

## Játékmenet

A játékos az eredeti játékhoz hűen el kell döntse, melyik tartalom kapott nagyobb nézettséget. Az első tartalom nézőszáma mindig is látható, a következőképpen:  
+ `1) tartalom címe -> 600000 nézőszám`

A második tartalom nézettsége rejtett.
+ `2) tartalom címe -> ??? nézőszám`

Ha a játékos helyesen válaszol, a játék ad egy pontot, kicseréli a második kérdést az elsőre, az elsőt el is távolítja a játékból. Ezután betölti a következő kört.  
A játék addig tart, amíg a játékos rosszul nem válaszol, vagy a játék kifogy kérdésekből - ami ha nem a demo, akkor elég sok idő (nehéz fokozatban az időből kifutás is game over-t jelent).  
A játékos, ha szerzett pontot a játék során és a témában a top 10-ben szereplő "leggyengébben muzsikáló" játékosnál többet szerzett, mentheti a rekordját.  
Ha Entert nyom, a neve automatikusan Anonymus lesz. Ha már egyszer létezett ugyanezen néven játékos, a pontszámot csak akkor írja felül, ha jobbat ért el (vagyis kétszer nem ad hozzá játékost a listához).

## Adatok

### Adat hozzáadása

A 2. menüpont kiválasztásakor lehetőségünk van készíteni új témát, vagy témán belül új tartalomgyártót, tartalmakat.

### Adat törlése

A 3. menüpont kiválasztásakor fel van adva a lehetőség, hogy témát, vagy melyik témából egy tartalomgyártót vagy annak egy tartalmát szeretnénk törölni.

### Adat módosítása

A 4. menüpont kiválasztásakor fel van adva a lehetőség, hogy témát, vagy melyik témából egy tartalomgyártót vagy annak egy tartalmát szeretnénk szerkeszteni.  
Téma és tartalomgyártó esetén a nevüket lehet, tartalom esetén a nevét és annak a nézettségét.

### Highscore lista

Az 5. menüpont kiválasztásakor az általunk keresett highscore adatbázist listázhatjuk ki, pontosabban a listán szereplő játékosokat pontszámmal együtt, pontszám szerint sorrendben.   
Legfeljebb 10 játékos és eredménye szerepelhet egy adatbázisban. Ez azt is jelenti, hogy egy játékos csak egyszer szerepel egy listán (kivétel, ha Anonymus).

### Leírás és segítség

A 6. menüpont kiválasztásakor a most látható szöveges fájlt adja ki a felhasználó számára is.

## Inspiráció és forráshasználat

Eredeti játék: http://www.higherlowergame.com

Kérdés házi feladat

ChatGPT segített:
- restart_from_main() (database.py)
- részben a téma fájlok kezelésében
- timerekkel próbálkozás (test.py)

Importok:  
> https://www.geeksforgeeks.org/play-sound-in-python/  
> https://www.geeksforgeeks.org/how-to-set-an-input-time-limit-in-python/?ref=gcse

Adatbázisok:  
> StarNetwork  
> SocialBlade  
> YouTube  

Egyéb:
    Stackoverflow: errorok nagyrészt

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11282100)
