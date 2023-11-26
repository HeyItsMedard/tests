-- RENDELÉSEK - az órai gyakorlások magánmegoldása

-- use sopron2024
-- 1. feladat
-- Írassa ki azon vevők összes adatát, 
-- akik cégformája nem KFT és nem RT!
select * from vevo
	where VEVONEV not like '% RT%'
	AND Vevonev NOT LIKE '% KFT%'

-- 2. feladat
-- Írassa ki azoknak a vevőknek a címét, 
-- és a számlavezető bankjuknak a megnevezését, 
-- akiknek telephelye vidéken van, és nem az OTP-nél vezetik a számlájukat.

select utcahaz, bankjel from vevo
	where varos != 'Budapest'
	and bankjel != 'OTP'

-- 3. feladat
-- Milyen különböző bankok vezetik a vevők számláit?

select distinct bankjel from vevo

-- 4. feladat
-- Van-e olyan rendelési tételsor, 
-- ahol a határidő nem lett megadva?

select 
 iif(
  (Exists (select COUNT(*) from rtetel where HATARIDO  IS  NULL)),
   'NINCS','VAN') 

select COUNT(*) from rtetel
 where HATARIDO  IS  NULL --0

select HATARIDO from RTETEL --valóban nincs

-- 4.b. feladat
-- Van-e olyan rendelési tételsor, 
-- ahol a teljesítési dátum nem lett megadva?

select COUNT(*) from rtetel
 where TDATUM IS  NULL --96

if 
	EXISTS (select * from rtetel
		where TDATUM  IS  NULL) 
			select 'VAN'
		else
			select 'NINCS'

select
	iif(Exists
	(select * from rtetel where tdatum is NULL), --96 sor
	'VAN', 'NINCS') --létezik vagy sem
	AS [Van-e olyan rendelési tételsor, ahol a teljesítés nem lett megadva?]

--5. Van-e a vevők között olyan, 
-- akiknek a telephelye téren van? 
--Ha igen, irassa ki a nevét és a címét.

select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim from vevo 
	where utcahaz like '% tér %' or utcahaz like '% tere %' 

--6. Írassa ki azoknak a vevőknek a kódját és nevét, 
-- akiknek a neve "k" betűvel kezdődik!

select VEVOKOD, VEVONEV from vevo
	where charindex('k',vevonev)=1 -- left (vevonev,1) = 'k'/substring substring(vevonev,1,1) = 'k'

--7. Írassa ki azoknak a palack vagy üveg mennyiségi egységű termékeknek 
--a cikkszámát, 
--megnevezését, 
--mennyiségi egységét 
--és vámtarifaszámát, 
--melyeknek a vámtarifaszáma nem '88'-al kezdődik.

select CIKKSZAM, MEGNEVEZES, MEGYSEG, VTSZ from cikk
  where vtsz not like '88%' --where charindex('88',vtsz) != 1
  and (MEGYSEG = 'ÜVEG' OR MEGYSEG = 'PALACK') -- ilyen palack nincs btw

-- 8. Tart-e a raktár szürkebarátot és kékfrankost? 
--Ha igen, írassa ki a termékek megnevezését és áfás eladási árát! 
--Ez utóbbi adat megnevezése az eredményben 'áfás ár' legyen!

select MEGNEVEZES, ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'Áfás ár' from cikk
	where megnevezes like '%szürkebarát%'
    or megnevezes like '%kékfrankos%'

if (select COUNT(*) from CIKK
  where megnevezes like '%szürkebarát%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%kékfrankos%') > 0
    -- select 'VAN'
   select megnevezes, eladasiar,
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'Áfás ÁR'
        from cikk
     where megnevezes like '%szürkebarát%'
	    or megnevezes like '%kékfrankos%'
  else
  select 'NINCS'

-- 9. Írassa ki azoknak a termékeknek a cikkszámát és megnevezését, 
-- valamint az aktuális és a minimális raktárkészletét, 
-- amelyeknél a készlet az előírt minimális készlet alá süllyedt. 
-- Az adatok ABC sorrendben jelenjenek meg.

select CIKKSZAM, MEGNEVEZES, KESZLET, MKESZLET FROM CIKK
	where MKESZLET > KESZLET
	order by MEGNEVEZES asc, KESZLET asc
	--vagy külön orderelni vmelyik alapján, idk

