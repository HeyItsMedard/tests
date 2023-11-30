use Pékség

create table pekaru (sutinev nvarchar(12), szall_ar smallint, darab smallint, szallid tinyint)

create table szallito (szallid tinyint, veznev nvarchar(15), kernev nvarchar(10), cim nvarchar(50))


insert into pekaru(sutinev, szall_ar, darab, szallid)
	values 
	('mákos buci',		90,		50,	1),
	('sós kifli',		40,		40,	2),
	('túrós batyu',		130,	75,	3),
	('mákos buci',		90,		15,	5),
	('túrós batyu',		130,	40,	4),
	('bulócska',		140,	15,	7),
	('mákos buci',		90,		15,	2),
	('diós kifli',		130,	50,	5),
	('bulócska',		140,	20,	6),
	('sós kifli',		40,		30,	4),
	('diós kifli',		130,	40,	1)

insert into szallito(szallid, veznev, kernev, cim)
	values
	(1,	'KOVÁCS',	'ANDREA',	'1102 Budapest Alsónémedi u.2.'),
	(2,	'KISS',		'ANITA',	'2045 Dunakeszi Fõ u. 11.'),
	(3,	'TÓTH',		'ANIKÓ',	'2000 Szentendre Barcsay sétány 4.'),
	(4,	'NÉMETH',	'FRUZSI',	'1117 Budatétény Kovács A. u.26.'),
	(5,	'SZABÓ',	'JUDIT',	'1105 Budakalász Petõfi u. 17.'),
	(6,	'HORVÁTH',	'NOÉMI',	'1115 Budapest-Sasad Arany J. u. 44.'),
	(7,	'VARGA',	'ZSUZSI',	'2134 Dunabogdány Sas Elemér u. 35.')

select * from pekaru
select * from szallito

--1. Írd le azt az utasítást, mely létrehozza a PEKARU táblát! (pontos szintaktikával!)
--2. Írja le azt a lekérdezést, amely kilistázza hány különbözó pékáru van az üzletben!

select count(distinct(sutinev)) from pekaru

--3. Az alábbi három lekérdezés ugyanarra a kérdésre válaszol.   (Biztos?)
--   Fogalmazd meg a kérdést magyar szavakkal!

-- 	SELECT VEZNEV, KERNEV FROM SZALLITO WHERE KERNEV < 'B';
--	SELECT VEZNEV, KERNEV FROM SZALLITO WHERE LEFT(KERNEV,1) = 'A';
--	SELECT VEZNEV, KERNEV FROM SZALLITO WHERE SUBSTRING(KERNEV,1,1) = 'A';

--  Add meg azt a lekérdezést, amely szintén ugyanerre a kérdésre válaszol az SQL LIKE függvényének felhasználásával!

select kernev from szallito
	where kernev like 'a%'

--4. Add meg azt a lekérdezést, mely megszámolja hány különbözõ pékárut szállított SZABÓ JUDIT beszállító az pékáru üzletbe!

select count(distinct(p.sutinev)) from pekaru p
	inner join szallito s on p.szallid = s.szallid
	where s.veznev = 'Szabó' and s.kernev = 'Judit'

--5. Írd le azt a lekérdezést, mely megadja az üzletben lévõ pékáruk összértékét (beszállítói áron) pékáruk szerint csoportosítva!

select distinct(sutinev), sum(szall_ar*darab) from pekaru
	group by sutinev

--6. Írd le azt a lekérdezést, mely kiírja a képernyõre a legdrágább pékáru szállítójának nevét és címét!

select concat(veznev, ' ', kernev) as Név , cim as Cím from szallito s
	inner join pekaru p on s.szallid = p.szallid
	where szall_ar = (select max(szall_ar) from pekaru)

--7. Írd le azt a parancsot, mely kiírja a képernyõre a diós kiflit forgalmazó szállítók székhelyének címét!

select cim as Cím from szallito s
	inner join pekaru p on s.szallid = p.szallid
	where sutinev like 'diós kifli'

--8. Az üzletvezetõ az alábbi lekérdezést írta be:

--	SELECT SUTINEV FROM PEKARU WHERE DARAB > 
--            (SELECT DARAB FROM PEKARU WHERE SZALLID = 1);
--    Mire volt kíváncsi? Fogalmazza meg értelmes magyar mondat segítségével! Miért hibás a lekérdezés?

--9. Az üzletvezetõ az alábbi lekérdezéseket próbálta ki egy adott cél érdekében. Közülük némelyik mûködött, némelyik nem, némelyik nem a kívánt eredményt szolgáltatta. Milyen kérdésre szeretett volna választ kapni? Mely lekérdezések alkalmasak erre? Miért nem mûködött némelyik lekérdezés? 
--Mit jelentenek, mit használnak ki az egyes lekérdezések? Megoldásodat részletesen ismertesd!

