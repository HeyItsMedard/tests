"""
Kérj be egy természetes számot, majd írd ki a faktoriálisát.
"""
szam = int(input("Kérem, adjon meg egy természetes számot: "))
eredmeny = 1
while szam != 1 and szam > 0:
    eredmeny = szam*eredmeny
    szam -= 1
print(eredmeny)