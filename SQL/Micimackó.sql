use Micimackó

create table Szeret (Nev nvarchar(50), Mit nvarchar(50))

select * from Szeret

-- 1. Melyek azok a gyümölcsök, amelyeket Micimackó nem szeret? (de valaki más igen) 

select Mit from Szeret
		where Nev = 'Micimackó'

select distinct(Mit) from Szeret
	where Mit not in
	(select Mit from Szeret
		where Nev = 'Micimackó')

-- 2. Kik nem szeretik az almát? (de valami mást igen) 

select distinct(Nev) from Szeret
	where Nev not in
	(select Nev from Szeret
		where Mit = 'alma')

-- 3. Kik szeretik vagy az almát vagy a körtét? 

select distinct(Nev) from Szeret
	where Nev in
	(select Nev from Szeret
		where Mit = 'alma' or Mit = 'körte')

-- 4. Kik szeretik az almát is és a körtét is? 

select distinct(Nev) from Szeret
	where Nev in (select Nev from Szeret where Mit = 'alma')
	and Nev in (select Nev from Szeret where Mit = 'körte')

-- 5. Kik azok, akik szeretik az almát, de nem szeretik a körtét? 

select distinct(Nev) from Szeret
	where Nev in (select Nev from Szeret where Mit = 'alma')
	and Nev not in (select Nev from Szeret where Mit = 'körte')

-- 6. Kik szeretnek legalább kétféle gyümölcsöt? 

select Nev, count(*) [Hány féle gyümit szeret] from Szeret
	group by Nev 
	having count(Mit) >= 2

-- 7. Kik szeretnek legfeljebb kétféle gyümölcsöt? 

select Nev, count(*) [Hány féle gyümit szeret] from Szeret
	group by Nev 
	having count(Mit) <= 2

-- 8. Kik szeretnek minden gyümölcsöt? 

select top 1 Nev, count(Mit) [Hány féle gyümit szeret] from Szeret 
	group by Nev
	order by count(Mit) desc 

select Nev, count(*) as [Hány féle gyümit szeret] from Szeret
	group by Nev
	having count(*) = (select max(fruitcount) from (select Nev, count(Mit) as fruitcount from Szeret group by Nev) Sz)

-- 9. Kik azok, akik pontosan ugyanazokat a gyümölcsöket szeretik, mint Micimackó? 

if exists (
	select Nev, count(Mit) as [Hány féle gyümit szeret] from Szeret
		where Mit in (select Mit from Szeret where Nev = 'Micimackó') 
		and Nev != 'Micimackó'
		group by Nev
		having count(Mit) = (select count(Mit) from Szeret where Nev = 'Micimackó'))

	select Nev, count(Mit) as [Hány féle gyümit szeret] from Szeret
		where Mit in (select Mit from Szeret where Nev = 'Micimackó') 
		and Nev != 'Micimackó'
		group by Nev
		having count(Mit) = (select count(Mit) from Szeret where Nev = 'Micimackó')
else 
	select 'Nincs ilyen' as [Akik pontosan azokat szeretik]

--10. Kik azok, akik legalább azokat a gyümölcsöket szeretik, mint Micimackó?

if exists (
	select Nev, count(Mit) as [Hány féle gyümit szeret] from Szeret
		where Nev in (select Nev from Szeret
			where Mit in (select Mit from Szeret where Nev = 'Micimackó') and Nev != 'Micimackó'
			group by Nev
			having count(Mit) = (select count(Mit) from Szeret where Nev = 'Micimackó'))
		group by Nev)

	select Nev, count(Mit) as [Hány féle gyümit szeret] from Szeret
		where Nev in (select Nev from Szeret
			where Mit in (select Mit from Szeret where Nev = 'Micimackó') and Nev != 'Micimackó'
			group by Nev
			having count(Mit) = (select count(Mit) from Szeret where Nev = 'Micimackó'))
		group by Nev
else
	select 'Nincs ilyen' as [Akik legalább azokat szeretik]
	