-- 10. Írassa ki azon termékek adatait, és a termékenkénti hasznot, amelyeknél 
--a haszon, azaz az eladási ár és a termelői ár különbsége, 
--termékenként 10 Ft-nál nagyobb, a mennyiségi egység darab, és a raktári készlet 200 egységnél magasabb! 
--Az adatok a haszon szerint csökkenő sorrendbe rendezve jelenjenek meg. 
--Az eredményben a haszon adatok oszlopának neve legyen 'Haszon'.
select *, eladasiar-termeloiar as Haszon from cikk
	where eladasiar-termeloiar > 10 
	and keszlet > 200 
	and megyseg = 'DARAB' 

-- 11. Írassa ki azoknak a nem 25 %-os áfakulcsú termékeknek az adatait, 
-- amelyeknek a termelői ára 100 és 250 Ft közé esik.
select * from cikk
	where AFAKULCS != 25
	and TERMELOIAR between 100 and 250

-- 12. Írassa ki az 1998 második félévében érkezett megrendelések adatait.

--FONTOS! HOGYAN TUDD MEG EGY ADAT TÍPUSÁT
select name from sys.types
  where system_type_id =
    (select system_type_id from sys.columns
       where name = 'datum') --datetime

select * from rendeles
  where cast(datum as date) >= 
        cast('1998-07-01' as date)
		and
		cast(datum as date) <= 
        cast('1998-12-31' as date)

select * from rendeles
  where month(datum) >= 7
    		and
		year(datum) = 1998

--13. A rendelési tételsorokból írassa ki azokat, 
--amelyeknél a szállítási határidő 1998. május harmadik dekádjába esik, 
--de a termékek még nem lettek kiszállítva. 
--Az adatok szállítási határidő szerint csökkenő, cikkszám szerint növekvő sorrendben jelenjenek meg.

select * from rtetel
	where month(hatarido) = 5
    		and
		year(hatarido) = 1998
		and day(hatarido) >= ROUND(31/3, 0)*2
		and TELJESITVE = 0
	order by HATARIDO desc, CIKKSZAM asc

-- 14. Milyen különböző szállítási határidőkkel rendeltek termékeket a raktárról?
-- Az eredmény a szállítási határidő szerint növekvően rendezett legyen!

select distinct hatarido from rtetel
	order by hatarido asc

--15.  Írassa ki az '1/98'-as rendelésszámú, 5
--50 egységnél kisebb rendelt mennyiség , 
--már kiszállított tételeket!

select * from rtetel
	where MENNYISEG < 50
	and
	TELJESITVE = 1
	and
	RENDELESSZAM = '1/98'

-- 16. Hány db. tételsor tesz eleget a 15. kérdés feltételeinek?

select COUNT(*) from rtetel
	where MENNYISEG < 50
	and
	TELJESITVE = 1
	and
	RENDELESSZAM = '1/98'

-- 17. 
--Mekkora a raktárból 1998.05.12-én, 
--a 41133404 cikkszámú termékbõl kiszállított összmennyiség? 
--Az összmennyiség alatt a rendelési 
--tételsorok mennyiség adatainak összegét értjük.

select SUM(MENNYISEG) as összmennyiség from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)
   and CIKKSZAM = 41133404

--18. A '2/98'-as rendelésnél melyik a legkorábbi, 
--és melyik a legutolsó szállítási határidő?

select CONVERT(DATE ,MIN(Hatarido)) AS oldest, CONVERT(DATE ,MAX(Hatarido)) AS recent from rtetel
	where RENDELESSZAM = '2/98'

--19. A 41777322 cikkszámú termékből mennyit rendeltek összesen?

select COUNT(*) from RTETEL
	where CIKKSZAM = 41777322

-- 20. Hány különböző városban van a vevőknek telephelye?

select COUNT(distinct varos) as VarosCount from vevo

--21. A 41777322 cikkszámú termékből mennyit szállítottak ki átlagosan 1998. május egy-egy dekádjában?
-- ez a feladvány szimplán szar példa

select '1.dekád', AVG(mennyiseg) as átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 1 and 10
union
select '2.dekád', AVG(mennyiseg) as átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 11 and 20
union
select '3.dekád', AVG(mennyiseg) as átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 21 and 30 

--22. Mekkora a darab mennyiségi egység termékeknél 
--  a legkisebb, a legnagyobb és az átlagos raktárkészlet? 
select 'legkisebb', min(keszlet) as raktárkészlet from cikk
  where megyseg = 'DARAB'
union all
select 'legnagyobb', max(keszlet) as raktárkészlet from cikk
  where megyseg = 'DARAB'
