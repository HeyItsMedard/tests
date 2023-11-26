
CREATE DATABASE medard

-- 2. Írassa ki azoknak a vevõknek a címét, 
-- és a számlavezetõ bankjuknak a megnevezését, 
-- akiknek telephelye vidéken van, 
-- és nem az OTP-nél vezetik a számlájukat.

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
  where VAROS = 'Kaposvár'
     or VAROS = 'Miskolc'
	 or VAROS = 'Sopron'
	 or VAROS = 'Szombathely'

SELECT * FROM VEVO
  where VAROS in ('Kaposvár','Miskolc',
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
	when BANKJEL = 'KHB' then 'Kereskedelmi és HitelBank'
	end as [Bank megnevezése]
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
	  IIF(bankJEL = 'KHB','Kereskedelmi és HitelBank',
	      'nem tudom'))
	 as [Bank megnevezése]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

CONCAT  overload
  olyan metódus  több féle képpen
  két paraméter
  három paraméter
  négy paraméter

SELECT CONCAT(IRANYITOSZAM,' ',VAROS,' ',UTCAHAZ) as cim,
    IIF(bankjel = 'BB','Budapest Bank',
	  IIF(bankJEL = 'KHB','Kereskedelmi és HitelBank',
	      'nem tudom'))
	 as [Bank megnevezése]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

select ASCII(' ')
select CHAR(32)

SELECT CONCAT(IRANYITOSZAM,CHAR(32),VAROS,CHAR(32),UTCAHAZ) as cim,
    IIF(bankjel = 'BB','Budapest Bank',
	  IIF(bankJEL = 'KHB','Kereskedelmi és HitelBank',
	      'nem tudom'))
	 as [Bank megnevezése]
     FROM VEVO
  where (VAROS != 'Budapest') and
        (BANKJEL != 'OTP')

-- 3. Milyen különbözõ bankok vezetik a vevõk számláit?
SELECT distinct bankjel from vevo

SELECT distinct bankjel 
 as [Milyen különbözõ bankok vezetik a vevõk számláit?]
from vevo

SELECT bankjel from vevo
group by bankjel

SELECT bankjel 
 as [Milyen különbözõ bankok vezetik a vevõk számláit?]
 from vevo
group by bankjel

-- 4. Van-e olyan rendelési tételsor, 
--  ahol a határidõ nem lett megadva?

-- eldöntendõ  van/nincs   igen/nem

select * from rtetel

select * from rtetel
 where HATARIDO  IS  NULL

select COUNT(*) from rtetel
 where HATARIDO  IS  NULL

if 
 (select COUNT(*) from rtetel
   where HATARIDO  IS  NULL) = 0
 select 'NINCS' AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]
 else
 select 'VAN' AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]

 if 
 EXISTS (select * from rtetel
   where HATARIDO  IS  NULL) 
 select 'VAN' AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]
 else
 select 'NINCS' AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]


 
select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN')

select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN') 
  AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]
 
 select 
 iif(
  (select COUNT(*) from rtetel where HATARIDO  IS  NULL) = 0,
   'NINCS','VAN') 
  AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]

  select 
 iif(
  (Exists (select COUNT(*) from rtetel where HATARIDO  IS  NULL)),
   'VAN','NINCS') 
  AS [Van-e olyan rendelési tételsor, ahol a határidõ nem lett megadva?]



-- 4.b. Van-e olyan rendelési tételsor, 
--  ahol a teljesítési dátum nem lett megadva?

