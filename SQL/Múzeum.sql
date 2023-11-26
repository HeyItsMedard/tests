use Múzeum

-- 2.
create table Személy (Nev nvarchar(16), Varos nvarchar(15), Adomany nvarchar(16), Datum date)
create table Mûtárgy (Alkoto nvarchar(15), Mucim nvarchar(20), Hely nvarchar(15), Erteke int)

-- 4.
select * from Személy
select * from Mûtárgy

-- 5.
select * from Mûtárgy
	order by Alkoto asc

-- 6.
select Nev from Személy
	order by Nev asc

-- 7.
update Személy
	set Nev = 'Jones Charles'
	where Nev = 'Charles Jones'

select * from Személy

-- 7. +

-- 8.
select * from Mûtárgy
	where Mucim = 'Archers Banquet'

delete from Mûtárgy 
	where Mucim = 'Archers Banquet'

-- 9.
select Varos from SZemély

-- 10. 
select distinct(Varos) from SZemély

-- 11.
select distinct(Alkoto) from Mûtárgy
	where left(Alkoto, 1) = 'M'

-- 12.
select distinct(Alkoto) from Mûtárgy
	where charindex('o', Alkoto) > 0

-- 13.
select Alkoto, Mucim, Erteke from Mûtárgy
	where Erteke between 100000 and 500000

-- 14. Listázzuk ki Monet alkotásainak címét, ahol a mû értéke nagyobb, mint 200.000 dollár!
select Mucim from Mûtárgy
		where Erteke > 200000 and Alkoto ='MONET'

-- 15. Ki az alkotója Roger Black adományának!
select Alkoto from Mûtárgy, Személy
	where Mûtárgy.Mucim = Személy.Adomany
	and Személy.Nev = 'Roger Black'

-- 16. Kiknek az alkotásai drágábbak Cezanne alkotásánál?
select distinct(Alkoto) from Mûtárgy
	where Erteke > (select Erteke from Mûtárgy where Alkoto = 'Cezanne')

-- 17. Mennyi a múzeumban található mûtárgyak összértéke?
select sum(Erteke) from Mûtárgy

-- 18. Ki adományozta a legdrágább mûkincset?
select Nev from Személy
	where Adomany in
	(select Mucim from Mûtárgy
		where Erteke in
		(select max(Erteke) from Mûtárgy))

-- 19. Írassuk ki azoknak az adományozóknak a lakhelyét, akik Rodin mûkincset ajándékoztak!
select Személy.Varos from Személy, Mûtárgy
	where Személy.Adomany = Mûtárgy.Mucim
	and Mûtárgy.Alkoto = 'Rodin'

-- 20. Írassuk ki a mûkincsek alkotók szerinti összértékét!
select Alkoto, sum(Erteke) from Mûtárgy
	group by Alkoto

-- 21. Írassuk ki a mûkincsek hely szerinti összértékét!
select Hely, sum(Erteke) from Mûtárgy
	group by Hely

-- 22. Melyik a kiállított alkotások közül a legolcsóbb Monet alkotást?
select Mucim from Mûtárgy
	where Hely = 'Kiállítva' and Erteke in
	(select min(Erteke) from Mûtárgy
		where Alkoto = 'Monet')

-- 23. Adjuk meg az 1985 elõtt készpénzt adományozók neveit! 
select Nev from Személy
	where Adomany = 'Készpénz'

-- 24. Listázzuk ki a Chicagoban vagy New Yorkban lakó adományozók adatait! 
select * from Személy
	where Varos = 'Chicago' or Varos = 'New York'

-- 25. Listázzuk ki az 1 milliónál kisebb értékû mûkincseket alkotó, azon belül érték szerinti csökkenõ sorrendben!
select * from Mûtárgy
	where Erteke < 1000000 
	order by Alkoto asc, Erteke desc

-- 26. Hány különbözõ alkotó alkotása szerepel a múzeumban?
select count(distinct(Alkoto)) from Mûtárgy
	where Hely = 'Kiállítva'

-- 27. Bõvítsük a MUTARGY táblát egy GALERIA oszloppal!
alter table Mûtárgy
add Galéria nvarchar(1)

-- 28. Állítsuk ki Monet alkotásait a C galériában!
update Mûtárgy
set Galéria = 'C'
where Alkoto = 'Monet' and Hely = 'kiállítva'

-- 29. Állítsuk ki a 400 000-nél olcsóbb alkotásokat a B galériában! 
update Mûtárgy
set Galéria = 'B'
where Erteke < 400000 and Alkoto != 'Monet' and Hely = 'kiállítva'

-- 30. A restaurálásról visszatért El Greco alkotást tegyük az A galériába!
update Mûtárgy
set Hely = 'kiállítva', Galéria = 'A'
where Alkoto = 'El Greco'
