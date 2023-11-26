8. Tart-e a raktár szürkebarátot és kékfrankost? 
Ha igen, írassa ki a termékek megnevezését 
és áfás eladási árát! Ez utóbbi adat megnevezése 
az eredményben 'áfás ár' legyen!

tábla

select * from CIKK

select * from CIKK
  where megnevezes like '%szürkebarát%'

select * from CIKK
  where megnevezes like '%kékfrankos%'

select * from CIKK
  where megnevezes like '%szürkebarát%'
    and  megnevezes like '%kékfrankos%'

if (select COUNT(*) from CIKK
  where megnevezes like '%szürkebarát%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%kékfrankos%') > 0

  select 'VAN'
  else
  select 'NINCS'

-- eldöntendõ
igen / nem

select * from cikk

select megnevezes, eladasiar,
  ELADASIAR*(1+AFAKULCS/100) as 'Áfás ÁR',
   ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerekített'
      from cikk

select megnevezes, eladasiar,
  ELADASIAR*(1+AFAKULCS/100) as 'Áfás ÁR',
   ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerekített',
   CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerekített2'
      from cikk

-- milyen típusú afakulcs?
-- Object Explorer "meghalt"
select * from sys.columns

select * from sys.columns
  where name = 'AFAKULCS'

select * from sys.types
  where system_type_id = 62

select name from sys.types
  where system_type_id =
    (select system_type_id from sys.columns
       where name = 'AFAKULCS')

if (select COUNT(*) from CIKK
  where megnevezes like '%szürkebarát%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%kékfrankos%') > 0
    -- select 'VAN'
   select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as 'Áfás ÁR',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerekített',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerekített2'
        from cikk
     where megnevezes like '%szürkebarát%'
	    or megnevezes like '%kékfrankos%'
  else
  select 'NINCS'

--
if exists (select * from CIKK
  where megnevezes like '%szürkebarát%') 
  and
   exists (select * from CIKK
  where megnevezes like '%kékfrankos%')
    -- select 'VAN'
   select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as 'Áfás ÁR',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerekített',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerekített2'
        from cikk
     where megnevezes like '%szürkebarát%'
	    or megnevezes like '%kékfrankos%'
  else
  select 'NINCS'

-- 
iif ??

select 
iif ((select COUNT(*) from CIKK
  where megnevezes like '%szürkebarát%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%kékfrankos%') > 0,
    -- iif igaz
    -- select 'VAN'
	-- 'VAN',
   (select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as 'Áfás ÁR',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerekített',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerekített2'
        from cikk
     where megnevezes like '%szürkebarát%'
	    or megnevezes like '%kékfrankos%'),
  /* else
  select 'NINCS' */
  'NINCS')

Msg 116, Level 16, State 1, Line 112
Only one expression can be specified 
in the select list when the 
subquery is not introduced with EXISTS.

--
9. Írassa ki azoknak a termékeknek a 
cikkszámát és megnevezését, valamint az aktuális 
és a minimális raktárkészletét, 
amelyeknél a készlet az elõírt minimális készlet 
alá süllyedt. Az adatok ABC sorrendben jelenjenek meg.

select * from cikk

select * from cikk
  where KESZLET < mkeszlet

select CIKKSZAM, megnevezes, KESZLET, mkeszlet from cikk
  where KESZLET < mkeszlet

select CIKKSZAM, megnevezes, KESZLET, mkeszlet from cikk
  where KESZLET < mkeszlet
    order by MEGNEVEZES asc

select CIKKSZAM, megnevezes, KESZLET, mkeszlet from cikk
  where KESZLET < mkeszlet
    order by keszlet asc

select CIKKSZAM, megnevezes, KESZLET, mkeszlet from cikk
  where KESZLET < mkeszlet
    order by MKESZLET-keszlet desc

--származtatott, számított érték alapján is lehet rendezeni

10. Írassa ki azon termékek adatait, 
és a termékenkénti hasznot, amelyeknél 
a haszon, azaz az eladási ár 
és a termelõi ár különbsége, 
termékenként 10 Ft-nál nagyobb, 
a mennyiségi egység darab, 
és a raktári készlet 200 egységnél magasabb! 
Az adatok a haszon szerint csökkenõ sorrendbe 
rendezve jelenjenek meg. 
Az eredményben a haszon adatok oszlopának 
neve legyen 'Haszon'.