union all
select 'átlagos',avg(keszlet) as raktárkészlet from cikk
  where megyseg = 'DARAB'

--23. Mekkora a legnagyobb értékû raktárkészlet 
--    áfás eladási árral számolva?
select max(keszlet * eladasiar*(1+afakulcs/100))
 as [legnagyobb értékû raktárkészlet] from cikk

--ChatGPT
SELECT TOP 1
    cikk.CIKKSZAM,
	CIKK.MEGNEVEZES,
    cikk.KESZLET * cikk.ELADASIAR * (1 + cikk.AFAKULCS / 100) AS [legnagyobb értékû raktárkészlet]
FROM
    cikk
ORDER BY
    [legnagyobb értékû raktárkészlet] DESC;

-- 24. Mekkora a legkisebb és legnagyobb haszon?
select  min(eladasiar - termeloiar) as legkisebb_haszon ,
        max(eladasiar - termeloiar) as legnagyobb_haszon 
from cikk

SELECT 'Legkisebb haszon' AS Tipus, cikk.MEGNEVEZES AS TermekMegnevezes, cikk.eladasiar - cikk.termeloiar AS Haszon
FROM cikk
WHERE cikk.eladasiar - cikk.termeloiar = (SELECT MIN(cikk2.eladasiar - cikk2.termeloiar) FROM cikk cikk2)

UNION ALL

SELECT 'Legnagyobb haszon' AS Tipus, cikk.MEGNEVEZES AS TermekMegnevezes, cikk.eladasiar - cikk.termeloiar AS Haszon
FROM cikk
WHERE eladasiar - termeloiar = (SELECT MAX(eladasiar - termeloiar) FROM cikk)
-- a legkisebb a chagpt féle, de ezt lehet szépíteni, mint látszik

-- 25. Mekkora a "Kg' mennyiségi egység termékek 
--    átlagos minimális raktárkészlete?

select avg(mkeszlet)  as [kérdés 25]
 from cikk
  where megyseg = 'kg'

select name from sys.types
  where system_type_id =
    (select system_type_id from sys.columns
       where name = 'mkeszlet') --smallint

--26. Hány db vevője van a raktárnak?
select COUNT(distinct VEVOKOD) from RENDELES --8, ha többszöri rendeléseket nem veszünk

--27. Hány db megrendelése van a raktárnak?
select count(*) as [Rendelések száma] from rendeles --17

--28. Mekkora értékű a teljes raktárkészlet termelői áron számolva?

select sum(keszlet*termeloiar) as [...] from cikk

SELECT 
    FORMAT(SUM(keszlet * termeloiar), 'C', 'hu-HU') AS TeljesRaktarErtek --forint by chatgpt
FROM 
    cikk

--29. Hány db különböző megrendelésben rendeltek '41773474'-es cikkszámú terméket?

SELECT COUNT(DISTINCT rendelesszam) AS RendelesSzamCount
FROM rtetel
WHERE cikkszam = '41773474';

--30. Van-e olyan város, ahol a bankok közül legalább egyben, legalább két vevő vezeti a számláját?

select * from vevo

select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
   having count(*) > 1

if exists (select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
  having count(*) > 1)
	select 'van'  as [....]
else
	select ' nincs' as [....]

--31. Vámtarifaszámonként hány különböző termék van a raktárban?

select vtsz, count(*) as db from cikk
 group by vtsz
   order by db desc

--32. Áfakulcsonként hány különböző eladási árú termék van a raktárban?

select afakulcs, count(*) as db 
   from cikk  
      group by afakulcs

--33. Van-e legalább három olyan termék, amelyeknek a vámtarifaszáma és az áfakulcsa is megegyezik? Írassa ki az ilyen termékek vámtarifaszámát, áfakulcsát, és a darabszámot!

if exists(
select vtsz,afakulcs, count(*)
   from cikk
    group by vtsz,afakulcs
	 having count(*) >=3)
select vtsz,afakulcs, count(*)
   from cikk
    group by vtsz,afakulcs
	 having count(*) >=3
else
 select 'nincs'

--34. Írassa ki azokat az eladási árakat, amelyek legalább két terméknél megegyeznek!

select eladasiar, COUNT(*) as Appearance from cikk
	group by ELADASIAR
	 having count(*) > 1

select * from cikk

--35. Írassa ki azokat a termelési árakat, amelyek egyediek, azaz csak egy terméknél fordulnak el!

