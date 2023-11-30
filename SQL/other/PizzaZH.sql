use Pizza

CREATE TABLE Hely (HelyID int, HelyNév nvarchar(50), Cim nvarchar(50), 
  Cegvezeto nvarchar(35), Hazhoz bit, Telefon nvarchar(15))

INSERT Hely VALUES 
(1,'Pizza Hut','Moszkva tér 6.','Szolnoki Péter',1,'2499-602'),
(2,'Pizza Pronto','Hollán E. u. 9.','Kiss Balázs',1,'3003-206'),
(3,'Don Pepe','Szemere u. 4.','Nagy Ferenc',0,'3264-135'),
(4,'Tom pizzeriája','Petõfi S. u. 47.','Morvai Tamás',1,'2967-194'),
(5,'Náncsi néni pizzeriája','Nagyszõlõsi út 32/b','Náncsi néni',0,'06-28-240-420'),
(6,'Szeged Pizza','Fõ u. 10.','Lantos Gábor',1,'3456-789'),
(7,'Luigi Pizzeria','Ady E. u. 142.','Fehér Lajos',1,'3572-133')

SELECT * FROM Hely

CREATE TABLE Pizza (PizzaID int, PizzaNév nvarchar(20), Inyencseg nvarchar(20),
 SutesiIdo tinyint)

--TRUNCATE TABLE Pizza

INSERT Pizza VALUES
(1,'Hawaii', 'sonka',30),
(2,'gombás', 'gomba',20),
(3,'halas', 'tonhal',10),
(4,'négy évszak','zöldborsó',28),
(5,'sima','ketchup',17)

SELECT * FROM Pizza

CREATE TABLE Pizza_Hely (PizzaID int, HelyID int, Atmero tinyint, Ar smallint)

INSERT Pizza_Hely VALUES
(1, 1, 25, 1670),
(2, 1, 25, 1720),
(2, 2, 24, 1565),
(3, 3, 30, 1890),
(4, 3, 32, 1700),
(1, 3, 32, 1740),
(5, 4, 30, 1500),
(5, 5, 32, 1575),
(4, 6, 29, 1680),
(3, 6, 27, 1940),
(5, 7, 30, 1690)

SELECT * FROM Pizza_Hely


--1. Melyek azok a pizzák, amelyek nevében és ínyencségében is szerepel a betû?
--(A) A feladatot stringkezelõ függvénnyel

select PizzaNév from Pizza
	where charindex('a', PizzaNév, 1) > 0 and charindex('a', Inyencseg, 1) > 0

--(B) A feladatot LIKE operátor használatával oldd meg!

select Pizzanév from Pizza
	where PizzaNév like '%a%' and Inyencseg like '%a%'

--2. Mi a neve a legrövidebb sütési idejû pizzának?
--(A) A feladatot subquery használatával oldd  meg!

select Pizzanév from Pizza 
	where SutesiIdo = (select min(SutesiIdo) from Pizza)

WITH Legrovidebb(Rovid)
AS
(SELECT MIN(SutesiIdo) FROM Pizza)

SELECT PizzaNév FROM Pizza 
	WHERE SutesiIdo = (SELECT Rovid FROM Legrovidebb)

--(B) A feladat megoldása során csak egyszer használd a FROM kulcsszót!

SELECT TOP 1 PizzaNév FROM Pizza ORDER BY SutesiIdo ASC

--3. Mely pizzák cm-ben megadott átmérõje páratlan? A listán a pizza neve és átmérõje mm-ben szerepeljen! Használj oszlop aliast!

select p.Pizzanév, h.Atmero * 10 as [Atmero(mm)] from Pizza p
	inner join Pizza_Hely h on p.PizzaID = h.PizzaID
	where h.Atmero % 2 = 1
 
--4. Add meg az egyes pizzák átlagárát!Az átlag számítás során pontos értékekkel számolj, de az eredményt egész pontossággal add meg!
--(A) név szerint

select p.Pizzanév, avg(h.Ar) as [Átlagár] from Pizza_hely h
	inner join Pizza p on h.PizzaID = p.PizzaID
	group by p.Pizzanév

--(B) átmérõ szerint

select Atmero, avg(Ar) as [Átlagár] from Pizza_hely 
	group by Atmero

--(C) név és átmérõ szerint

select p.Pizzanév, h.Atmero, avg(h.Ar) as [Átlagár] from Pizza_hely h
	inner join Pizza p on h.PizzaID = p.PizzaID
	group by p.Pizzanév, h.Atmero

