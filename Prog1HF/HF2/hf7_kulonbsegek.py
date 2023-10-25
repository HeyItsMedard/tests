"""
Olvass be 10 egész számot egy listába.
Készíts egy újabb listát az eredeti lista egymást követő elemeinek
különbségeiből.
Az így kapott listát a print()-nek paraméterként átadva írasd ki.
"""
lista1 = []
lista2 = []
for i in range(10):
    szam = int(input("Szám: "))
    lista1.append(szam)
for i in range(len(lista1)-1):
    lista2.append(lista1[i+1]-lista1[i])
print(lista2)