from functools import partial


"""1. feladat:
A partial segítségével készítsd el a read_num függvényt!
Írja ki, hogy "Kérek egy számot: ", majd olvassa be a számot a felhasználótól!
"""
# def read_num():
#     return input("Kérek egy számot: ")
read_num = partial(input, "Kérek egy számot: ")
number = read_num()

"""2. feladat:
A partial segítségével készítsd el az open_w, open_r és open_a függvényeket!
Ezek nyissák meg a megadott fájlt írásra, olvasásra és hozzáfűzésre, utf-8 kódolással!
"""

open_w = partial(open, mode='w', encoding='utf-8')
with open_w("teszt.txt") as f:
    f.write("Ez egy teszt fájl.\n")

open_a = partial(open, mode='a', encoding='utf-8')
with open_a("teszt.txt") as f:
    f.write("Második sor.\n")

open_r = partial(open, mode='r', encoding='utf-8')
with open_r("teszt.txt") as f:
    print("A fájl tartalma:\n" + f.read())

with open_w("teszt.txt") as f:
    f.write("Felülírás után.\n")

with open_r("teszt.txt") as f:
    print("A fájl tartalma:\n" + f.read())