--5. Mely pizzázó hely(ek)nek a legkisebb a pizza kínálata? Írasd ki a hely(ek) nevét ABC növekvõ sorrendben!

--(A) subquery használatával

select HelyNév from Hely 
	where HelyID in 
		(select HelyID as Minimum from Pizza_hely
			group by HelyID
			having count(PizzaID) = 1)

  SELECT HelyNév FROM Hely WHERE HelyID IN
  (SELECT TOP 1 WITH TIES HelyID FROM Pizza_Hely
    GROUP BY HelyID 
     ORDER BY COUNT(*) ASC
	 )
   ORDER BY HelyNév

--(B) CTE használatával

 WITH T(HelyID, darab)
  AS
   (SELECT HelyID, COUNT(*) darab FROM Pizza_Hely
    GROUP BY HelyID 
	 )
 SELECT HelyNév FROM Hely WHERE HelyID IN
  (SELECT HelyID FROM T WHERE darab = (SELECT MIN(darab) FROM T))
  ORDER BY HelyNév


--(C) INNER JOIN használatával

select h.HelyNév, count(ph.PizzaID) as Darab from Hely h
	inner join Pizza_hely ph on h.HelyID = ph.HelyID
	group by h.HelyNév
	having count(Darab) = 1
	order by h.HelyNév asc

SELECT * FROM	
 (SELECT TOP 1 WITH TIES HelyNév FROM Hely H INNER JOIN Pizza_Hely PH
   ON H.HelyID = Ph.HelyID 
    GROUP BY H.HelyNév
      ORDER BY COUNT(*) ASC) T
  ORDER BY HelyNév ASC

--6. A modern kor szelleméhez alkalmazkodva
--    Náncsi néni pizzériájából is lehet kérni házhoz szállítást 
--    Módosítsd a megfelelõ táblát a megfelelõ értékkel!

update Hely
set Hazhoz = 1
	where HelyID = 5

--7. Készítsd el az a lekérdezést, mely az eredeti összefoglaló táblázat struktúrájú  tíz oszlopos táblát adja ereményül!

select h.HelyNév, p.PizzaNév, ph.Atmero, h.Cim, h.Cegvezeto, h.Hazhoz, ph.Ar, h.Telefon, p.Inyencseg, p.SutesiIdo from Pizza p
	inner join Pizza_hely ph on p.PizzaID = ph.PizzaID
	inner join Hely h on h.HelyID = ph.HelyID

--8. Van-e olyan cégvezetõ, aki egynél több pizzériát vezet?

select h.Cegvezeto from Hely h, Pizza_hely ph
	where h.HelyID = ph.HelyID
	group by h.Cegvezeto
	having count(ph.HelyID) > 1

--9. Melyikbõl van több páratlan vagy páros házszámú pizzériából?
--    Feltétel: a házszám az utolsó szóköztól a cim végi pontig, vagy perjelig terjed
--     nincs Október 23. u. 19
--     de lehet Arany János utca 19/A
--    Ha kell készíts temporary táblát akár az eredeti adatbázisban
--     akár a tempdb-ben, akár memóriában!
--     A tesztelhetõség miatt a feladatot több lépésben oldd meg!
--      Ha már nagyon kész vagy, elgondolkodhatsz, hogy lehetne egy 
--             komplex CTE lekérdezéssel megoldani...
--     Ha már nagyon kész vagy, gondolkodj tárolt eljárással történõ megoldáson!

create table Cim(Cimek varchar(50))
insert into Cim(Cimek)
	values 
	('Moszkva tér 6.'),
	('Hollán E. u. 9.'),
	('Szemere u. 4.'),
	('Petõfi S. u. 47.'),
	('Nagyszõlõsi út 32/b'),
	('Fõ u. 10.'),
	('Ady E. u. 142.')

select Cim into Cimek 
	from Hely

update Cim
	set Cimek =  trim('/.abcd' from substring(Cimek, PATINDEX('%[0-9]%', Cimek), len(Cimek))) from Cim

update Cim
	set Cimek = cast(Cimek as int)

select * from Cim

if ((select count(Cimek) from Cim where Cimek % 2 = 1) > (select count(Cimek) from Cim where Cimek % 2 = 0))
	select 'Páratlan'
else 
	select 'Páros'

--10. Kell-e a Ligának rendkívüli gyûlést összehívnia?
