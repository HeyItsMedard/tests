
22. Mekkora a darab mennyiségi egység termékeknél 
  a legkisebb, a legnagyobb és az átlagos raktárkészlet? 

select * from cikk

select * from cikk
  where megyseg = 'DARAB'

select min(keszlet) as [legkisebb raktárkészlet] from cikk
  where megyseg = 'DARAB'

select max(keszlet) as [legnagyobb raktárkészlet] from cikk
  where megyseg = 'DARAB'

select avg(keszlet) as [átlagos raktárkészlet] from cikk
  where megyseg = 'DARAB'

---
select min(keszlet) as [legkisebb raktárkészlet] from cikk
  where megyseg = 'DARAB'
union all
select max(keszlet) as [legnagyobb raktárkészlet] from cikk
  where megyseg = 'DARAB'
union all
select avg(keszlet) as [átlagos raktárkészlet] from cikk
  where megyseg = 'DARAB'

 --
 -- string literal
 select 'legkisebb raktárkészlet' as [....], min(keszlet) as  érték
   from cikk
  where megyseg = 'DARAB'
union all
select 'legnagyobb raktárkészlet', max(keszlet)  from cikk
  where megyseg = 'DARAB'
union all
select 'átlagos raktárkészlet', 
  avg(cast(keszlet as real))  from cikk
  where megyseg = 'DARAB'

--
select min(keszlet) as [legkisebb raktárkészlet],   
       max(keszlet) as [legnagyobb raktárkészlet], 
       avg(cast(keszlet as float))
	   as [átlagos raktárkészlet] from cikk
  where megyseg = 'DARAB'

--
select top 1 keszlet as [legnagyobb raktárkészlet] from cikk
  where megyseg = 'DARAB'
    order by keszlet desc

select top 1 keszlet as [legkisebb raktárkészlet] from cikk
  where megyseg = 'DARAB'
    order by keszlet asc

select min(keszlet) as [legkisebb raktárkészlet] from cikk
  where megyseg = 'DARAB'

select sum(keszlet)/count(keszlet) as [átlagos raktárkészlet] 
 from cikk
  where megyseg = 'DARAB'

select sum(cast(keszlet as decimal))/count(keszlet) 
  as [átlagos raktárkészlet] 
   from cikk
     where megyseg = 'DARAB'

---
milyen típusú a KESZLET?

select * from sys.columns

select * from sys.columns
  where name = 'KESZLET'

 type_id   52

 select * from sys.types

 select name from sys.types
   where system_type_id = 52

 select name from sys.types
   where system_type_id =
     (select system_type_id from sys.columns
        where name = 'KESZLET')

--23. Mekkora a legnagyobb értékû raktárkészlet 
--    áfás eladási árral számolva?
select 25/100

select eladasiar, eladasiar*(1+afakulcs/100), keszlet,
  keszlet * eladasiar*(1+afakulcs/100) from cikk

select max(keszlet * eladasiar*(1+afakulcs/100))
 as [legnagyobb értékû raktárkészlet]
   from cikk


select min(keszlet * eladasiar*(1+afakulcs/100))
 as [legnagyobb értékû raktárkészlet]
   from cikk

-- 24. Mekkora a legkisebb és legnagyobb haszon?
haszon = eladasiar - termeloiar
select * from cikk

select eladasiar,termeloiar,
       eladasiar - termeloiar as haszon from cikk

select  min(eladasiar - termeloiar) as legkisebb_haszon ,
        max(eladasiar - termeloiar) as legnagyobb_haszon 
from cikk

-- 25. Mekkora a "Kg' mennyiségi egység termékek 
--    átlagos minimális raktárkészlete?
select * from cikk

select mkeszlet from cikk

select mkeszlet from cikk
  where megyseg = 'kg'

select * from cikk
  where megyseg = 'kg'

select avg(mkeszlet) from cikk
  where megyseg = 'kg'

  58+86 = 144   /2   72

select avg(cast(mkeszlet as real))  as [kérdés 25]
 from cikk
  where megyseg = 'kg'

-- 26

select * from vevo

select 10

select count(*) as [...] from vevo

select * from rendeles

select count(*) as [....] from rendeles

--28. Mekkora értékû a teljes raktárkészlet 
-- termelõi áron számolva?
select keszlet, termeloiar from cikk

select sum(keszlet*termeloiar) as [...] from cikk

-- 29. Hány db különbözõ megrendelésben rendeltek
--  '41773474'-es cikkszámú terméket?

