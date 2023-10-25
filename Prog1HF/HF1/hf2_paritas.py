"""
Kérj be egy természetes számot, és írd ki, hogy "páros" vagy, hogy "páratlan" a megadott szám.
"""

szam = int(input("Kérem, adjon meg egy természetes számot: "))
if szam % 2 == 0:
    print("páros")
else:
    print("páratlan")