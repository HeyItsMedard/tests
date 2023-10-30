[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SFXAZa43)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12507064)
### 1. feladat

Készíts egy szavazatszámláló flask appot.

Hozz létre egy fájlt a szavazati lehetőségekkel, és a szavazatok számát is fájlban tárold (ugyanebben van egy külön fájlban).

A főoldalon jelenjenek meg a lehetőségek nevei, a szavazatok darabszámai és az arányuknak megfelelő progress bar-ok, továbbá szavazó gombok minden váláaszlehetőséghez.

Szavazás után frissüljenek a darabszámok a nézeten.

(Azzal nem kell foglalkozni, hogy egy felhasználó akármennyi szavazatot tud leadni.)

Példa:

![](voting.png)

### 2. feladat

Készíts aranyköpés-gyűjtő flask appot.

A főoldalon jelenjen meg a beküldött aranyköpések száma, és a navigációs linkek, melyek minden oldalon megegyeznek: "Főoldal", "Új aranyköpés", "Random aranyköpés", "Legfrissebb aranyköpés".
Ehhez használj template öröklődést!

Az egyes aranyköpések a "/<id>" URL-en legyenek elérhetőek. Jelenjen meg az aranyköpés szövege, valamint linkek az előző és következő aranyköpésre (csak ha van).

![](view_quote.png)

Az Új aranyköpés oldalon legyen egy textarea és egy Beküldés gomb. Ha a szöveg üres, vagy csak whitespace karakterekből áll, ne kerüljön mentésre. Különben beküldés után töltsön be az új aranyköpés oldala.

![](new_quote.png)
