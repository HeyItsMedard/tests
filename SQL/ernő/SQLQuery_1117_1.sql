lek�rdez�s

SELECT * FROM t�bla

-- CTE
Common table expression

create table foci(csapatok nvarchar(50), 
                  eredm�ny char(3))

insert foci values('Liverpool - Manchester','1:0')
insert foci values('UTE - Fradi','1:2')
insert foci values('AA - BB','0:0')

select * from foci

helyes tot�tipp
el�tt van : ut�n      1

select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
	   from foci

select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
	   into seg�dt�bla
	   from foci

select * from seg�dt�bla

select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestot�tipp			  
   from seg�dt�bla

drop table seg�dt�bla

select * from t�bla   <--  fizikai l�tez�

select * from 
(select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
 from foci) as [Tom Cruise]


 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestot�tipp
	   from
(select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
 from foci) as [Tom Cruise]

 -- "el�re tenni"

with [Tom Cruise]
as
 (select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
 from foci)  
 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestot�tipp
	   from
	    [Tom Cruise]

--
go
--
with golok
as
 (select cast(left(eredm�ny,1) as int) as gol1,
       cast(right(eredm�ny,1) as int) as gol2
 from foci)  
 select gol1, gol2,
       case when gol1 > gol2 then '1'
             when gol1 <gol2 then '2'
			 when gol1 = gol2 then 'X'
       end as helyestot�tipp
	   from
	    golok

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

go
--
https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver16


with ter
as
(select * from vevo
 where utcahaz like '% t�r %'
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
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %')
select iif(exists(select * from ter),'van','nincs')

with ter
as
(select * from vevo
 where utcahaz like '% t�r %'
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
 where utcahaz like '% t�r %'
    or utcahaz like '% tere %'),
eredmeny
as
(select VEVONEV, 
   IRANYITOSZAM+' '+VAROS+' '+UTCAHAZ as cim from ter)
select * from eredmeny
  