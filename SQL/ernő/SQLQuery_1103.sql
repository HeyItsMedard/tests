8. Tart-e a rakt�r sz�rkebar�tot �s k�kfrankost? 
Ha igen, �rassa ki a term�kek megnevez�s�t 
�s �f�s elad�si �r�t! Ez ut�bbi adat megnevez�se 
az eredm�nyben '�f�s �r' legyen!

t�bla

select * from CIKK

select * from CIKK
  where megnevezes like '%sz�rkebar�t%'

select * from CIKK
  where megnevezes like '%k�kfrankos%'

select * from CIKK
  where megnevezes like '%sz�rkebar�t%'
    and  megnevezes like '%k�kfrankos%'

if (select COUNT(*) from CIKK
  where megnevezes like '%sz�rkebar�t%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%k�kfrankos%') > 0

  select 'VAN'
  else
  select 'NINCS'

-- eld�ntend�
igen / nem

select * from cikk

select megnevezes, eladasiar,
  ELADASIAR*(1+AFAKULCS/100) as '�f�s �R',
   ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerek�tett'
      from cikk

select megnevezes, eladasiar,
  ELADASIAR*(1+AFAKULCS/100) as '�f�s �R',
   ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerek�tett',
   CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerek�tett2'
      from cikk

-- milyen t�pus� afakulcs?
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
  where megnevezes like '%sz�rkebar�t%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%k�kfrankos%') > 0
    -- select 'VAN'
   select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as '�f�s �R',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerek�tett',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerek�tett2'
        from cikk
     where megnevezes like '%sz�rkebar�t%'
	    or megnevezes like '%k�kfrankos%'
  else
  select 'NINCS'

--
if exists (select * from CIKK
  where megnevezes like '%sz�rkebar�t%') 
  and
   exists (select * from CIKK
  where megnevezes like '%k�kfrankos%')
    -- select 'VAN'
   select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as '�f�s �R',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerek�tett',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerek�tett2'
        from cikk
     where megnevezes like '%sz�rkebar�t%'
	    or megnevezes like '%k�kfrankos%'
  else
  select 'NINCS'

-- 
iif ??

select 
iif ((select COUNT(*) from CIKK
  where megnevezes like '%sz�rkebar�t%') > 0
  and
   (select COUNT(*) from CIKK
  where megnevezes like '%k�kfrankos%') > 0,
    -- iif igaz
    -- select 'VAN'
	-- 'VAN',
   (select megnevezes, eladasiar,
    ELADASIAR*(1+AFAKULCS/100) as '�f�s �R',
     ROUND(ELADASIAR*(1+AFAKULCS/100),0) as 'kerek�tett',
      CAST(ELADASIAR*(1+AFAKULCS/100)+0.5 as int) as 'kerek�tett2'
        from cikk
     where megnevezes like '%sz�rkebar�t%'
	    or megnevezes like '%k�kfrankos%'),
  /* else
  select 'NINCS' */
  'NINCS')

Msg 116, Level 16, State 1, Line 112
Only one expression can be specified 
in the select list when the 
subquery is not introduced with EXISTS.

--
9. �rassa ki azoknak a term�keknek a 
cikksz�m�t �s megnevez�s�t, valamint az aktu�lis 
�s a minim�lis rakt�rk�szlet�t, 
amelyekn�l a k�szlet az el��rt minim�lis k�szlet 
al� s�llyedt. Az adatok ABC sorrendben jelenjenek meg.

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

--sz�rmaztatott, sz�m�tott �rt�k alapj�n is lehet rendezeni

10. �rassa ki azon term�kek adatait, 
�s a term�kenk�nti hasznot, amelyekn�l 
a haszon, azaz az elad�si �r 
�s a termel�i �r k�l�nbs�ge, 
term�kenk�nt 10 Ft-n�l nagyobb, 
a mennyis�gi egys�g darab, 
�s a rakt�ri k�szlet 200 egys�gn�l magasabb! 
Az adatok a haszon szerint cs�kken� sorrendbe 
rendezve jelenjenek meg. 
Az eredm�nyben a haszon adatok oszlop�nak 
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

   -- rendezni lehet sz�rmaztatott/sz�m�tott �rt�k szerint
   -- alias szerint?  kifejez�s?
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

