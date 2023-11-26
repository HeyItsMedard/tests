
CREATE DATABASE medard

-- 2. �rassa ki azoknak a vev�knek a c�m�t, 
-- �s a sz�mlavezet� bankjuknak a megnevez�s�t, 
-- akiknek telephelye vid�ken van, 
-- �s nem az OTP-n�l vezetik a sz�ml�jukat.

CIKK
RENDELES
RTETEL
VEVO

SELECT * FROM VEVO

SELECT * FROM VEVO
  where VAROS = 'Budapest'

-- nem Budapest

SELECT * FROM VEVO
  where NOT (VAROS = 'Budapest')

SELECT * FROM VEVO
  where VAROS <> 'Budapest'

SELECT * FROM VEVO
  where VAROS != 'Budapest'

SELECT distinct varos from vevo

SELECT * FROM VEVO
  where VAROS = 'Kaposv�r'
     or VAROS = 'Miskolc'
	 or VAROS = 'Sopron'
	 or VAROS = 'Szombathely'

SELECT * FROM VEVO
  where VAROS in ('Kaposv�r','Miskolc',
	              'Sopron','Szombathely')


-- nem OTP

SELECT * FROM VEVO
  where NOT (BANKJEL = 'OTP')

SELECT * FROM VEVO
  where VAROS <> 'OTP'

SELECT * FROM VEVO
  where VAROS != 'OTP'

SELECT distinct bankjel from vevo

SELECT * FROM VEVO
  where BANKJEL = 'BB'
     or BANKJEL = 'KHB'

SELECT * FROM VEVO
  where VAROS in ('BB','KHB')

---

SELECT * FROM VEVO
  where NOT (VAROS = 'Budapest') and
        NOT (BANKJEL = 'OTP')

NOT A AND NOT B
NOT (A OR B)

SELECT * FROM VEVO
  where NOT (VAROS = 'Budapest' or BANKJEL = 'OTP')

SELECT * FROM VEVO
  where VAROS <> 'Budapest' and
        BANKJEL <> 'OTP'

SELECT * FROM VEVO
  where (VAROS <> 'Budapest') and
        (BANKJEL <> 'OTP')

SELECT * FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

SELECT IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim,
    bankjel
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

SELECT IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim,
    case 
	when bankjel = 'BB' then 'Budapest Bank'
	when BANKJEL = 'KHB' then 'Kereskedelmi �s HitelBank'
	end as [Bank megnevez�se]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')


SELECT CONCAT(
     CONCAT(
       CONCAT(
         CONCAT(IRANYITOSZAM,' '),VAROS)
		 ,' '),
		 UTCAHAZ) as cim,
    IIF(bankjel = 'BB','Budapest Bank',
	  IIF(bankJEL = 'KHB','Kereskedelmi �s HitelBank',
	      'nem tudom'))
	 as [Bank megnevez�se]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

CONCAT  overload
  olyan met�dus  t�bb f�le k�ppen
  k�t param�ter
  h�rom param�ter
  n�gy param�ter

SELECT CONCAT(IRANYITOSZAM,' ',VAROS,' ',UTCAHAZ) as cim,
    IIF(bankjel = 'BB','Budapest Bank',
	  IIF(bankJEL = 'KHB','Kereskedelmi �s HitelBank',
	      'nem tudom'))
	 as [Bank megnevez�se]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

select ASCII(' ')
select CHAR(32)

SELECT CONCAT(IRANYITOSZAM,CHAR(32),VAROS,CHAR(32),UTCAHAZ) as cim,
    IIF(bankjel = 'BB','Budapest Bank',
	  IIF(bankJEL = 'KHB','Kereskedelmi �s HitelBank',
	      'nem tudom'))
	 as [Bank megnevez�se]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

-- 3. Milyen k�l�nb�z� bankok vezetik a vev�k sz�ml�it?
SELECT distinct bankjel from vevo

SELECT distinct bankjel 
 as [Milyen k�l�nb�z� bankok vezetik a vev�k sz�ml�it?]
from vevo

SELECT bankjel from vevo
group by bankjel

