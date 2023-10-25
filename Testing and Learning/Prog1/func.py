# Köszön a paraméterben megadott embernek
# Paraméterből megadott üzenettel üdvözölje a felhasználót

# def hello(name, message = "Hello"):
#   print(message, name)


# hello('Alice')

# Egy listából összegezzük a számokat egy függvénnyel

# def sum(list):
#   osszeg = 0
#   for number in list:
#     osszeg += number
#   return osszeg

# print(sum([0, 1, 2]))
# print(sum([0, 1, 2, 3, 4, 5, 6]))

# Három bemeneti számból visszaadja a legnagyobbat

# def max(a, b, c):
#   if a > b and a > c:
#     return a
#   if c > b and a < c:
#     return c
#   return b

# print(max(4, 35, 201))

# Ami eldönti, hogy a kapott szám az benne van-e a kapott intervallumban

# def inrange(szam, start, end):
#   if start > end:
#     print('Rossz sorrend')
#   return start <= szam and szam <= end

# print(inrange(13, 0, 12))

# Van két változó a, b és számoljuk a kerületet, területet és írjuk ki őket

# a = 10
# b = 20

# def kerulet(a, b):
#   return (a + b) * 2

# def terulet(a, b):
#   return a * b

# def kiir(a, b):
#   print(kerulet(a, b), terulet(a, b))

# kiir(a, b)

# Írjunk egy függvényt, ami megadja két számról, hogy az előjelük megegyezik-e

# def elojel(a, b):
#   if (a >= 0 and b >= 0) or (b < 0 and a < 0):
#     return True
#   return False

# print(elojel(2, 5))
# print(elojel(10, 0))
# print(elojel(0, -3))
# print(elojel(-2, -3))

# Ami eldönti a kapott évről, hogy szökőév-e
# szökőev: minden 4-edik, nem szököév minden 100-adik, viszont szökőév minden 400-adik
# pl 2000 -> szökőév

# def szokoev(ev):
#   if ev % 400 == 0:
#     return True
#   if ev % 100 == 0:
#     return False
#   if ev % 4 == 0:
#     return True
#   return False

# print(szokoev(2003))
# print(szokoev(2000))
# print(szokoev(2023))

# Ami paraméterül kap egy számot, és erre a számra meghív 2 függvényt
# - harmadik hatvány
# - kiszámolja az abszolút értékét

# def kob(szam):
#   return szam ** 3

# def abszolut(szam):
#   if szam < 0:
#     return szam * -1
#   return szam

# def fgv(szam):
#   print(kob(szam), abszolut(szam))

# fgv(2)
# fgv(-2)

# Ami -1-től +1-ig tizedenként kiírja egymás mellé a számokat a, a^3, 3*a, |a|

# def hatvany(szam):
#   return szam ** 3

# def szor(szam):
#   return szam * 3

# def abszolut(szam):
#   if szam < 0:
#     return szam * -1
#   return szam

# def kiir(szam):
#   print(szam, hatvany(szam), szor(szam), abszolut(szam))

# for i in range(-10, 10):
#   kiir(i / 10)

# A szám prím-e?
# szam 2 -> szam : szam % i == 0 -> nem prím

# def prime(szam):
#   if szam >= 2:
#     for i in range(2, szam):
#       if szam % i == 0:
#         return False
#     return True
#   else:
#     return False


# print(prime(0))
# print(prime(2))
# print(prime(1))
# print(prime(10))
# print(prime(7))
# print(prime(11))
# print(prime(15))

# Kapunk egy listát és visszaadja azokat az elemeket amik egyediek

# def exists(szam, lista):
#   for i in lista:
#     if i == szam:
#       return True
#   return False

# def uniques(szamok):
#   egyediek = []
#   for szam in szamok:
#     if not exists(szam, egyediek):
#       egyediek.append(szam)
#   return egyediek

# print(uniques([0, 0, 0, 1, 2, 2, 4, 5, 5, 10]))

# 1-> limit piírja a számokat és kiírja páros-e vagy páratlan
# 1 PTLAN
# 2 PAROS

# def paros(szam):
#   return szam % 2 == 0

# def eldont(szam):
#   if paros(szam):
#     return 'PAROS'
#   return 'PTLAN'

# limit = 10

# for i in range(1, limit + 1):
#   print(i, eldont(i))

# a = 1,
# 0 -> a = 1 reset
# 1 -> hozzaad az a-hoz 1-et
# 2 -> megfordítja az előjelet
# 3 -> szoroz 2-vel
# 9 -> kilép

def reset():
  return 1

def add(szam):
  return szam + 1

def invert(szam):
  return -szam

def double(szam):
  return szam * 2

def kerdez():
  return int(input("Opció? "))

def menu():
  print("0: reset (a = 1)")
  print("1: hozzáad 1")
  print("2: megfordít előjel")
  print("3: dupláz")
  print("9: kilép")

a = 1
opcio = 0
while opcio != 9:
  if opcio == 0:
    a = reset()
  if opcio == 1:
    a = add(a)
  if opcio == 2:
    a = invert(a)
  if opcio == 3:
    a = double(a)
  print('a =', a)
  menu()
  opcio = kerdez()
