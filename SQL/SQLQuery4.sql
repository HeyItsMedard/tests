-- Totózzunk!
-- 1: elso csapat, 2: masodik csapat, x: döntetlen
-- 1:0		1>0		1
-- 1:1		1=1		x
-- 0:2		0<2		2

-- Üzleti logika implementációja


-- 1. lépés tábla mérkõzések

create table merkozesek(id int, csapatok nvarchar(50), eredmeny char(3))

select * from sys.tables

select * from sys.tables
	where cast(create_date as date) > '2022-03-20'

select * from sys.tables
	where month(create_date) = 3
	and day(create_date) > 10
	and name like 'm%'

select * from merkozesek

insert merkozesek values(1, 'UTE - Fradi', '1:0')
insert merkozesek values(1, 'Liverpool - Manchester', '1:1')
insert merkozesek values(1, 'Leverkusen - Bayern München', '1:2')

insert merkozesek values(1, 'A - B', '5:0')
insert merkozesek values(1, 'C - D', '4:4')
insert merkozesek values(1, 'E - F', '1:6')


-- Totótipp?
-- Lépések:
-- 1. eredmény hazai:vendég
-- 2. elagazas: ha hazai > vendeg 1, ha hazai = vendeg x, ha hazai < vendeg 2

-- (A) merkozesek struktura modositassal
-- (B) uj segedtabla, ugyanabba az adatbazisba
-- (C) masik adatbazis
-- (Ð) feldolgozás idejen a tempdb használjuk
-- (E) memoriaba irom a segedtablat


create table merkozesek2 (id int, csapatok nvarchar(50), eredmeny char(3))

insert merkozesek2 values(1, 'UTE - Fradi', '1:0')
insert merkozesek2 values(1, 'Liverpool - Manchester', '1:1')
insert merkozesek2 values(1, 'Leverkusen - Bayern München', '1:2')

insert merkozesek2 values(1, 'A - B', '5:0')
insert merkozesek2 values(1, 'C - D', '4:4')
insert merkozesek2 values(1, 'E - F', '1:6')


-- (A) 

alter table merkozesek2 add gol1 int, gol2 int
select * from merkozesek2

update merkozesek2 set gol1 = cast(left(eredmeny, 1) as int)
update merkozesek2 set gol1 = convert(int, left(eredmeny,1))

update merkozesek2 set gol2 = cast(right(eredmeny, 1) as int)


-- Lemásolni:
-- 1. csinalunk egy az eredetivel azonos fejlécû táblát 
--		insert merkozesek3 select * from merkozesek2

-- 2. select * into merkozesek4 from merkozesek2
-- 3. 


select *, 
	case 
		when gol1 > gol2 then '1'
		when gol1 < gol2 then '2'
		when gol1 = gol2 then 'x'
	end [helyestipp]
	from merkozesek2

select *, iif(gol1 > gol2, '1',
		  iif(gol1 = gol2, 'x', '2'))
	[helyestipp]
	from merkozesek2


-- alter table merkozesek2 drop column gol1, gol2

-- (B)

select *, cast(left(eredmeny, 1) as int) gol1, cast(right(eredmeny, 1) as int) gol2
	into merkozesek4 from merkozesek

select * from merkozesek4

-- (C)

-- (D)

-- (E) 

declare @toto table (id int, csapatok nvarchar(50), eredmeny char(3), gol1 int, gol2 int)
insert @toto

select *, cast(left(eredmeny, 1) as int) gol1, cast(right(eredmeny, 1) as int) gol2
	from merkozesek

select * from @toto

select *, 
	case 
		when gol1 > gol2 then '1'
		when gol1 < gol2 then '2'
		when gol1 = gol2 then 'x'
	end [helyestipp]
	from @toto



select *, 
	case 
		when gol1 > gol2 then '1'
		when gol1 < gol2 then '2'
		when gol1 = gol2 then 'x'
	end [helyestipp]
	from (
	select *, cast(left(eredmeny, 1) as int) gol1, cast(right(eredmeny, 1) as int) gol2
	from merkozesek) T


-- CTE 

with Toto(id, csapatok, eredmeny, gol1, gol2) as
	(select *, cast(left(eredmeny, 1) as int) gol1, cast(right(eredmeny, 1) as int) gol2
		from merkozesek)
	select *, 
		case 
		when gol1 > gol2 then '1'
		when gol1 < gol2 then '2'
		when gol1 = gol2 then 'x'
	end [helyestipp]
	from Toto



