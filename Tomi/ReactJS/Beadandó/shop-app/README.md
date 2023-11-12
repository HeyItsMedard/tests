Med's Albums
=== 
## Leírás
Med's Albums egy React alkalmazás lesz, amely egy albumokat hirdető online platformot kínál a felhasználóknak. 
Az alkalmazás célja, hogy albumokat jelenítsen meg címmel és képpel együtt, és lehetővé tegye a felhasználók számára, hogy ezeket az albumokat kosárba rakják, majd ellenőrizzék a kiválasztott albumokat egy másik oldalon.

## Funkcionalitás
A projektnek a következő fő funkciókat kell tartalmaznia:

Albumok megjelenítése: Az alkalmazásnak egy főoldalt kell tartalmaznia, ahol az összes rendelkezésre álló albumot megjeleníti. Minden albumnak tartalmaznia kell a következőket:

- Cím
- Kép (album borító)
- Leírás (kiadási év, lemezkiadó, stb. opcionális)
- Ár

Albumok kosárba rakása: A felhasználóknak lehetőségük kell, hogy legyen az albumokat a kosárba rakni. Ezt a főoldalon egy + ikonnal vagy hasonló gombbal kell elérhetővé tenni minden album mellett.

Kosár megtekintése: A projektnek egy másik oldalt kell tartalmaznia, ahol a felhasználók megtekinthetik a kosarában található albumokat, illetve kivehessék kedvük szerint.

## Technológia
Az alkalmazás készítése során a következő technológiai stack szükséges:

- React: A projekt fő keretrendszere.
- JavaScript: Az alkalmazás logikájának írásához.
- CSS/SCSS: Az alkalmazás stílusozásához.
- React Router: Az oldalváltások kezeléséhez.
- Hook-ok: Funkciók véghez viteléhez.
- Storage: legyen mentve minden tevékenység, amit a user végrehajtott.
- API: még előre nem kiválasztott API. A fejlesztés során lesz igazán lehetőségem felfedezni, melyik lesz az alkalmazás számára hasznos.
- Github: verziókövetett fejlesztés.

### Egyéb ötletek:

- [ ] Web Host: régebb már használtam 000webhost-ot, de az például nem ad egyedi domaint. Próbálok felfedezni jobb lehetőségeket egy egyedi domain érdekében.
- [ ] Streaming platformok: a user felfedezheti az album zenéit vásárlás előtt. Ez lehet egy gomb is, ami egy kis részletet (vagy mixet) játszhat le, vagy egy lista elérhető streaming platformokról, amin meghallgathatja az albumot.
- [ ] Szűrés: genre, név, ár, kiadás típusa (CD/LP/kazetta...) stb. szerint.
- [ ] Keresés: a user rákereshet egy albumra (/artistra).

Az alkalmazás bővítésére rengeteg lehetőség van, így későbbiekben lehet szó további ötletekről.

### Wireframe:

![wf1](https://github.com/Uni-Sopron/web2-23o-HeyItsMedard/assets/62563792/5b7c4b2c-90fe-4487-8d07-85f553a084f2)
![wf2](https://github.com/Uni-Sopron/web2-23o-HeyItsMedard/assets/62563792/cb7e5b89-40fc-4cfe-9a8a-8b93dee71d3a)

Az elképzelésben eltérések, változtatások történhetnek.

### Start:

```bash
npm install
npm start
```

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/VhlUuMcI)