SELECT bankjel 
 as [Milyen k�l�nb�z� bankok vezetik a vev�k sz�ml�it?]
 from vevo
group by bankjel

-- 4. Van-e olyan rendel�si t�telsor, 
--  ahol a hat�rid� nem lett megadva?

-- eld�ntend�  van/nincs   igen/nem

select * from rtetel

select * from rtetel
 where HATARIDO  IS  NULL

select COUNT(*) from rtetel
 where HATARIDO  IS  NULL

if 
 (select COUNT(*) from rtetel
   where HATARIDO  IS  NULL) = 0
 select 'NINCS' AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]
 else
 select 'VAN' AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]

 if 
 EXISTS (select * from rtetel
   where HATARIDO  IS  NULL) 
 select 'VAN' AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]
 else
 select 'NINCS' AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]


 
select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN')

select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN') 
  AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]
 
 select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN') 
  AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]

  select 
 iif(
  (Exists (select COUNT(*) from rtetel where HATARIDO  IS  NULL)),
   'VAN','NINCS') 
  AS [Van-e olyan rendel�si t�telsor, ahol a hat�rid� nem lett megadva?]



-- 4.b. Van-e olyan rendel�si t�telsor, 
--  ahol a teljes�t�si d�tum nem lett megadva?

if 
 (select COUNT(*) from rtetel
   where TDATUM  IS  NULL) = 0
 select 'NINCS' AS [Van-e olyan rendel�si t�telsor, ahol teljes�t�si d�tum nem lett megadva?]
 else
 select 'VAN' AS [Van-e olyan rendel�si t�telsor, ahol teljes�t�si d�tum nem lett megadva?]


 select COUNT(*) from rtetel
 --221
 select COUNT(tdatum) from rtetel
 -- 125

 if (select COUNT(*) from rtetel) >
    (select COUNT(tdatum) from rtetel)
 select 'VAN'
 else
 select  'NINCS'

 
 if (select COUNT(*) from rtetel) -
    (select COUNT(tdatum) from rtetel) > 0
 select 'VAN'
 else
 select  'NINCS'

  if (select COUNT(*) - COUNT(tdatum) from rtetel) > 0
 select 'VAN'
 else
 select  'NINCS'

 -- 5. 
 -- Van-e a vev�k k�z�tt olyan, 
 -- akiknek a telephelye t�ren van? 
 -- igen, irassa ki a nev�t �s a c�m�t.

 select * from vevo

 select * from vevo
 where utcahaz like '%t�r%'

  select * from vevo
 where utcahaz like '% t�r %'

 select * from vevo
 where utcahaz like '%'+CHAR(32)+'t�r'+CHAR(32)+'%'

  select * from vevo
 where utcahaz like '%  t�r %'

 if
 exists (select * from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %')
	-- then nincs   igaz �g
 select VEVONEV, 
   IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %'
	else
	 select 'nincs'   
	  as [Van-e a vev�k k�z�tt olyan, akiknek a telephelye t�ren van? ]

-- select eredm�ny�t tegy�k el
--    t�bla
--       fizikailag adatb�zisban
--        melyik  saj�t  Sopron2024   tempdb
--       v�ltoz�ban
--       mem�ri�ban 


select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
into mzperx from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %'

if
 exists (select * from mzperx)
	-- then nincs   igaz �g
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from mzperx
	else
	 select 'nincs'  

drop table mzperx

--
-- temporary table megold�s
select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
into #mzperx from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %'

if
 exists (select * from #mzperx)
	-- then nincs   igaz �g
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from #mzperx
	else
	 select 'nincs'  

--	 # kil�pek Query windows  automatikusan t�rl�dnek
-- NEM KELL: drop table #mzperx


-- mem�ri�ban dolgozik
-- select into @v�ltoz�  NINCS
-- t�bla l�trehoz�s, fejl�c, adatt�pus
declare @saj�tt�bla table
  (
  VEVONEV nvarchar(30),
  IRANYITOSZAM nvarchar(4),
  VAROS nvarchar(15),
  UTCAHAZ nvarchar(20)
  )

insert @saj�tt�bla
select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
  from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %'

if
 exists (select * from @saj�tt�bla)
	-- then nincs   igaz �g
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from @saj�tt�bla
	else
	 select 'nincs'  

@saj�tt�bla v�ltoz�  lok�lis
 automatikusan t�rl�dik  �rt�ke
 deallok�l

-- subquery
if select T.IRANYITOSZAM +T.VAROS+T.UTCAHAZ  as cim
(select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
  from vevo
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %') T


if exists(select * from T)
   select T.IRANYITOSZAM +T.VAROS+T.UTCAHAZ  as cim
   from 
   (select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
    from vevo
    where utcahaz like '% t�r %'
     or utcahaz like '% tere %') T
else
  select 'nincs'

-- CTE  common table expressions
WITH
SELECT

ld. k�s�bb november 3.

--
select * from vevo
 where (charindex(' t�r ',utcahaz) > 0) or
       (charindex(' tere ',utcahaz) > 0)
  
 select utcahaz, REPLACE(utcahaz,' t�r ','') from VEVO

 select * from vevo
 where (len(utcahaz) -
   len(REPLACE(utcahaz,' t�r ','')) > 0)


select * from vevo
 where (len(utcahaz) -
   len(REPLACE(utcahaz,' t�r ','')) > 0)  or
   (len(utcahaz) -
   len(REPLACE(utcahaz,' tere ','')) > 0)

-- 
-- 6. �rassa ki azoknak a vev�knek a k�dj�t �s nev�t, 
-- akiknek a neve "k" bet�vel kezd�dik!

   like 'k%'
   left (vevonev,1) = 'k'
   charindex('k',vevonev)=1
   substring(vevonev,1,1) = 'k'
   vevonev > 'JZZZZZZZ' and vevonev < 'LAAAAAAA'
   vevonev >= 'KAaaaaaaaaaaa' and vevonev <= 'KZZZZZZZ'

   -- 7. �rassa ki azoknak a palack vagy �veg 
   -- mennyis�gi egys�g� term�keknek a cikksz�m�t, 
   -- megnevez�s�t, mennyis�gi egys�g�t �s v�mtarifasz�m�t, 
   -- melyeknek a v�mtarifasz�ma nem '88'-al kezd�dik.

   select * from cikk

   select * from cikk
     where MEGYSEG = 'PALACK' or MEGYSEG='�VEG'

	 select * from cikk
     where MEGYSEG in ('PALACK','�VEG')


select * from cikk
  where vtsz like '88%'

select * from cikk
  where vtsz like '88%'

select * from cikk
  where not vtsz like '88%'

select * from cikk
  where not (vtsz like '88%')

select * from cikk
  where vtsz not like '88%'


select * from cikk
  where charindex('88',vtsz) = 1

select * from cikk
  where charindex('88',vtsz) <> 1

select * from cikk
  where charindex('88',vtsz) != 1


  --
   select * from cikk
     where (MEGYSEG = 'PALACK' or MEGYSEG='�VEG')
	   and  not vtsz like '88%' 

select * from
(select * from cikk
   where (MEGYSEG = 'PALACK' or MEGYSEG='�VEG')) T 
   where not T.vtsz like '88%' 


select cikkszam, megnevezes, 
       megyseg, vtsz
	   from cikk
     where (MEGYSEG = 'PALACK' or MEGYSEG='�VEG')
	   and  not vtsz like '88%' 

--
select cikkszam, megnevezes, 
       megyseg, vtsz
	   from cikk
     where MEGYSEG in ('PALACK','�VEG')
	   and not vtsz like '88%' 

select ASCII('%')
-- 37

create table valami(n�v varchar(50))
insert valami values('SANYI')
insert valami values('15%')
select * from valami

select * from valami
  where n�v like '%'+CHAR(37)+'%'

select * from valami
  where n�v like '%[%]%'

select * from CIKK
where VTSZ like '%[^8]%'

select * from CIKK
where VTSZ like '[^8]%'

select * from CIKK
where VTSZ like '[^88]%'

select * from CIKK
where VTSZ like '[^8][^8]%'

select * from CIKK
order by vtsz

select * from valami

select * from valami
  where charindex('%',n�v)> 1