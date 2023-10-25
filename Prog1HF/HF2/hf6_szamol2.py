"""
Olvass be 100 egész számot egy listába.
Olvass be további egész számokat, és mindegyik után írd ki, hányszor szerepel a
listában (ne add hozzá újból a listához).
Ha olyan számot adnak meg, ami nincs a listában, akkor a 0 kiírása után álljon
le a program.
"""
lista = []
i = 0
while i < 100:
    szam = int(input("Szám: "))
    lista.append(szam)
    i+=1
while True:
    szam = int(input("Keresésre alkalmazott szám: "))
    j=0
    db = 0
    while j<len(lista):
        if lista[j] == szam:
            db += 1
        j+=1
    if db == 0:
        print(0)
        break
    else:
        print(db)