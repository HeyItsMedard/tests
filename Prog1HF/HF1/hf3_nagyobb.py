"""
Kérj be két számot, majd írd ki, hogy
    "az első szám a nagyobb" vagy
    "a második szám a nagyobb" vagy
    "a két szám egyenlő"
"""
szam1 = int(input("Első szám: "))
szam2 = int(input("Második szám: "))
if szam1 > szam2:
    print("az első szám a nagyobb")
elif szam2 == szam1:
    print("a két szám egyenlő")
else:
    print("a második szám a nagyobb")