select * from cikk
 where cikkszam = '41773474'

select * from rendeles

select * from rtetel
 where cikkszam = '41773474'

select distinct rendelesszam from rtetel
 where cikkszam = '41773474'

select count (distinct rendelesszam) from rtetel
 where cikkszam = '41773474'

select count(*) from 
(select distinct rendelesszam from rtetel
 where cikkszam = '41773474') T

--
30. Van-e olyan város, ahol a bankok közül legalább egyben, 
legalább két vevõ vezeti a számláját?

select * from vevo

select bankjel, count(*) from vevo
  group by bankjel

select bankjel, varos, count(*) from vevo
  group by bankjel,varos

select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
   having count(*) > 1


if
exists (select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
  having count(*) > 1)
select 'van'  as [....]
else
 select ' nincs' as [....]

select count(*) from
(select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
   having count(*) > 1) T
   
if (select count(*) from
(select bankjel, varos, count(*) db from vevo
  group by bankjel,varos
   having count(*) > 1) T) > 0
select 'van'  as [....]
else
 select ' nincs' as [....]

-- 31. Vámtarifaszámonként hány különbözõ termék van a raktárban?


select * from cikk
-- 69 termék

select vtsz from cikk
 group by vtsz
 -- 38

select vtsz, count(*) db from cikk
 group by vtsz

select vtsz, count(*) db from cikk
 group by vtsz
   order by vtsz

select vtsz, count(*) db from cikk
 group by vtsz
   order by db desc

32. Áfakulcsonként hány különbözõ eladási árú termék van a raktárban?

select afakulcs, count(*) db 
   from cikk  
      group by afakulcs

33. Van-e legalább három olyan termék, 
   amelyeknek a vámtarifaszáma és az áfakulcsa is megegyezik? 
   Írassa ki az ilyen termékek vámtarifaszámát, 
   áfakulcsát, és a darabszámot!

   select vtsz,afakulcs, count(*)
   from cikk
    group by vtsz,afakulcs
	 having count(*) >=3

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


 select * from 
 (select vtsz,afakulcs, count(*) as db
   from cikk
    group by vtsz,afakulcs
	 having count(*) >=3) as ZS

---
declare @atm table(vtsz nvarchar(10), afakulcs float, db int)
insert @atm 
select vtsz,afakulcs, count(*) as db
   from cikk
    group by vtsz,afakulcs
	 having count(*) >=3
if exists (select * from @atm)
 select * from @atm
else
 select 'nincs'
 ---
 
 34 ---


 --47.  Írassa ki azoknak a vevõknek a kódját, és nevét, 
 -- akik rendeltek 25%-os áfa kulcsú terméket. 
 -- A feladatot subquery használatával oldja meg!

 select * from cikk 
  where afakulcs = 25
  -- 69 --> 54
  cikkszam  11111112

  select * from rtetel
   where cikkszam = '11111112'

    rendelesszam

	1/98
	2/98

	select * from rendeles

	select * from vevo

	vevo.vevokod = rendeles.vevokod

	rendeles.rendelesszam = rtetel.rendelesszam

	rtetel.cikkszam = cikk.cikkszam


	select * from vevo where vevokod =
	(select vevokod from rendeles where rendelesszam =
	 (select rendelesszam from rtetel
       where cikkszam = 
         (select cikkszam from cikk 
            where afakulcs = 25)))

select * from vevo where vevokod in
	(select vevokod from rendeles where rendelesszam in
	 (select rendelesszam from rtetel
       where cikkszam in 
         (select cikkszam from cikk 
            where afakulcs = 25)))

select * from cikk, rtetel

select * from cikk, rtetel
  where cikk.cikkszam = rtetel.cikkszam

select * from cikk cross join rtetel
  where cikk.cikkszam = rtetel.cikkszam

select * from cikk inner join rtetel
  on cikk.cikkszam = rtetel.cikkszam

  -- 221

  select * from cikk left join rtetel
  on cikk.cikkszam = rtetel.cikkszam
  -- 222

  select * from cikk right join rtetel
  on cikk.cikkszam = rtetel.cikkszam
  -- 221

  select * from cikk inner hash join rtetel
  on cikk.cikkszam = rtetel.cikkszam

  select * from cikk inner loop join rtetel
  on cikk.cikkszam = rtetel.cikkszam

  select * from cikk inner merge join rtetel
  on cikk.cikkszam = rtetel.cikkszam
