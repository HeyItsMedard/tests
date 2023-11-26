lekérdezés

SELECT * FROM tábla

-- CTE
Common table expression

create table foci(csapatok nvarchar(50), 
                  eredmény char(3))

insert foci values('Liverpool - Manchester','1:0')
insert foci values('UTE - Fradi','1:2')
insert foci values('AA - BB','0:0')

select * from foci

helyes totótipp
elõtt van : után      1

select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
	   from foci

select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
	   into segédtábla
	   from foci

select * from segédtábla

select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestotótipp			  
   from segédtábla

drop table segédtábla

select * from tábla   <--  fizikai létezõ

select * from 
(select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
 from foci) as [Tom Cruise]


 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestotótipp
	   from
(select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
 from foci) as [Tom Cruise]

 -- "elõre tenni"

with [Tom Cruise]
as
 (select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
 from foci)  
 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestotótipp
	   from
	    [Tom Cruise]

--
go
--
with golok
as
 (select cast(left(eredmény,1) as int) as gol1,
       cast(right(eredmény,1) as int) as gol2
 from foci)  
 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestotótipp
	   from
	    golok

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

go
--
https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver16


with ter
as
(select * from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %')
if exists (select * from ter)
  select VEVONEV, 
   IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim
   from ter
else
  select 'nincs'

with ter
as
(select * from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %')
select iif(exists(select * from ter),'van','nincs')

with ter
as
(select * from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %')
select 
  iif(exists(select * from ter),
    (select * from ter)
	,'nincs')

Msg 116, Level 16, State 1, Line 135
Only one expression can be specified 
in the select list when the subquery 
is not introduced with EXISTS.

multiple CTE

with ter
as
(select * from vevo
 where utcahaz like '% tér %'
    or utcahaz like '% tere %'),
eredmeny
as
(select VEVONEV, 
   IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim from ter)
select * from eredmeny
  