select eladasiar, COUNT(*) as Appearance from cikk
	group by ELADASIAR
	 having count(*) = 1

--36. Írassa ki áfakulcsonként a maximális értékű minimális készlet értékeket! ????????
--ebben nagyon bizonytalan vagyok

select TOP 1 keszlet, afakulcs, MEGNEVEZES, TERMELOIAR from CIKK 
	where afakulcs = 12 -- insert afakulcs szam here
	order by KESZLET asc, TERMELOIAR desc
select * from CIKK where AFAKULCS = 12 -- 2 sor
select * from CIKK where KESZLET = 1

WITH RankedCikk AS (
    SELECT
        keszlet,
        afakulcs,
        MEGNEVEZES,
        TERMELOIAR,
        ROW_NUMBER() OVER (PARTITION BY afakulcs ORDER BY KESZLET ASC, TERMELOIAR DESC) AS RowNum
    FROM
        CIKK
)
SELECT
    keszlet,
    afakulcs,
    MEGNEVEZES,
    TERMELOIAR
FROM
    RankedCikk
WHERE
    RowNum = 1
--elméletileg, máshogy nem vágom hogy lehet vagy mit akar

--37.  Írassa ki az egyedi készlet értékeket!
select keszlet from CIKK group by keszlet having COUNT(keszlet) =1

--38. A vevőkód feltűntetésével írassa ki, hogy az egyes vevőknek hány rendelése van!
select VEVOKOD, COUNT(vevokod) as OrderCount from RENDELES group by VEVOKOD

--39. Írassa ki azokat a napokat, amelyeken legalább 2 megrendelés érkezett.
select DATUM, COUNT(datum) from RENDELES group by DATUM having COUNT(datum) > 1

--40. Írassa ki megrendelésenként a rendelésszám feltüntetésével 
-- a '41773474' cikkszámú termékből kiszállított összmennyiséget!
select RENDELESSZAM, SUM(MENNYISEG) from RTETEL 
	where CIKKSZAM = 41773474
	group by RENDELESSZAM

--41. Írassa ki a '9/98'-as megrendelésből a termékenként átlagosan rendelt mennyiséget!
select * from RTETEL
where RENDELESSZAM = '9/98'
select CIKKSZAM, AVG(MENNYISEG) as Atlag from RTETEL
	where RENDELESSZAM = '9/98'
	group by CIKKSZAM
	order by Atlag asc
--megnevezessel
SELECT RTETEL.CIKKSZAM, CIKK.MEGNEVEZES, AVG(RTETEL.MENNYISEG) AS AtlagMennyiseg
FROM RTETEL
INNER JOIN CIKK ON RTETEL.CIKKSZAM = CIKK.CIKKSZAM
WHERE RTETEL.RENDELESSZAM = '9/98'
GROUP BY RTETEL.CIKKSZAM, CIKK.MEGNEVEZES
order by AtlagMennyiseg asc

--42. Írassa ki termékenként a ki nem szállított tételek összmennyiségét.
select RTETEL.CIKKSZAM, CIKK.MEGNEVEZES, COUNT(teljesitve) as Unaccomplished from RTETEL
INNER JOIN CIKK ON RTETEL.CIKKSZAM = CIKK.CIKKSZAM
WHERE TELJESITVE = 0
Group by RTETEL.CIKKSZAM, CIKK.MEGNEVEZES
order by Unaccomplished desc

--43. Írassa ki rendelésenként és termékenként a minimális rendelt mennyiséget!

SELECT
    RENDELESSZAM,
    CIKKSZAM,
    MIN(MENNYISEG) AS MinRendeltMennyiseg
FROM
    RTETEL
GROUP BY
    RENDELESSZAM, CIKKSZAM

--44. Írassa ki rendelésenként, termékenként és a teljesítés módja szerint a rendelt összmennyiségeket, 
--valamennyi adatra vonatkozóan csökkenő sorrendbe rendezve!

SELECT
    RENDELESSZAM,
    CIKKSZAM,
    TELJESITVE,
    SUM(MENNYISEG) AS OsszMennyiseg
FROM
    RTETEL
GROUP BY
    RENDELESSZAM, CIKKSZAM, TELJESITVE
ORDER BY
    OsszMennyiseg DESC


--45. A teljes rendelés állományt figyelembe véve termékenként mekkora a legkisebb és a legnagyobb rendelt mennyiség?

SELECT
    CIKKSZAM,
    MIN(MENNYISEG) AS MinRendeltMennyiseg,
    MAX(MENNYISEG) AS MaxRendeltMennyiseg
