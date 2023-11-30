use ZH

CREATE TABLE FagyiForg(MarkaID tinyint, MarkaNev nvarchar(20), 
                       ReklamSzoveg nvarchar(40), Forgalmazo nvarchar(40))

INSERT FagyiForg VALUES(1, 'Schöller','Jeges legjobb','Schöller Kft.')
INSERT FagyiForg VALUES(2, 'Leó', N'Oroszlánszelidítõ','Kiss Leó Bt.')
INSERT FagyiForg VALUES(3, 'Möwenpick', N'Ez finom', 'Schöller Kft.')
INSERT FagyiForg VALUES(4, 'Eskimo', 'Hú de hideg',	'Igloo Rt.')
INSERT FagyiForg VALUES(5, 'Cornetto', 'Szív küldi', 'Italy Rt.')
INSERT FagyiForg VALUES(6, 'Stollwerck', N'A szeretet íze', 'St.Hungary')
INSERT FagyiForg VALUES(7, 'Magnum', N'Édes bûnbeesés', 'Tom Magnum')

SELECT * FROM FagyiForg

CREATE TABLE FagyiSzin(IzKod tinyint, Iz nvarchar(20), Szin nvarchar(20))

INSERT FagyiSzin VALUES (1, 'eper', 'piros')
INSERT FagyiSzin VALUES (2, 'vanília', 'fehér')
INSERT FagyiSzin VALUES (3, 'málna', 'piros')
INSERT FagyiSzin VALUES (4, 'banán', 'sárga')
INSERT FagyiSzin VALUES (5, 'puncs', 'rózsa')
INSERT FagyiSzin VALUES (6, 'csoki', 'barna')
INSERT FagyiSzin VALUES (7, 'túró', 'fehér')
INSERT FagyiSzin VALUES (8, 'dinnye', 'sárga')

SELECT * FROM FagyiSzin

CREATE TABLE Fagyi(MarkaID tinyint, DvP bit, Adag tinyint, IzKod tinyint, Ar smallint)

INSERT Fagyi VALUES(1, 1, 10, 1, 335)
INSERT Fagyi VALUES(1, 1, 20, 1, 369)
INSERT Fagyi VALUES(1, 0, 10, 2, 329)
INSERT Fagyi VALUES(1, 1, 20, 3, 373)
INSERT Fagyi VALUES(2, 1, 20, 4, 369)
INSERT Fagyi VALUES(3, 0, 20, 1, 375)
INSERT Fagyi VALUES(4, 1, 30, 5, 411)
INSERT Fagyi VALUES(5, 0, 20, 6, 477)
INSERT Fagyi VALUES(4, 1, 25, 1, 489)
INSERT Fagyi VALUES(4, 0, 25, 1, 480)
INSERT Fagyi VALUES(4, 0, 25, 6, 499)
INSERT Fagyi VALUES(5, 0, 20, 7, NULL)
INSERT Fagyi VALUES(6, 0, 50, 2, 533)
INSERT Fagyi VALUES(7, 0, 20, 3, 473)
INSERT Fagyi VALUES(3, 0, 30, 8, 500)
INSERT Fagyi VALUES(3, 1, 30, 6, 512)

SELECT * FROM Fagyi


--1. Írasd ki azoknak a forgalmazóknak a nevét, akiknek a cégformája nem Kft és nem Rt!
--    A megoldásban mutasd be a de Morgan azonosságot!
--1.A. stringkezelõ függvény használatával

select Forgalmazo from FagyiForg
	where right(Forgalmazo, 4) != 'Kft.'
	and right(Forgalmazo, 3) != 'Rt.'

select forgalmazo from FagyiForg
	where charindex('Kft', Forgalmazo) = 0
	and charindex('Rt.', Forgalmazo) = 0

--1.B. LIKE operátor használatával

select MarkaNev from FagyiForg
	where  not (Forgalmazo like '%rt%' or Forgalmazo like '%kft%')

--2.  Van-e az adatbázisban olyan fagyi, amelyiknek Vacogi nem tudja az árát?
--     A megoldásban ne használd az IS operátort!
--2.A. A kérdésre adott válaz van/nincs
--      Használd az IF szerkezetet, avagy az IIF  függvényt!

if (select count(Ar) from Fagyi
		where Ar is NULL)  > 1
	select 'van'
else 
	select 'nincs'