--SELECT SUTINEV, SZALL_AR FROM PEKARU WHERE SZALL_AR < MAX(SZALL_AR);
--SELECT SUTINEV, SZALL_AR FROM PEKARU WHERE SZALL_AR < (SELECT MAX(SZALL_AR) FROM PEKARU);
--SELECT SUTINEV, SZALL_AR FROM PEKARU WHERE SZALL_AR < ALL (SELECT SZALL_AR FROM PEKARU);
--SELECT Y.SUTINEV, Y.SZALL_AR FROM PEKARU X, PEKARU Y WHERE Y.SZALL_AR < X.SZALL_AR AND X.SZALL_AR = MAX(X.SZALL_AR);
--SELECT X.SUTINEV, X.SZALL_AR FROM PEKARU X, PEKARU Y WHERE Y.SZALL_AR < X.SZALL_AR AND X.SZALL_AR = (SELECT MAX(SZALL_AR) FROM PEKARU);
--SELECT Y.SUTINEV, Y.SZALL_AR FROM PEKARU X, PEKARU Y WHERE Y.SZALL_AR < X.SZALL_AR AND X.SZALL_AR = (SELECT MAX(SZALL_AR) FROM PEKARU);

--10. Mi a különbség az alábbi két lekérdezés között! Mit látunk a képernyõn? 
--      Válaszodat részletesen ismertesd!

--	SELECT  SUTINEV, SUM(DARAB) FROM PEKARU WHERE SUTINEV LIKE  'm%' 
--          GROUP BY SUTINEV;

--	SELECT  SUTINEV, SUM(DARAB) FROM PEKARU GROUP BY SUTINEV HAVING 
--	SUTINEV LIKE  'm%';






--Tételezzük fel, hogy a pékáru boltos az alábbiak szerint képezi az eladási árakat

--Nettó ár = beszállítói ár  * 1.15
--Bruttó ár = Nettó ár + ÁFA = Nettó ár * 1.27

create function netto_ar (@szallar int)
returns float
	as 
	begin
		return @szallar * 1.15
	end

create function brutto_ar (@szallar float)
returns float
	as 
	begin
		declare @nettoar int
		set @nettoar = dbo.netto_ar(@szallar)
		return @nettoar*1.27
	end

create function haszon(@nagyobb float, @kisebb float)
returns float
	as
	begin
		return @nagyobb - @kisebb
	end


--11. Mennyi volt a pékáru üzlet az napi bruttó bevétele?

select sum(szall_ar * 1.15 * 1.27) from pekaru
select sum(dbo.brutto_ar(szall_ar)) from pekaru

select sum(szall_ar * 1.15 * 1.27 * darab) from pekaru
select sum(dbo.brutto_ar(szall_ar * darab)) from pekaru

--12. Mekkora volt a pékáru üzlet nettóérték alapján számolt nyeresége?

select sum(szall_ar * 1.15) - sum(szall_ar) from pekaru
select sum(dbo.netto_ar(szall_ar)) - sum(szall_ar) from pekaru

select sum(szall_ar * 1.15 * darab) - sum(szall_ar * darab) from pekaru
select sum(dbo.netto_ar(szall_ar * darab)) - sum(szall_ar * darab) from pekaru

--13. Adjuk meg termékenként a nettóérték alapján számolt nyereséget! A listát rendezzük a nyereség alapján csökkenõ sorrendbe, azaz a listán a legnagyobb nyereségû termék szerepeljen elõször!

select distinct(sutinev), (szall_ar * 1.15 - szall_ar) as [Netto nyereseg] from pekaru
	order by [Netto nyereseg] desc

select distinct(sutinev), (dbo.netto_ar(szall_ar) - szall_ar) as [Netto nyereseg] from pekaru
	order by [Netto nyereseg] desc
select distinct(sutinev), dbo.haszon(dbo.netto_ar(szall_ar), szall_ar) as [Netto nyereseg] from pekaru
	order by [Netto nyereseg] desc

select distinct(sutinev), (szall_ar * 1.15 * darab - szall_ar * darab) as [Netto nyereseg] from pekaru
	order by [Netto nyereseg] desc

select distinct(sutinev), (dbo.netto_ar(szall_ar * darab) - szall_ar * darab) as [Netto nyereseg] from pekaru
	order by [Netto nyereseg] desc


--14. Szûkítsük a 13. kérdés eredménylistáját oly módon, hogy azon csak az s betût tartalmazó és az 1000 Ft-nál nagyobb nyereséget hozó termékek legyenek rajta!

select distinct(sutinev), (szall_ar * 1.15 * darab - szall_ar * darab) as [Netto nyereseg] from pekaru
	where (szall_ar * 1.15 * darab - szall_ar * darab) > 1000 and sutinev like '%s%'
	order by [Netto nyereseg] desc

select distinct(sutinev), (dbo.netto_ar(szall_ar * darab) - szall_ar * darab) as [Netto nyereseg] from pekaru
	where (dbo.netto_ar(szall_ar * darab) - szall_ar * darab) > 1000 and sutinev like '%s%'
	order by [Netto nyereseg] desc


--15. Adjuk meg azt a listát, melyen a szállítók neve szerepel valmint a pékség által eladott termékeik össz beszállítói értéke. A lista név szerint legyen növekvõ sorrendbe rendezve!

select concat(s.veznev, ' ', s.kernev) as Nev, sum(p.szall_ar * p.darab) from szallito s
	inner join pekaru p on s.szallid = p.szallid
	group by concat(s.veznev, ' ', s.kernev)
	order by Nev asc