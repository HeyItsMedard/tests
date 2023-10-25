"""
Olvass be 10 egész számot egy listába.
Olvass be 2 listaindexet (2 külön input() hívással).
Cseréld fel a megadott indexeken lévő elemeket.
Az így kapott listát a print()-nek paraméterként átadva írasd ki.
"""
lista = []
for i in range(10):
    szam = int(input("Szám: "))
    lista.append(szam)
ind1 = int(input("Index1: "))
ind2 = int(input("Index2: "))
temp = lista[ind1]
lista[ind1] = lista[ind2]
lista[ind2] = temp
print(lista)