--2.B. Találj olyan megoldást, amely az EXISTS kulcsszót használja!

if exists(
	select Ar from Fagyi
		where Ar is NULL)
	select 'van'
else 
	select 'nincs'

--3. A kínálatban dobozosból vagy pálcikásból van több?

if ((select count(DvP) from Fagyi where DvP = 1) > (select count(DvP) from Fagyi where DvP = 0))
	select 'Dobozos'
else 
	select 'Pálcikás'

--4. Hány különbözõ adagú (dkg) fagyi szerepel az adatbázisban?
--4.A.  A feladatot DISTINCT kulcsszó használatával oldd meg!

select count(distinct(Adag)) from Fagyi

--4.B. A feladatot DISTINCT kulcsszó használata nélkül oldd meg!

select Adag from Fagyi
	group by Adag

--5. Milyen ízû(ek) az adatbázisban szereplõ legnagyobb adagú (dkg) fagyi(k)? A lekérdezésben ne használd a MAX függvényt!

select top 1 Adag, Iz from Fagyi, FagyiSzin
	where Fagyi.IzKod = FagyiSzin.IzKod
	order by Adag desc

--6. Mely cég(ek) forgalmaz(nak) egynél több fagyi márkát!
--    Mi ezeknek a márkáknak a reklámszövege?
--6.A. A feladatot belsõ lekérdezéssel (subquery) oldd meg!

select Forgalmazo, MarkaNev, ReklamSzoveg from FagyiForg
	where Forgalmazo in (select Forgalmazo from FagyiForg
							group by Forgalmazo
							having count(MarkaNev) > 1)

--6.B. A feladatot tábla kapcsolással oldd meg!

select FF.Forgalmazo, FF.MarkaNev, FF.ReklamSzoveg from FagyiForg FF, FagyiForg FF2
	where FF.MarkaID = FF2.MarkaID
	and FF.Forgalmazo = FF2.Forgalmazo
	group by FF.Forgalmazo, FF.MarkaNev, FF.ReklamSzoveg
	having count(FF2.MarkaNev) > 1

--6.C. A feladatot CTE használatával oldd meg!

with CTE(Forgalmazo)
  as
   (select Forgalmazo from FagyiForg
		group by Forgalmazo
		having count(MarkaNev) > 1)
select Forgalmazo, MarkaNev, ReklamSzoveg from FagyiForg
	where Forgalmazo in (select * from CTE)


--6.D. A feladatot nézet (view) használatával oldd meg!

create view FagyiNezet as 
	select Forgalmazo from FagyiForg
		group by Forgalmazo
		having count(MarkaNev) > 1
select Forgalmazo, MarkaNev, ReklamSzoveg from FagyiForg
	where Forgalmazo in (select * from FagyiNezet)

--7. Add meg az egyes fagyik átlagárát!
--    Az átlag számítás során pontos értékekkel számolj, 
--   de az eredményt egész pontossággal add meg!
--7.A. fagyi íze szerint

select Szin, round(avg(Ar), 0) as [Átlag Ár] from Fagyi, FagyiSzin
	where Fagyi.IzKod = FagyiSzin.IzKod
	group by Szin

--7.B. adag szerint

select Adag, round(avg(Ar), 0) as [Átlag Ár] from Fagyi
	group by Adag

--7.C. fagyi íz és adag szerint

select Iz, Szin, round(avg(Ar), 0) as [Átlag Ár] from Fagyi, FagyiSzin
	where Fagyi.IzKod = FagyiSzin.IzKod
	group by Iz, Szin

--8. Írasd ki a táblázat szerinti azonos színû fagyikat  (párban)
--        sárga     banán dinnye
--        fehér     vanília túró
--        piros     eper    málna
--Egy-egy párosítás csak egyszer szerepeljen a listán
--(     piros eper málna
--      piros málna eper  ne legyen)

select F1.Szin, F1.Iz, F2.Iz from FagyiSzin F1, FagyiSzin F2
	where F1.Szin = F2.Szin
	and F1.Iz != F2.Iz 

select F1.Szin, F1.Iz, F2.Iz from FagyiSzin F1, FagyiSzin F2
	where F1.Szin = F2.Szin
	and F1.Iz != F2.Iz 
	and F1.IzKod > F2.IzKod

