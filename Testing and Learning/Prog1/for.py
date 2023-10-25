# Írjuk ki a lista elemeit

# list = ["alma", "korte", "szilva", "banan"]

# for i in list:
#   print(i)

# Írjuk ki a "banán" karaktereit egyesével
# szoveg = "banán"

# for karakter in szoveg:
#   print(karakter)

# for i in range(len(szoveg)):
#   print(szoveg[i])

# BREAK, CONTINUE

# Írjuk ki a gyümölcsöket, de álljunk meg a banánnnál
list = ["alma", "korte", "banan", "szilva"]

# for gyumolcs in list:
#   if gyumolcs == "banan":
#     break
#   print(gyumolcs)

# Írjuk ki a gyümölcsöket, de hagyjuk ki a banánt

# for gyumolcs in list:
#   if gyumolcs == 'banan':
#     continue
#   print(gyumolcs)

# RANGE(START, END, SKIP)

# Írja ki a számokat 1-10-ig

# for i in range(1, 11):
#   print(i)

# Írja ki a felhasználó által megadott intervallum közötti számokat  3, 8 -> 3, 4, 5, 6, 7, 8
# start = int(input('Kezdeti érték? '))
# end = int(input('Vége érték? '))

# for i in range(start, end + 1):
#   print(i)

# Intervallumban minden x.-ik elemet írjon ki x usertől jön

# skip = int(input('Hányasával? '))

# for i in range(start, end + 1, skip):
#   print(i)

# Else for végén

# for i in range(10):
#   if i > 4:
#     break
#   print(i)
# else:
#   print('vége')

# Listának elemeit összegezni

# list = [2, 1, 2]
# sum = 0
# for number in list:
#   sum += number
# print('Sum', sum)

# Listának elemeit összeszorozza
# list = [2, 1, 2]
# sum = 1
# for number in list:
#   sum *= number
# print('Szorzat', sum)

# Visszaadjuk a legnagyobb elemet egy listából

# list = [0, 1, 2, 5, 10, 6, 20, 7]
# max = list[0]

# for number in list:
#   if number > max:
#     max = number
# print('Max', max)

# Visszadja egy új listában a felhasználó által megadott értéknél nagyobb számokat egy listából

# list = [0, 1, 2, 4, 10, 51, 6]
# list2 = []
# x = int(input('Minél legyen nagyobb? '))

# for i in list:
#   if i > x:
#     list2.append(i)
# print('Hosszabbak', list2)

# Listából minden 2. elemet visszaad egy új listában

# list = [0, 1, 2, 4, 10, 51, 6]
# elemek = []

# for item in range(0, len(list), 2):
#   elemek.append(list[item])
# print('Minden második', elemek)

# Minden adott hossznál hosszabb elemeket ad vissza egy listából

# list = ["alma", "korte", "szilva", "banan", "fa"]
# hossz = int(input('Minél legyen hosszabb? '))

# for item in list:
#   if len(item) > hossz:
#     print(item)

# Fibonacci sorozatot for ciklussal oldjuk meg 7db -> 0 1 1 2 3 5 8
# hossz = int(input('Meddig számoljuk ki? '))
# n1 = 0
# n2 = 1

# for i in range(hossz):
#   print(n1)
#   osszeg = n1 + n2
#   n1 = n2
#   n2 = osszeg

# Piramis milyen magas piramis legyen?
# magassag = int(input('Milyen magas legyen? '))

# for sor in range(magassag):
#   space = magassag - 1 - sor
#   for pont in range(space):
#     print(' ', end="")
#   o = sor * 2 + 1
#   for karika in range(o):
#     print('o', end="")
#   print()

# Írja ki a szorzótáblát

# 1 2 3 4  5  6  7  8  9 10
# 2 4 6 8 10 12 14 16 18 20

# for sor in range(1, 10 + 1):
#   for oszlop in range(1, 10 + 1):
#     print(sor * oszlop, " ", end="")
#   print()

# 2 listának az elemeit egymással kombiáljuk

# gyumolcsok = ['alma', 'körte', 'cseresznye']
# jelzok = ['nagy', 'piros', 'finom']

# for jelzo in jelzok:
#   for gyumolcs in gyumolcsok:
#     print(jelzo, gyumolcs)

# Prim számokat írja ki egy adott intervallumban, amit a felhasználó definiál
# 10, 50 -> 10 < prim? < 50