FROM
    RTETEL
GROUP BY
    CIKKSZAM

--46.  Írassa ki azoknak a vevőknek a kódját, és nevét, akik rendeltek 25%-os áfa kulcsú terméket. 
-- A feladatot táblázatok kapcsolásával oldja meg! 

select  distinct V.vevokod, V.vevonev from cikk C
    inner join rtetel RT
	on C.cikkszam= RT.cikkszam
	inner join rendeles R
	on RT.rendelesszam = R.rendelesszam
	inner join vevo V
	on R.vevokod  = V.vevokod
	where  C.afakulcs =25

--47.  Írassa ki azoknak a vevőknek a kódját, és nevét, akik rendeltek 25%-os áfa kulcsú terméket.  
-- A feladatot alkérdés használatával oldja meg!

select vevokod,vevonev from vevo
 where vevokod in 
 (select vevokod from rendeles where
    rendelesszam in
	(select rendelesszam from rtetel
	  where cikkszam in
	   (select cikkszam from cikk 
	     where afakulcs = 25)))

--48. Írassa ki a '3/98'-as megrendelés tételeit úgy, hogy a termék neve is jelenjen meg.

select RT.RENDELESSZAM, C.MEGNEVEZES from rtetel RT inner join cikk C
 on RT.CIKKSZAM  = C.CIKKSZAM 
   where RT.RENDELESSZAM = '3/98'

--49. Írassa ki az 1998.03.18.-i megrendelések rendelési tételeit! A feladatot táblázat összekapcsolásával oldja meg!

select * from rtetel RT inner join rendeles R
 on RT.rendelesszam  = R.rendelesszam 
   where  cast(datum as date) = cast('1998-03-18' as date)

--50. Írassa ki az 1998.03.18.-i megrendelések rendelési tételeit! A feladatot alkérdés használatával oldja meg!

select * from rtetel
 where rendelesszam in
  (select rendelesszam from rendeles where
    datum = '1998-03-18')

--51. Írassa ki azon vevők kiszállított rendelési tételsorait, akik a Budapest Banknál (BB) vezetik számlájukat. 
--A feladatot alkérdés használatával oldja meg.

select * from rtetel
	where teljesitve = 1
	 and rendelesszam in
	(select rendelesszam from rendeles
	   where vevokod in (
		  select vevokod from vevo
			  where bankjel = 'BB'))

-- 52. Írassa ki a budapesti vevõk által rendelt, 
-- darab, vagy csomag mennyiségi egység  
-- termékek rendelési tételeit. 
-- A feladatot táblázat összekapcsolásával oldja meg! 
-- Az eredmény rendelésszám szerint, 
-- azon belül cikkszám szerint 
-- növekvõ sorrendbe rendezett legyen.

select RT.* from vevo V inner join rendeles R
     ON R.VEVOKOD = V.VEVOKOD
	 inner join rtetel RT
	 ON R.RENDELESSZAM = RT.RENDELESSZAM
     inner join  cikk C
	 ON RT.CIKKSZAM = C.CIKKSZAM
 where  V.varos = 'Budapest'
	  and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

select RT.* from vevo V cross join cikk C
    cross join   rtetel RT
	cross join rendeles R
where R.VEVOKOD = V.VEVOKOD
    and RT.CIKKSZAM = C.CIKKSZAM
	and R.RENDELESSZAM = RT.RENDELESSZAM
	and V.varos = 'Budapest'
	and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

--53. 52 csak subqueryvel

select * from rtetel
 where rendelesszam in
  (select rendelesszam from rendeles
 where vevokod in
   (select  vevokod
      from vevo where varos = 'Budapest'))
 and cikkszam in (
   select cikkszam from cikk 
   where megyseg = 'darab' or megyseg='csomag')
  order by rendelesszam asc, cikkszam asc

--54. Írassa ki a vidéki vevők megrendeléseinek adatait. A tételsorokat nem kell kiíratni. A feladatot a táblázatok összekapcsolásával oldja meg.

select R.* from vevo V INNER JOIN rendeles R
  ON V.vevokod = R.vevokod
   where V.VAROS != 'Budapest'

--55. A cikkszám és megnevezés feltüntetésével írassa ki, hogy az egyes termékekből mely napokon kell szállítani.

select C.cikkszam, C.megnevezes, R.hatarido
  from rtetel R INNER JOIN cikk C
     ON R.cikkszam = C.cikkszam