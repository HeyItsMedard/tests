"""
Olvass be 10 egész számot egy listába.
Olvass be még egy számot, és keresd meg a legnagyobb többszörösét a listában.
Írd ki a legnagyobb többszöröst, vagy azt, hogy "nem található a többszöröse".
"""
lista = []
for i in range(10):
    szam = int(input("Szám: "))
    lista.append(szam)
keres = int(input("Keresésre alkalmazott szám: "))
lt = 0
for szam in lista:
    if szam % keres == 0 and szam > lt:
        lt = szam
if lt == 0:
    print("nem található a többszöröse")
else:
    print(lt)