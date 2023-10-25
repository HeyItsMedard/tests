"""
Olvass be 100 egész számot, majd írd ki, hány különböző volt köztük.
"""
lista = []

for i in range(100):
    szam = int(input("Szám: "))
    if i==0:
        lista.append(szam)
    else:
        db=0
        for elem in lista:
            if elem==szam:
                db+=1
        if db==0:
            lista.append(szam)
    i+=1
print(len(lista))