--1. 	Hozd létre a VESZHELYZET adatbázist!

use Vészhelyzet

--2. 	Hozd létre az ORVOSOK táblát! Hozd létre az OSZTALYOK táblát!

create table Orvosok (Nro smallint, Nev varchar(20), Beosztas varchar(50), Munkaber int, Fonokkod smallint, Szuletes date, Okod tinyint)

create table Osztalyok (Okod tinyint, Osztaly varchar(20), Emelet tinyint)

--3. 	Töltsük fel az ORVOSOK táblát! Töltsük fel az OSZTALYOK táblát!

insert into Orvosok
	values
	(0001,	'Marc Green','Sebész	', 88885,	0335	, '1954-01-12',	123),
	(0012,	'Peter Benton','Sebész', 77776,	0001	, '1962-04-23',	145),
	(0007,	'Susan Howard','Anaszteziológus', 69876,	0234	, '1957-03-21',	123),
	(0045,	'John Carter	','Medikus', 30000,	0012	, '1966-11-12',	116),
	(0032,	'Sarah Brown	','Medikus', 32000,	0335	, '1961-05-13',	123),
	(0111,	'Dug Ross','Fül- orr gégész', 64000,	0555	,'1955-02-28',	145),
	(0123,	'Jimmy Tailor','Pszichológus', 59876,	0666	, '1949-11-13',	097),
	(0234,	'Nick Palmer	','Neurológus', 64341,	0335	, '1950-10-09',	097),
	(0176,	'Jeremy Dalton','Kardiológus', 78765,	0777	, '1953-07-21',	145),
	(0335,	'Frank Watson','Sebész', 99876,	0888	, '1939-02-03',	123),
	(0222,	'Bill Richard','Belgyógyász', 56789,	0654	, '1959-12-23',	116)

insert into Osztalyok
	values
	(123	, 'Traumatológia',	5),
	(145	, 'Intenzív',		4),
	(116	, 'Belgyógyászat', 	3),
	(097	, 'Idegosztály',		2),
	(088	, 'Gyermek osztály',3)

select * from Orvosok
select * from Osztalyok

--4. 	Listázd ki hány különbözõ beosztású orvos van!

select count(distinct Beosztas) from Orvosok 

--5.	Listázd ki a második emeleten dolgozó orvosok születési dátumát!

select Nev, Szuletes from Orvosok, Osztalyok
	where Orvosok.Okod = Osztalyok.Okod
	and Emelet = 2

--6.	Írjuk ki az összes J betûvel kezdõdõ orvos nevét és 	beosztását!

select Nev, Beosztas from Orvosok
	where Nev like 'J%'

--7.	Adjuk meg a belgyógyászaton dolgozó orvosok nevét, beosztását csökkenõ névsorrendben!

select Nev from Orvosok 
	where Beosztas = 'Belgyógyász'
	order by Nev desc

--8.	Add meg azoknak az orvosoknak a nevét, beosztását, születési dátumát belsõ lekérdezéssel, akik többet keresnek John Carter-nél!

select Nev, Beosztas, Szuletes from Orvosok 
	where Munkaber > (select Munkaber from Orvosok 
						where Nev like '%John Carter%')

--9.	Add meg azoknak az orvosoknak a nevét, beosztását, osztály kódját Descartes szorzat képzéssel (és/vagy INNER JOIN használatával) és a 
--megfelelõ feltétel megadásával, akik kevesebbet keresnek Green doktornál!

select Nev, Beosztas, Szuletes from Orvosok 
	where Munkaber < (select Munkaber from Orvosok 
						where Nev like '%Green%')

select O.Nev, O.Beosztas, O.Okod from Orvosok O, Orvosok Orv
	where Orv.Nev like '%Green%' 
	and O.Munkaber < Orv.Munkaber

--10.	Add meg az intenzív osztályon dolgozók átlag munkabérét!

select round(avg(Orvosok.Munkaber),0) from Orvosok, Osztalyok
	where Orvosok.Okod = Osztalyok.Okod
	and Osztalyok.Osztaly = 'Intenzív'

--11.	Adj Benton doktornak 20% munkabér emelést!

update Orvosok
	set Munkaber = Munkaber  * 1.2 
	where Nev like '%Benton%'

--12.	Írasd ki az összes olyan osztályt, amelyben legalább két sebész dolgozik!

select O.Osztaly from Osztalyok O
	inner join Orvosok Orv on O.Okod = Orv.Okod
	group by O.Osztaly
	having count(Orv.Okod) > 1
