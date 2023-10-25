"""
Kérj be egy számot, ami megadja, hány listaelemet szeretne megadni a felhasználó.
Olvass be ennyi racionális számot, és tárold őket egy listába.
Számold meg, és írd ki, hogy közülük hány szám nagyobb, mint az utolsó.
"""
hossz = int(input("Lista hossza: "))
lista = []
for i in range(hossz):
    szam = float(input("Szám: "))
    lista.append(szam)
utolso = lista[hossz-1]
darab = 0
for i in range(hossz):
    if lista[i] > utolso:
        darab += 1
print(darab)