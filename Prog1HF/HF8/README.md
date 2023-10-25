[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11045921)
A feladat egy egyszerű kvízjáték program elkészítése.

A programban lehessen kvízt játszani, és kérdéseket szerkeszteni.

A különböző funkciókhoz tartozó kódrészletek legyenek külön fájlokba rendezve.

### Játék

Kvízjáték indításakor írja ki az elérhető kérdések számát, és kérje be, hogy hány kérdés legyen a kvízben.

Sorsolja ki és keverje össze a megadott számú kérdést.

Egyesével jelenítse meg a kérdéseket, és kérje be a válaszokat.

A kvíz végén jelenítse meg az eredményt, pl.: "7/9 helyes válasz", majd térjen vissza a főmenübe.

#### Kérdés típusok

- MCQ (multiple choice question): Feleletválasztós kérdésnél a lehetőségeket írja ki véletlenszerű sorrendben `a) 1. válasz b) 2. válasz ...` formában, minden választ külön sorba írva, és kérje be a válasz betűjelét, kis- vagy nagybetűt is elfogadva. A JSON-ben az első válaszlehetőség a helyes.
- text: A válasz egy egysoros szöveg, a kis- és nagybetűk között ne tegyen különbséget.
- number: A választ fogadja el, ha az a $[correct-tolerance, correct+tolerance]$ intervallumban van. Törtszámokat is tudjon kezelni.
- true/false: A kérdés szövege előtt írja ki a `"True or False?"` szöveget. Válaszként fogadja el az alábbi értékeket, kis- és nagybetűs írásmódban is: `["true", "T", "yes", "Y", "false", "F", "no", "N"]`

### Kérdések törlése

Listázza a kérdések szövegeit, a sorszámukkal és típusukkal együtt, majd kérje be a törlendő kérdés sorszámát.

Addig ismételje, amíg 0-t vagy üres stringet nem ad meg a felhasználó. Ezután térjen vissza a főmenübe.

Hibás sorszám esetén írjon ki egy hibaüzenetet.

### Kérdések hozzáadása

Jelenítsen meg egy menüt (a főmenühöz hasonlóan), amiben az opciók az egyes kérdéstípusok, valamint a visszatérés a főmenübe.

Kérje be a kérdés szövegét, valamint a helyes választ. MCQ esetén kérjen be további válaszlehetőségeket, míg üres stringet nem ad meg a felhasználó.

A kérdés felvitele után térjen vissza a kérdések hozzáadása almenübe.
