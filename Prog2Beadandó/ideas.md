
<span style="font-size: 1.5em;"> Legyen game over screen - hozzá megfelelő gif háttérben, középen az elért pontszámmal és szöveggel, hanggal is akár.  

<span style="font-size: 1.5em;"> Statisztika: highscore - egyéni - közösségi gombok, highscore egy max 10 elemű listát ad vissza névvel és ponttal; egyéninél: legjobb pontszám, átlag pontszám, játszott meccsek, eltöltött idő a játékban (lehet ehhez kéne logout time is és logout gomb); közösségi: össz játékosok száma, átlag legjobb pontszám, regisztrációk hónapra bontva gráf - még ezer lehetőség van  

Backburner:
def formatted_played_time(self):
        seconds = self.played_time.total_seconds()
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}:{int(minutes)}:{int(seconds)}"

<span style="font-size: 1.5em;"> Regisztrációs és bejelentkezéses errorok  

<span style="font-size: 1.5em;"> Legyen tudtára adva a játékosnak, hogy top 10-ben van!  

<span style="font-size: 1.5em;"> Kalkuláljon game over kiírásnál esetleg olyat is, hogy a játékosok hány százalékánál teljesített a játékos jobban!  

<span style="font-size: 1.5em;"> Kommentek!

<span style="font-size: 1.5em;"> Visszagomb bejelentkezésnek és regisztrációnak

<span style="font-size: 1.5em;"> Szebb több kevesebb gombok

<span style="font-size: 1.5em;"> Legvégén dokumentáció.
