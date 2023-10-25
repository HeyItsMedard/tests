"""
Olvass be 10 egész számot egy listába, majd olvass be további 10 egész számot,
amiket adj hozzá a lista elemeihez.
Az elsőt az elsőhöz, a másodikat a másodikhoz, és így tovább...
Az így kapott listát a print()-nek paraméterként átadva írasd ki.
"""
lista = []
for i in range(10):
    szam = int(input("Szám: "))
    lista.append(szam)
for i in range(10):
    szam = int(input("Szám: "))
    lista[i] += szam
print(lista)