select * from CIKK
 where eladasiar - TERMELOIAR > 10
   and MEGYSEG = 'darab'
   and KESZLET > 200

select megnevezes, eladasiar, termeloiar,
    eladasiar - TERMELOIAR as [haszon],
	KESZLET, megyseg
	from CIKK
 where eladasiar - TERMELOIAR > 10
   and MEGYSEG = 'darab'
   and KESZLET > 200
   order by

   -- rendezni lehet származtatott/számított érték szerint
   -- alias szerint?  kifejezés?
   select megnevezes, eladasiar, termeloiar,
    eladasiar - TERMELOIAR as [haszon],
	KESZLET, megyseg
	from CIKK
 where eladasiar - TERMELOIAR > 10
   and MEGYSEG = 'darab'
   and KESZLET > 200
   order by eladasiar - TERMELOIAR desc

   --
    select megnevezes, eladasiar, termeloiar,
    eladasiar - TERMELOIAR as [haszon],
	KESZLET, megyseg
	from CIKK
 where eladasiar - TERMELOIAR > 10
   and MEGYSEG = 'darab'
   and KESZLET > 200
   order by haszon desc

-- 11. Írassa ki azoknak a nem 25 %-os 
-- áfakulcsú termékeknek az adatait, 
-- amelyeknek a termelõi ára 100 és 250 Ft közé esik.

select * from CIKK
 where AFAKULCS = 25

 select * from CIKK
 where not (AFAKULCS = 25)

select * from CIKK
 where AFAKULCS != 25

 select * from CIKK
 where AFAKULCS <> 25

 select distinct afakulcs from cikk

  select * from CIKK
 where AFAKULCS in (0,12)

 select * from CIKK
   where TERMELOIAR >= 100 and TERMELOIAR <= 250

    select * from CIKK
   where TERMELOIAR between 100 and 250

   between  adattípus  számok/numerikus
                       dátum
					   szöveges  char nvarchar

select * from CIKK
   where 
     not (TERMELOIAR < 100 or TERMELOIAR > 250)

12. Írassa ki az 1998 második félévében 
   érkezett megrendelések adatait.

select * from rendeles

datum oszlop   datetime

select name from sys.types
  where system_type_id =
    (select system_type_id from sys.columns
       where name = 'datum')

I. félév  01.01 - 06.30
II. félév 07.01 - 12.31

select * from rendeles
 where datum > ???

select * from rendeles
  where datum >= '1998.07.01'

select * from rendeles
  where datum >= '1998-07-01'

  datetime >= char      implicit konverzió

select * from rendeles
  where cast(datum as date) >= 
        cast('1998-07-01' as date)

select * from rendeles
  where datum between 
        cast('1998-07-01' as date) and
        cast('1998-12-31' as date)

select * from rendeles
  where cast(datum as date) >= 
        cast('1998-07-01' as date)
		and
		cast(datum as date) <= 
        cast('1998-12-31' as date)

select * from rendeles
  where cast(datum as date) >= 
        cast('1998-07-01' as date)
		and
		year(datum) = 1998

select * from rendeles
  where month(datum) >= 7
    		and
		year(datum) = 1998

select *, substring(datum,6,2) from rendeles
 -- where substring(datum,6,2)
 Msg 8116, Level 16, State 1, Line 286
Argument data type datetime is invalid 
for argument 1 of substring function.

select *, substring(cast(datum as char(10)),6,2) 
from rendeles
-- YYYY-MM-DD


select *, 
cast(datum as char(10)),
substring(cast(datum as char(10)),6,2) 
from rendeles

select *, 
--substring(
  cast(format(datum,'YYYY/mm/dd') as char(10))  --,6,2) 
from rendeles

select *, 
--substring(
  cast(format(
    cast(datum as date),'YYYY/mm/dd','hu-hu') 
	  as char(10))  --,6,2) 
from rendeles

select CONVERT(varchar(20),datum,112)
from rendeles