--9. Készítsd el azt a lekérdezést, amely az eredeti táblával hasonló szerkezetû
--    kilenc oszlopos táblázatot hozza létre!
--   A feladat megoldása során NE használj INNER JOIN-t!
--   Válaszd a megfelelõ OUTER JOIN-t (LEFT, RIGHT, FULL ??? )!
--   Választásodat indokold!

select FF.MarkaNev, iif (F.DvP = 1,'+', '-') as Dobozos, iif (F.DvP = 0,'+', '-') as Palcikas, F.Adag, FS.Iz, FF.ReklamSzoveg, FS.Szin, F.Ar, FF.Forgalmazo from Fagyi F
	left join FagyiForg FF on F.MarkaID = FF.MarkaID
	left join FagyiSzin FS on F.IzKod = Fs.IzKod

select FF.MarkaNev, iif (F.DvP = 1,'+', '-') as Dobozos, iif (F.DvP = 0,'+', '-') as Palcikas, F.Adag, FS.Iz, FF.ReklamSzoveg, FS.Szin, F.Ar, FF.Forgalmazo from Fagyi F
	right join FagyiForg FF on F.MarkaID = FF.MarkaID
	right join FagyiSzin FS on F.IzKod = Fs.IzKod

--10. Mennyibe kerülne Vacoginak, ha az összes Eskimo márkából vásárolna egyet-egyet?
	
select sum(Ar) from Fagyi, FagyiForg
	where Fagyi.MarkaID = FagyiForg.MarkaID
	and FagyiForg.MarkaNev like '%Eskimo%'
 
--11. A NAV elõírásai szerint az egyes forgalmazók adószámát a FAGYIFORG táblában
--      rögzíteni kell.
--      A NAV rendelkezésre bocsátotta az adószámokat a következõ NAVADO táblában!
CREATE TABLE NAVADO(Forgalmazo nvarchar(40), AdoSzam char(13))

INSERT NAVADO VALUES('Schöller Kft.','12121212-1-17')
INSERT NAVADO VALUES('Kiss Leó Bt.', '34343434-3-22')
INSERT NAVADO VALUES('Igloo Rt.',    '55555555-3-28')
INSERT NAVADO VALUES('Italy Rt.',    '23456781-1-21')
INSERT NAVADO VALUES('St.Hungary',   '10203040-2-19')
INSERT NAVADO VALUES('Magnum',       '21435461-2-44')

select * from NAVADO

--11.A.  Adj hozzá a FAGYIFORG táblához egy új oszlopot!

alter table FagyiForg 
	add Adoszam char(13)

select * from FagyiForg

--11.B.  SQL utasítás(ok) segítségével a NAV táblából írd be a megfelelõ adószámokat a módosított FAGYIFORG táblába!

update FagyiForg
	set Adoszam = (select AdoSzam from NAVADO where Forgalmazo = 'Schöller Kft.') where Forgalmazo = 'Schöller Kft.'

update FagyiForg
	set Adoszam = (select AdoSzam from NAVADO where Forgalmazo = 'Kiss Leó Bt.') where Forgalmazo = 'Kiss Leó Bt.'
...

--12. Bonus  Mely reklámszöveg(ek)ben szerepel a legtöbb  e    betû?

select ReklamSzoveg from FagyiForg
	
select top 4 ReklamSzoveg, len(ReklamSzoveg) - len(replace(ReklamSzoveg, 'e', '')) as Ebetukszama from FagyiForg
	order by Ebetukszama desc

--13. Bonus pontszerzési lehetõség

--  Van-e olyan ár, ami prímszám?
--307, 311, 313, 317, 331, 337, 347, 349,
--353, 359, 367, 373, 379, 383, 389, 397

--401, 409, 419, 421, 431, 433, 439, 443, 449,
--457, 461, 463, 467, 479, 487, 491, 499

create function isPrime (@number int) 
returns int as 
begin
	declare @result bit = 1, @i int = 2
	while (@i<@number)
		begin
			if(@number % @i = 0)
			begin
				set @result = 0
				break
			end
			set @i += 1
		end
	return @result
end

if exists(	
	select Ar from Fagyi
		where dbo.isPrime(Ar) = 1)
	select 'van'
else
	select 'nincs'

--Ne csak egyszerû halmazmûveletet tartalmazó lekérdezést írj!
--Adj SQL nyelven kivitelezhetõ megoldási javaslatot a prímség eldöntésére
--(segéd tábla, tárolt eljárás, felhasználói függvény...)