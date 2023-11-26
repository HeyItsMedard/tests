55. A cikksz�m �s megnevez�s felt�ntet�s�vel �rassa ki, 
hogy az egyes term�kekb�l mely napokon kell sz�ll�tani.

select * from cikk

select * from rendeles

select * from rtetel
hatarido -- cikkszam

select hatarido from rtetel where cikkszam in
 (select cikkszam from cikk)

select * from rtetel R,cikk C
  where R.cikkszam = C.cikkszam

select C.cikkszam, C.megnevezes, R.hatarido
  from rtetel R,cikk C
     where R.cikkszam = C.cikkszam

select C.cikkszam, C.megnevezes, R.hatarido
  from rtetel R CROSS JOIN cikk C
     where R.cikkszam = C.cikkszam

select C.cikkszam, C.megnevezes, R.hatarido
  from rtetel R INNER JOIN cikk C
     ON R.cikkszam = C.cikkszam

--
54. �rassa ki a vid�ki vev�k megrendel�seinek adatait. 
A t�telsorokat nem kell ki�ratni. 
A feladatot a t�bl�zatok �sszekapcsol�s�val oldja meg.

select * from vevo
 where varos <> 'Budapest'

select * from rendeles

select R.* from vevo V, rendeles R

select R.* from vevo V, rendeles R
  where V.vevokod = R.vevokod
   and V.VAROS != 'Budapest'

select R.* from vevo V CROSS JOIN rendeles R
  where V.vevokod = R.vevokod
   and V.VAROS != 'Budapest'

select R.* from vevo V INNER JOIN rendeles R
  ON V.vevokod = R.vevokod
   where V.VAROS != 'Budapest'

-- 53. �rassa ki a budapesti vev�k �ltal rendelt, 
-- darab, vagy csomag mennyis�gi egys�g term�kek 
-- rendel�si t�teleit. 
-- A feladatot alk�rd�s-->subquery haszn�lat�val oldja meg. 
-- Az eredm�ny rendel�ssz�m szerint, 
-- azon bel�l cikksz�m szerint n�vekv� sorrendbe 
-- rendezett legyen!


select * from rtetel
select * from cikk 
   where megyseg = 'darab' or megyseg='csomag'
select * from vevo where varos = 'Budapest'

select rendelesszam from rendeles
 where vevokod = 
   (select  vevokod
      from vevo where varos = 'Budapest')

select rendelesszam from rendeles
 where vevokod in
   (select  vevokod
      from vevo where varos = 'Budapest')

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

-- 52. �rassa ki a budapesti vev�k �ltal rendelt, 
-- darab, vagy csomag mennyis�gi egys�g  
-- term�kek rendel�si t�teleit. 
-- A feladatot t�bl�zat �sszekapcsol�s�val oldja meg! 
-- Az eredm�ny rendel�ssz�m szerint, 
-- azon bel�l cikksz�m szerint 
-- n�vekv� sorrendbe rendezett legyen.

select * from vevo V, cikk C, rtetel RT, rendeles R
 where 

 select * from vevo
 V.VEVOKOD

 select * from cikk
 C.CIKKSZAM

 select * from rendeles
 R.VEVOKOD = V.VEVOKOD
 RENDELESSZAM

 select * from rtetel
 RT.CIKKSZAM = C.CIKKSZAM

 select * from vevo V, cikk C, 
     rtetel RT, rendeles R
 where R.VEVOKOD = V.VEVOKOD
      and RT.CIKKSZAM = C.CIKKSZAM
	  and R.RENDELESSZAM = RT.RENDELESSZAM
	  and V.varos = 'Budapest'
	  and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

 select RT.* from vevo V, cikk C, 
     rtetel RT, rendeles R
 where R.VEVOKOD = V.VEVOKOD
      and RT.CIKKSZAM = C.CIKKSZAM
	  and R.RENDELESSZAM = RT.RENDELESSZAM
	  and V.varos = 'Budapest'
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

select RT.* from vevo V inner join rendeles R
     ON R.VEVOKOD = V.VEVOKOD
	 inner join rtetel RT
	 ON R.RENDELESSZAM = RT.RENDELESSZAM
     inner join  cikk C
	 ON RT.CIKKSZAM = C.CIKKSZAM
 where  V.varos = 'Budapest'
	  and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

