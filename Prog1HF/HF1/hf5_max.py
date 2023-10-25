"""
Kérj be számokat, míg 0-t nem kapsz, majd írd ki, mi volt a legnagyobb kapott szám.
"""
szam = float(input("Szám (0 - Kilépés): "))
max = szam
while szam != 0:
    if szam >= max:
        max = szam
    szam = float(input("Szám (0 - Kilépés): "))
print(max)
