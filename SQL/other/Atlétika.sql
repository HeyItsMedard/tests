use Atlétika

--1. Hozd létre a KALAPACS adatbázist!

--2. Hozd létre az EREDMENY, a SPORTOLO, az EDZO táblákat! Írd le a megfelelõ parancsokat!

create table eredmeny (spkod numeric(4), tavolsag numeric(4,2), vbeve numeric(4), 
						helyezes numeric(1), kivel numeric(4), kitol numeric(4))

create table sportolo (spkod numeric(4), spnev nvarchar(20), sporsz nvarchar(20), 
						edzokod numeric(4), spszul date)

create table edzo (edzokod numeric(4), edzorsz nvarchar(20), edzonev nvarchar(20), 
						edzoszul date, aktiv numeric(1))


--3. Vigyük fel a táblákba az egyes sportolók, edzõk, eredmények adatait!

insert into eredmeny (spkod, tavolsag, vbeve, helyezes, kivel, kitol)
	values 
	(1010, 78.13, 1996, 3, 1020, 1050)

insert into eredmeny (spkod, tavolsag, vbeve, helyezes)
	values 
	(1020, 79.93, 1996, 1),
	(1030, 83.33, 2024, 2),
	(1040, 78.88, 1998, 2),
	(1050, 77.77, 1998, 3),
	(1040, 79.65, 2000, 3),
	(1060, 80.22, 2020, 2),
	(1050, 80.12, 2004, 2),
	(1070, 81.54, 2016, 1),
	(1080, 80.88, 2014, 3)

insert into sportolo(spkod, spnev, sporsz, edzokod, spszul)
	values
	(1010, 'Kovács Géza',		'Magyarország',		3113, '1969-12-23'),
	(1020, 'Szergej Jevgenyev',	'Belorusszia',		3125, '1973-05-06'),
	(1030, 'Mike Tailor',		'USA',				3146, '1998-07-07'),
	(1040, 'Alekszej Litvinov',	'Azerbajdzsán',		3166, '1975-02-02'),
	(1050, 'Gécsek Tibor',		'Magyarország',		3245, '1966-03-05'),
	(1060, 'Jurij Szedih',		'Ukrajna',			3267, '1996-03-03'),
	(1070, 'Igor Kuznyecov',	'Belorusszia',		3241, '1979-05-05'),
	(1080, 'Frank Lewis',		'USA',				3314, '1978-04-15'),
	(1090, 'Abdulajev Atanov',	'Grúzia',			3117, '1976-06-12'),
	(1100, 'Alex Bailey',		'Nagy-Britannia',	3124, '1974-03-21')

insert into edzo(edzokod, edzorsz, edzonev)
	values
	(3113,	'Magyarország', 'Tóth Ede'),
	(3125,	'Belorusszia',	'Pjotr Kutuzov'),
	(3146,	'USA',			'John Jones'),
	(3166,	'Azerbajdzsán',	'Sztyepan Holadna'),
	(3245,	'Magyarország', 'Németh Pál'),
	(3267,	'Ukrajna',		'Vologya Scsitenko'),
	(3241,	'Belorusszia',	'Gavrik Lebegyev'),
	(3314,	'USA',			'Sam Thomas'),
	(3117,	'Grúzia',		'Iván Likopenko'),
	(3124,	'Nagy-Britannia', 'Eleonor Hravaty')

select * from eredmeny
select * from sportolo
select * from edzo


--4. Késõbb Frank Lewis edzõként is tevékenykedett. Vigyük fel adatait az EDZO táblába is!

insert into edzo(edzorsz, edzonev)
select sporsz, spnev from sportolo
	where spnev = 'Frank Lewis' 

select * from edzo

--5. Listázzuk ki hány különbözõ ország versenyzõje vett részt a világbajnokságokon 1996-tól 2100-ig!

select count(*) from
	(select distinct(sporsz) from sportolo s
		inner join eredmeny e on s.spkod = e.spkod
		where e.vbeve between 1996 and 2100) c


--6.  Írassuk ki a képernyõre a nyilvántartott eredményeket (NEV, TAVOLSAG, VBEVE, HELYEZES) világbajnokságok éve szerint növekvõ,
--	azon belül a helyezés szerint csökkenõ sorrendben!

select s.spnev, e.tavolsag, e.vbeve, e.helyezes from eredmeny e, sportolo s
	order by vbeve asc, helyezes desc
	

--7. Írjuk ki a képernyõre a világbajnokságok történetének legnagyobb eredményét elért versenyzõ edzõjének a nevét!

select edzonev from edzo ed
	inner join sportolo s on ed.edzokod = s.edzokod
	inner join eredmeny e on s.spkod = e.spkod
	where e.tavolsag = (select max(tavolsag) from eredmeny)


--8.  Írjuk azon versenyzõk neveit, akik két egymást követõ világbajnokságon is dobogóra tudtak kerülni!

insert into eredmeny (spkod, tavolsag, vbeve, helyezes)
	values (1020, 80.12, 2000, 1)

select spnev from sportolo 
	where spkod in (select e.spkod from eredmeny e, eredmeny er
						where e.spkod = er.spkod and e.vbeve + 4 = er.vbeve) 

--9. Adjuk meg azokat az edzõket, akiknek tanítványa 1980 elõtt született!

select e.edzonev from edzo e
	inner join sportolo s on e.edzokod = s.edzokod
	where s.spszul < '1980-01-01'

--10. Adjuk meg melyik évben dobták az amerikai versenyzõk által elért legkisebb eredményt!