if 
 (select COUNT(*) from rtetel
   where TDATUM  IS  NULL) = 0
 select 'NINCS' AS [Van-e olyan rendelési tételsor, ahol teljesítési dátum nem lett megadva?]
 else
 select 'VAN' AS [Van-e olyan rendelési tételsor, ahol teljesítési dátum nem lett megadva?]


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
 -- Van-e a vevõk között olyan, 
 -- akiknek a telephelye téren van? 
 -- igen, irassa ki a nevét és a címét.

 select * from vevo

 select * from vevo
 where utcahaz like '%tér%'

  select * from vevo
 where utcahaz like '% tér %'

 select * from vevo
 where utcahaz like '%'+CHAR(32)+'tér'+CHAR(32)+'%'

  select * from vevo
 where utcahaz like '%  tér %'

 if
 exists (select * from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %')
	-- then nincs   igaz ág
 select VEVONEV, 
   IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %'
	else
	 select 'nincs'   
	  as [Van-e a vevõk között olyan, akiknek a telephelye téren van? ]

-- select eredményét tegyük el
--    tábla
--       fizikailag adatbázisban
--        melyik  saját  Sopron2024   tempdb
--       változóban
--       memóriában 


select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
into mzperx from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %'

if
 exists (select * from mzperx)
	-- then nincs   igaz ág
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from mzperx
	else
	 select 'nincs'  

drop table mzperx

--
-- temporary table megoldás
select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
into #mzperx from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %'

if
 exists (select * from #mzperx)
	-- then nincs   igaz ág
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from #mzperx
	else
	 select 'nincs'  

--	 # kilépek Query windows  automatikusan törlõdnek
-- NEM KELL: drop table #mzperx


-- memóriában dolgozik
-- select into @változó  NINCS
-- tábla létrehozás, fejléc, adattípus
declare @sajáttábla table
  (
  VEVONEV nvarchar(30),
  IRANYITOSZAM nvarchar(4),
  VAROS nvarchar(15),
  UTCAHAZ nvarchar(20)
  )

insert @sajáttábla
select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
  from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %'

if
 exists (select * from @sajáttábla)
	-- then nincs   igaz ág
 select VEVONEV, IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from @sajáttábla
	else
	 select 'nincs'  

@sajáttábla változó  lokális
 automatikusan törlõdik  értéke
 deallokál

-- subquery
if select T.IRANYITOSZAM +T.VAROS+T.UTCAHAZ  as cim
(select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
  from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %') T


if exists(select * from T)
   select T.IRANYITOSZAM +T.VAROS+T.UTCAHAZ  as cim
   from 
   (select VEVONEV, IRANYITOSZAM,VAROS,UTCAHAZ 
    from vevo
    where utcahaz like '% tér %'
     or utcahaz like '% tere %') T
else
  select 'nincs'

-- CTE  common table expressions
WITH
SELECT

ld. késõbb november 3.

--
select * from vevo
 where (charindex(' tér ',utcahaz) > 0) or
       (charindex(' tere ',utcahaz) > 0)
  
 select utcahaz, REPLACE(utcahaz,' tér ','') from VEVO

 select * from vevo
 where (len(utcahaz) -
   len(REPLACE(utcahaz,' tér ','')) > 0)


select * from vevo
 where (len(utcahaz) -
   len(REPLACE(utcahaz,' tér ','')) > 0)  or
   (len(utcahaz) -
   len(REPLACE(utcahaz,' tere ','')) > 0)

-- 
-- 6. Írassa ki azoknak a vevõknek a kódját és nevét, 
-- akiknek a neve "k" betûvel kezdõdik!

   like 'k%'
   left (vevonev,1) = 'k'
   charindex('k',vevonev)=1
   substring(vevonev,1,1) = 'k'
   vevonev > 'JZZZZZZZ' and vevonev < 'LAAAAAAA'
   vevonev >= 'KAaaaaaaaaaaa' and vevonev <= 'KZZZZZZZ'

   -- 7. Írassa ki azoknak a palack vagy üveg 
   -- mennyiségi egységû termékeknek a cikkszámát, 
   -- megnevezését, mennyiségi egységét és vámtarifaszámát, 
   -- melyeknek a vámtarifaszáma nem '88'-al kezdõdik.

   select * from cikk

   select * from cikk
     where MEGYSEG = 'PALACK' or MEGYSEG='ÜVEG'

	 select * from cikk
     where MEGYSEG in ('PALACK','ÜVEG')


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
     where (MEGYSEG = 'PALACK' or MEGYSEG='ÜVEG')
	   and  not vtsz like '88%' 

select * from
(select * from cikk
   where (MEGYSEG = 'PALACK' or MEGYSEG='ÜVEG')) T 
   where not T.vtsz like '88%' 


select cikkszam, megnevezes, 
       megyseg, vtsz
	   from cikk
     where (MEGYSEG = 'PALACK' or MEGYSEG='ÜVEG')
	   and  not vtsz like '88%' 

--
select cikkszam, megnevezes, 
       megyseg, vtsz
	   from cikk
     where MEGYSEG in ('PALACK','ÜVEG')
	   and not vtsz like '88%' 

select ASCII('%')
-- 37

create table valami(név varchar(50))
insert valami values('SANYI')
insert valami values('15%')
select * from valami

select * from valami
  where név like '%'+CHAR(37)+'%'

select * from valami
  where név like '%[%]%'

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
  where charindex('%',név)> 1