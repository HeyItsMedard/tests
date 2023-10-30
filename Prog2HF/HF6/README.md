[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/mXouGV50)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12308829)
## Feladatok

A meglévő egyszerű játékot kell továbbfejleszteni.

- Ne körökre osztott legyen, hanem 1 másodpercenként lépjenek a szörnyek.
- A szörnyek ne random irányokba lépjenek, hanem egy meghatározott (kezdetben random) irányba tartsanak.
  - Az aktuális irányt tárolja a Monster objektum.
  - Ha nem tud lépni, maradjon helyben, de forduljon random irányba.
  - A megjelenése utaljon a mozgási irányára, pl.: 👹 helyett ⏫, ⏪, ⏬, ⏩.
- Legyen mérve a játékidő. Győzelem esetén kérje be a nevet, adja hozzá a ranglistához (`leaderboard.txt`) az idővel együtt, és jelenítse meg a top 10-et a pálya alatt.
  - Ezzel párhuzamosan a pálya mutasson az eredménynek megfelelő animációt:
    - Győzelem esetén sorra pusztuljanak el a szörnyek (változzanak 💀 koponyává).
    - Vereség esetén teljen meg az egész pálya 👹 szörnyekkel.
    - Ehhez bővítsd a megfelelő osztályokat szükség szerint.
  - A ranglista megjelenítése után `Q` beírására álljon le a program.