rekordok sz�ma
szelekt�v
statisztika
Oracle  MS SERVER
query optimizer

-- els� gondolat
select RT.* from vevo V inner join rendeles R
     ON R.VEVOKOD = V.VEVOKOD
	 inner join rtetel RT
	 ON R.RENDELESSZAM = RT.RENDELESSZAM
     inner join  cikk C
	 ON RT.CIKKSZAM = C.CIKKSZAM
 where  V.varos = 'Budapest'
	  and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

--set forceplan on
-- set optimizer off

-- m�sodik gondolat, mi van ha a m�sik t�blakapcsol�s
-- jobb??
select RT.* from rtetel RT
     inner join  cikk C
	 ON RT.CIKKSZAM = C.CIKKSZAM
     inner join rendeles R
     ON R.RENDELESSZAM = RT.RENDELESSZAM
	 inner join  vevo V 
     ON R.VEVOKOD = V.VEVOKOD
 where  V.varos = 'Budapest'
	  and C.megyseg in ('darab','csomag')
order by R.rendelesszam asc, C.cikkszam asc

set forceplan off

-- 51. �rassa ki azon vev�k kisz�ll�tott 
-- rendel�si t�telsorait, akik a Budapest Bankn�l (BB)
--  vezetik sz�ml�jukat. A feladatot alk�rd�s 
-- haszn�lat�val oldja meg.

select * from rtetel
where teljesitve = 1

select * from rendeles
vevokod

select * from vevo
 where bankjel = 'BB'
---- 
select * from rtetel
where teljesitve = 1
 and rendelesszam in
(select rendelesszam from rendeles
   where vevokod in (
      select vevokod from vevo
          where bankjel = 'BB'))

--49. �rassa ki az 1998.03.18.-i megrendel�sek 
-- rendel�si t�teleit! 
-- A feladatot t�bl�zat �sszekapcsol�s�val oldja meg!

select * from cikk

select * from rtetel
 where rendelesszam in
  (select rendelesszam from rendeles where
    datum = '1998-03-18')

select * from rendeles

  datetime
 
-- rendezetts�g
-- rekordsz�m
-- eloszl�s, distribution
-- szelektivit�s

select * from rtetel
 where rendelesszam in
  (select rendelesszam from rendeles where
    cast(datum as date) = cast('1998-03-18' as date)) 
  
select * from rtetel, rendeles
 where rtetel.rendelesszam  = rendeles.rendelesszam 
   and  cast(datum as date) = cast('1998-03-18' as date)

select * from rtetel cross join rendeles
 where rtetel.rendelesszam  = rendeles.rendelesszam 
   and  cast(datum as date) = cast('1998-03-18' as date)

select * from rtetel inner join rendeles
 on rtetel.rendelesszam  = rendeles.rendelesszam 
   where  cast(datum as date) = cast('1998-03-18' as date)

select * from rtetel RT inner join rendeles R
 on RT.rendelesszam  = R.rendelesszam 
   where  cast(datum as date) = cast('1998-03-18' as date)

--50. �rassa ki az 1998.03.18.-i megrendel�sek 
-- rendel�si t�teleit! 
-- A feladatot alk�rd�s haszn�lat�val oldja meg!

--

--46.  �rassa ki azoknak a vev�knek a k�dj�t, 
--�s nev�t, akik rendeltek 25%-os �fa kulcs� term�ket.  
--A feladatot t�bl�zatok kapcsol�s�val oldja meg! 

--47.  �rassa ki azoknak a vev�knek a k�dj�t, 
--�s nev�t, akik rendeltek 25%-os �fa kulcs� term�ket.  
--A feladatot alk�rd�s haszn�lat�val oldja meg!

select * from rendeles
vevokod
select * from rtetel
cikkszam

select vevokod,vevonev from vevo
 where vevokod in 
 (select vevokod from rendeles where
    rendelesszam in
	(select rendelesszam from rtetel
	  where cikkszam in
	   (select cikkszam from cikk 
	     where afakulcs = 25)))
  
  select * from rtetel

  select  distinct V.vevokod, V.vevonev from cikk C
    inner join rtetel RT
	on C.cikkszam= RT.cikkszam
	inner join rendeles R
	on RT.rendelesszam = R.rendelesszam
	inner join vevo V
	on R.vevokod  = V.vevokod
	where  C.afakulcs =25