select vbeve from eredmeny 
	where tavolsag = (select min(tavolsag) from eredmeny e, sportolo s
						where e.spkod = s.spkod and s.sporsz = 'USA')

--11. Írjuk le azt a lekérdezést, mely megmondja a 2010 és 2030 között megrendezésre 
--      Került világbajnokságok ezüstérmeseinek átlageredményét!

select avg(tavolsag) from eredmeny 
	where helyezes = 2 and vbeve between 2010 and 2030

--12. Hogy lehetne Igor Kuznyecov edzõkódját 3244-re módosítani?

update edzo
	set edzokod = 3244
	where edzonev = 'Igor Kuznyecov'

--13. Doppingolás miatt töröljük Mike Tailor-ra vonatkozó adatokat!

delete eredmeny from sportolo 
	inner join eredmeny on sportolo.spkod = eredmeny.spkod
	where sportolo.spnev = 'Mike Tailor'

delete from sportolo
	where spnev = 'Mike Tailor'
 
--14. Listázzuk ki azon versenyzõk neveit, akik minden VB-n nagyobbat dobtak annál a versenyzõnél, akiktõl a legjobban tartottak!
--a. belsõ lekérdezéssel

select s.spnev from sportolo s
	inner join eredmeny e on s.spkod = e.spkod
	where e.tavolsag > (select tavolsag from eredmeny
							where spkod in (select kitol from eredmeny))

--b. DESCARTES szorzattal



--15. Listázzuk ki azon versenyzõk neveit, akiknek a nemzetisége azonos a kivel edzene versenyzõ nemzetiségével!

select s.spnev from sportolo s
	where s.sporsz in (select s.sporsz from sportolo s
							inner join eredmeny e on s.spkod = e.spkod
							where  s.spkod = e.kivel)

--16. Adjuk meg azon dobogós versenyzõk neveit, akiknek (edzõként) késõbb a tanítványa is dobogóra állhatott!

select s.spnev from sportolo s
	inner join edzo e on s.spnev = e.edzonev
	where e.edzokod in (select s.edzokod from sportolo s, eredmeny e
							where s.spkod = e.spkod and e.helyezes >= 1)

--17.  Adjuk meg azon versenyzõl neveit, akik késõbb edzõként más országban dolgoztak!

select s.spnev from sportolo s
	inner join edzo e on s.spnev = e.edzonev
	where s.sporsz != e.edzorsz

--18. Adjuk meg a 2010-es VB nemzetenkénti átlageredményét! helyett 2000

select s.sporsz, avg(e.tavolsag) from eredmeny e
	inner join sportolo s on e.spkod = s.spkod
	where e.vbeve = 2000
	group by sporsz

--19. Adjuk meg a VB-kénti átlageredményeket!

select e.vbeve, avg(e.tavolsag) from eredmeny e
	inner join sportolo s on e.spkod = s.spkod
	group by e.vbeve

--20. Adjuk meg a volt Szovjetúnió tagállamainak átlag eredményét 2010 és 2020 között! (Ha szükséges vegyünk fel egy új táblát!)

create table szovjetunio (tagallam nvarchar(20))

insert into szovjetunio(tagallam)
	values
	('Azerbajdzsán'),
	('Észtország'),
	('Fehéroroszország'),
	('Grúzia'),
	('Kazahsztán'),
	('Kirgizisztán'),
	('Lettország'),
	('Litvánia'),
	('Moldova'),
	('Örményország'),
	('Oroszország'),
	('Tádzsikisztán'),
	('Üzbegisztán')

select * from szovjetunio

select avg(e.tavolsag) from eredmeny e
	inner join sportolo s on e.spkod = s.spkod
	where s.sporsz in (select tagallam from szovjetunio)
	and e.vbeve between 2010 and 2020
	 
--21. Módosítsuk a SPORTOLO táblát! Vegyük fel az egyes sportolók szponzorainak nevét!

alter table sportolo
add szponzor nvarchar(20)

select * from sportolo

--22. Módosítsuk az EDZO táblát! Vegyük fel az egyes edzõk lábméretét!

alter table edzo
add labmeret numeric(2)

select * from edzo

--23. Listázzuk ki azon edzõk nevét, akik sosem voltak aktív kalapácsvetõk, de tanítványuk ezüstérmet nyert!

select e.edzonev from edzo e
	inner join sportolo s on e.edzokod = s.edzokod
	inner join eredmeny er on s.spkod = er.spkod
	where e.edzonev not in (select spnev from sportolo) and er.helyezes = 2

--24. Listázzuk ki azon sportolók neveit, amelyben szerepl e betû! 

select spnev from sportolo
	where spnev like '%e%'

--25. Hozzunk létre egy nézetet, mely csak a 2050 utáni eredményeket tartalmazza!

create view [Eredmenyek 2050 utan] as
	select * from eredmeny
		where vbeve > 2050

--26. Ki dobta név szerint az amerikai dobóatléták által valaha elért legkisebb eredményt, amellyel a világbajnokságok történetében dobogóra lehetett állni?

select s.spnev from sportolo s
	inner join eredmeny e on s.spkod = e.spkod
	where e.tavolsag = (select min(e.tavolsag) from eredmeny e, sportolo s
							where e.spkod = s.spkod and s.sporsz = 'USA' and e.helyezes >= 1)

--27. Mikor született az a versenyzõ, aki az amerikai dobóatléták elért legkisebb eredményt dobta?

select s.spnev, s.spszul from sportolo s
	inner join eredmeny e on s.spkod = e.spkod
	where e.tavolsag = (select min(e.tavolsag) from eredmeny e, sportolo s
							where e.spkod = s.spkod and s.sporsz = 'USA')