select *
from rendeles
  where 
   cast
    (substring(CONVERT(varchar(20),datum,112),5,2) as int)
	>=7

-- 17. 
Mekkora a raktárból 1998.05.12-én, 
a 41133404 cikkszámú termékbõl kiszállított összmennyiség? 
Az összmennyiség alatt a rendelési 
tételsorok mennyiség adatainak összegét értjük.

select * from rendeles

select * from rtetel

select * from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)

-- aggregálás  SUM
select SUM(MENNYISEG) as összmennyiség from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)
 
select * from rtetel
 where CIKKSZAM = 41133404

select SUM(MENNYISEG) as összmennyiség from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)
   and CIKKSZAM = 41133404

-- 21. A 41777322 cikkszámú termékbõl 
-- mennyit szállítottak ki átlagosan 
-- 1998. május egy-egy dekádjában?

05.01 - 05.10
05.11 - 05.20
05.21 - 05.30
05.31

select AVG(mennyiseg)
  from rtetel
   where YEAR(HATARIDO) = 1998
         and MONTH(hatarido )= 5
		 and DAY(hatarido) between 1 and 10

select * from rtetel
 where YEAR(HATARIDO) = 1998
         and MONTH(hatarido )= 5
		 and DAY(hatarido) between 1 and 10

select AVG(mennyiseg)
  from rtetel
   where YEAR(HATARIDO) = 1998
         and MONTH(hatarido )= 5
		 and DAY(hatarido) between 11 and 20

select '1.dekád', AVG(mennyiseg) átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 1 and 10
union
select '2.dekád', AVG(mennyiseg) átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 11 and 20
union
select '3.dekád', AVG(mennyiseg) átlagmennyiség
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 21 and 30

-- dátum?



-- group by??
select * into temp_dekad from rtetel

select * from temp_dekad

alter table temp_dekad add dekad tinyint

update temp_dekad set dekad = 1
  where HATARIDO between '1998-05-01' and '1998-05-10'

update temp_dekad set dekad = 1
  where cast(HATARIDO as date)
     between cast('1998-05-01' as date) 
	     and cast('1998-05-10' as date)

update temp_dekad set dekad = 2
  where cast(HATARIDO as date)
     between cast('1998-05-11' as date) 
	     and cast('1998-05-20' as date)

update temp_dekad set dekad = 3
  where cast(HATARIDO as date)
     between cast('1998-05-21' as date) 
	     and cast('1998-05-30' as date)

update temp_dekad set dekad = 4
  where cast(HATARIDO as date) = cast('1998-05-31' as date)

select dekad, count(*) db, AVG(mennyiseg) [átlagmennyiség]
 from temp_dekad
  where dekad is not null
   group by dekad

select * from rtetel

-- case when then
select hatarido,
  case when day(hatarido) >= 1 and DAY(hatarido) <= 10
            then '1.' 
			when day(hatarido) >= 11 and DAY(hatarido) <= 20
            then '2.' 
			when day(hatarido) >= 21 and DAY(hatarido) <= 30
            then '3.' 
			when day(hatarido) = 31 
            then '4.' 
       end [dekád]
from
RTETEL
 where
   YEAR(HATARIDO) = 1998 and MONTH(hatarido)= 5

 --- dekád    temp tábla új oszlop
 group by dekad
 --  OK

 -- besorolás
 -- kategoriákra bontás
 -- szegmentáció

 select 21/10

 select 5/10

 select DAY(getdate())  -- 2023-11-03
 -- int

 select DAY(getdate())/ 10 + 1  as [1.dekád]

 vásárló
  kor eloszlási

    0-10
	11-20
	21-30
	..

select hatarido, (DAY(hatarido)-1) /10 +1 [dekád]
from rtetel
  where YEAR(hatarido) = 1998
    and MONTH(hatarido) = 5

select (DAY(hatarido)-1) /10 +1 [dekád],
   AVG(MENNYISEG) [átlagmennyiseg]
from rtetel
  where YEAR(hatarido) = 1998
    and MONTH(hatarido) = 5
	group by (DAY(hatarido)-1) /10 +1

group by származtatott/számított érték alapján

-- saját logikát írni
--  user-defined function
--  saját függvény