-- 11. �rassa ki azoknak a nem 25 %-os 
-- �fakulcs� term�keknek az adatait, 
-- amelyeknek a termel�i �ra 100 �s 250 Ft k�z� esik.

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

   between  adatt�pus  sz�mok/numerikus
                       d�tum
					   sz�veges  char nvarchar

select * from CIKK
   where 
     not (TERMELOIAR < 100 or TERMELOIAR > 250)

12. �rassa ki az 1998 m�sodik f�l�v�ben 
   �rkezett megrendel�sek adatait.

select * from rendeles

datum oszlop   datetime

select name from sys.types
  where system_type_id =
    (select system_type_id from sys.columns
       where name = 'datum')

I. f�l�v  01.01 - 06.30
II. f�l�v 07.01 - 12.31

select * from rendeles
 where datum > ???

select * from rendeles
  where datum >= '1998.07.01'

select * from rendeles
  where datum >= '1998-07-01'

  datetime >= char      implicit konverzi�

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
Mekkora a rakt�rb�l 1998.05.12-�n, 
a 41133404 cikksz�m� term�kb�l kisz�ll�tott �sszmennyis�g? 
Az �sszmennyis�g alatt a rendel�si 
t�telsorok mennyis�g adatainak �sszeg�t �rtj�k.

select * from rendeles

select * from rtetel

select * from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)

-- aggreg�l�s  SUM
select SUM(MENNYISEG) as �sszmennyis�g from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)
 
select * from rtetel
 where CIKKSZAM = 41133404

select SUM(MENNYISEG) as �sszmennyis�g from rtetel
  where cast(HATARIDO  as date) = cast('1998-05-12' as date)
   and CIKKSZAM = 41133404

-- 21. A 41777322 cikksz�m� term�kb�l 
-- mennyit sz�ll�tottak ki �tlagosan 
-- 1998. m�jus egy-egy dek�dj�ban?

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

select '1.dek�d', AVG(mennyiseg) �tlagmennyis�g
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 1 and 10
union
select '2.dek�d', AVG(mennyiseg) �tlagmennyis�g
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 11 and 20
union
select '3.dek�d', AVG(mennyiseg) �tlagmennyis�g
  from rtetel
   where YEAR(HATARIDO) = 1998 and MONTH(hatarido )= 5
		 and DAY(hatarido) between 21 and 30

-- d�tum?



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

select dekad, count(*) db, AVG(mennyiseg) [�tlagmennyis�g]
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
       end [dek�d]
from
RTETEL
 where
   YEAR(HATARIDO) = 1998 and MONTH(hatarido)= 5

 --- dek�d    temp t�bla �j oszlop
 group by dekad
 --  OK

 -- besorol�s
 -- kategori�kra bont�s
 -- szegment�ci�

 select 21/10

 select 5/10

 select DAY(getdate())  -- 2023-11-03
 -- int

 select DAY(getdate())/ 10 + 1  as [1.dek�d]

 v�s�rl�
  kor eloszl�si

    0-10
	11-20
	21-30
	..

select hatarido, (DAY(hatarido)-1) /10 +1 [dek�d]
from rtetel
  where YEAR(hatarido) = 1998
    and MONTH(hatarido) = 5

select (DAY(hatarido)-1) /10 +1 [dek�d],
   AVG(MENNYISEG) [�tlagmennyiseg]
from rtetel
  where YEAR(hatarido) = 1998
    and MONTH(hatarido) = 5
	group by (DAY(hatarido)-1) /10 +1

group by sz�rmaztatott/sz�m�tott �rt�k alapj�n

-- saj�t logik�t �rni
--  user-defined function
--  saj�t f�ggv�ny