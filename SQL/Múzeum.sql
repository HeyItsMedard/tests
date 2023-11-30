use sopron2024

--1. Hozzuk létre a MUZEUM adatbázist!
--  2. Hozzuk létre a SZEMELY és a MUTARGY táblát!
--  3. Vigyük fel a SZEMELY és a MUTARGY táblákban az adatokat! 


CREATE TABLE SZEMELY (
    NEV NVARCHAR(16),
    VAROS NVARCHAR(15),
    ADOMANY NVARCHAR(20),
    DATUM DATE
);


INSERT INTO SZEMELY (NEV, VAROS, ADOMANY, DATUM)
VALUES
('Benjamin Jones', 'New York', 'készpénz', '1975-01-01'),
('Daniel Smith', 'Boston', 'Argenteuil', '1979-03-05'),
('Roger Black', 'Amsterdam', 'Éjszakai õrjárat', '1985-04-04'),
('Charles Jones', 'San Diego', 'készpénz', '1976-09-18'),
('Zodiac Fischer', 'Seattle', 'készpénz', '1969-10-01'),
('Robert Browne', 'Chicago', 'Dávid', '1980-09-02'),
('Bill Fox', 'Chicago', 'készpénz', '1984-04-03'),
('David Bario', 'Oshkosh', 'Gondolkodó', '1977-02-28'),
('Lawrence Walters', 'Oshkosh', 'készpénz', '1986-09-09');

CREATE TABLE MUTARGY (
    ALKOTO NVARCHAR(15),
    MUCIM NVARCHAR(20),
    HELY NVARCHAR(15),
    ERTEKE NUMERIC
);

INSERT INTO MUTARGY (ALKOTO, MUCIM, HELY, ERTEKE)
VALUES
('Rodin', 'Gondolkodó', 'kölcsön', 338000),
('Michelangelo', 'Dávid', 'kölcsön', 967000),
('Ticiano', 'Madonna', 'kölcsön', 134000),
('Bosch', 'Kísértés', 'restaurálás', 100000),
('El Greco', 'Feltámadás', 'restaurálás', 205000),
('Coreggio', 'Madonna', 'restaurálás', 760000),
('Rembrandt', 'Danae', 'restaurálás', 950000),
('Rembrandt', 'Éjszakai őrjárat', 'kiállítva', 1200000),
('Renoir', 'Le Dejeuner', 'kiállítva', 650000),
('Cezanne', 'Baigneuses', 'kiállítva', 230000),
('Monet', 'Londoni Parlament', 'kiállítva', 256000),
('Monet', 'Impresszió', 'kiállítva', 280000),
('Monet', 'Argenteuil', 'kiállítva', 300000),
('Hals', 'Archers Banquet', 'kiállítva', 500000),
('Gainsborough', 'Blue Boy', 'kiállítva', 420000);


-- 4. Ellenőrizzük a táblák felvitelét! Egy-egy lekérdezés mindkét táblára!
select * from SZEMELY
select * from MUTARGY
-- 5. Listázzuk ki a MUTARGY táblát ALKOTO szerint növekvő sorrendben!
select * from MUTARGY
order by ALKOTO asc

-- 6. Listázzuk ki a SZEMELY táblában lévő személyeket neveit csökkenő sorrendben!
select NEV from SZEMELY
	order by NEV asc

-- 7. Módosítsuk a SZEMELY táblában Charles Jones nevét Jones Charles-ra!
update SZEMELY
	set NEV = 'Jones Charles'
	where NEV = 'Charles Jones'

-- 8. Töröljük ki Hals Archers Banquet alkotását a MUTARGY táblából (ugyanis ellopták)!
delete from MUTARGY
	where MUCIM = 'Archers Banquet'

--9.-10. Listázzuk ki a (különböző) városokat a SZEMELY táblából!
select distinct VAROS from SZEMELY

--11. Listázzuk ki az M betűvel kezdődő alkotók neveit!
select distinct ALKOTO from MUTARGY
where SUBSTRING(ALKOTO, 1,1) = 'M'
--where left(Alkoto, 1) = 'M'

-- 12. Listázzuk ki azokat az alkotókat, akiknek a nevében szerepel o betű!
select distinct ALKOTO from MUTARGY
where CHARINDEX('o', ALKOTO) > 0

