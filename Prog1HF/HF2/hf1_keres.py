"""
Olvass be egész számokat egy listába, míg 0-t nem kapsz.
A 0-t már ne add hozzá a listához.
Ezután olvasd be a keresendő számot, és írd ki a listabeli indexét.
Ha nem szerepel a listában, akkor írj ki "-1"-et.
Ha többször is szerepel, csak az első indexét írd ki.
"""
lista = []
szam = 1
while True:
    szam = int(input("Szám (0 - Kilépés): "))
    if szam == 0:
        break
    lista.append(szam)
keres = int(input("Keresett érték: "))
if keres in lista:
    print(lista.index(keres))
else:
    print(-1)