--13. Listázzuk ki a 100 000 és 500 000 dollár közötti alkotások alkotóját, címét és értékét! 
select ALKOTO, MUCIM, ERTEKE FROM MUTARGY
where ERTEKE between 100000 and 500000
--14. Mire volt kíváncsi az alábbi kérdező! Fogalmazd meg értelmes magyar mondattal!
--	SELECT MUCIM FROM MUTARGY 
--		WHERE ERTEKE > 200 000 AND ALKOTO ='MONET';
-- Válasz: Monet egyik műcímért akarta tudni, aminek az értéke magasabb volt mint 200 ezer dollár.

--15. Ki az alkotója Roger Black adományának!
select ALKOTO from MUTARGY, SZEMELY
	where SZEMELY.ADOMANY = MUTARGY.MUCIM 
	and SZEMELY.NEV = 'Roger Black'

select * from MUTARGY where ALKOTO = 'Rembrandt'

select adomany, mucim from SZEMELY, MUTARGY -- áh, nálam vmiért Éjszakai orjárat van adomany oszlopban...

SELECT M.ALKOTO
FROM MUTARGY M
JOIN SZEMELY S ON M.MUCIM = S.ADOMANY
WHERE M.ALKOTO = 'Roger Black';

--16. Kiknek az alkotásai drágábbak Cezanne alkotásánál?
select distinct(ALKOTO) from MUTARGY
	where ERTEKE > (select ERTEKE from MUTARGY where ALKOTO = 'Cezanne')

--17. Mennyi a múzeumban található műtárgyak összértéke?
select sum(Erteke) from MUTARGY

--18. Ki adományozta a legdrágább műkincset?
select NEV from SZEMELY
	where ADOMANY in
	(select MUCIM from MUTARGY
		where ERTEKE in
		(select max(Erteke) from MUTARGY, SZEMELY
			where SZEMELY.ADOMANY = MUTARGY.MUCIM))

-- 19. Írassuk ki azoknak az adományozóknak a lakhelyét, akik Rodin mûkincset ajándékoztak!
select SZEMELY.VAROS from SZEMELY, MUTARGY
	where SZEMELY.ADOMANY = MUTARGY.MUCIM
	and MUTARGY.ALKOTO = 'Rodin'

-- 20. Írassuk ki a mûkincsek alkotók szerinti összértékét!
select ALKOTO, sum(ERTEKE) as Összérték from MUTARGY
	group by ALKOTO

-- 21. Írassuk ki a mûkincsek hely szerinti összértékét!
select HELY, sum(Erteke) from Mutargy
	group by Hely

-- 22. Melyik a kiállított alkotások közül a legolcsóbb Monet alkotást?
select MUCIM from MUTARGY
	where HELY = 'Kiállítva' and ERTEKE in
	(select min(ERTEKE) from MUTARGY
		where Alkoto = 'Monet')

-- 23. Adjuk meg az 1985 elõtt készpénzt adományozók neveit! 
select Nev from SZEMELY
	where Adomany = 'Készpénz'

-- 24. Listázzuk ki a Chicagoban vagy New Yorkban lakó adományozók adatait! 
select * from SZEMELY
	where Varos = 'Chicago' or Varos = 'New York'

-- 25. Listázzuk ki az 1 milliónál kisebb értékû mûkincseket alkotó, azon belül érték szerinti csökkenõ sorrendben!
select * from MUTARGY
	where Erteke < 1000000 
	order by Alkoto asc, Erteke desc

-- 26. Hány különbözõ alkotó alkotása szerepel a múzeumban?
select count(distinct(Alkoto)) from MUTARGY
	where Hely = 'Kiállítva'

-- 27. Bõvítsük a MUTARGY táblát egy GALERIA oszloppal!
alter table MUTARGY
add GALERIA nvarchar(1)
-- drop column GALERIA to remove

--28. Állítsuk ki Monet alkotásait a C galériában!
update MUTARGY
set GALERIA = 'C'
where Alkoto = 'Monet' and Hely = 'kiállítva'
select * from MUTARGY

--29. Állítsuk ki a 400 000-nél olcsóbb alkotásokat a B galériában! 
update MUTARGY
set GALERIA = 'B'
where ERTEKE < 400000 and Alkoto != 'Monet' and Hely = 'kiállítva'

--30. A restaurálásról visszatért El Greco alkotást tegyük az A galériába!
update MUTARGY
set GALERIA = 'A'
where Alkoto = 'El Greco' and Hely = 'restaurálás'

--Reset
update MUTARGY
set GALERIA = NULL
