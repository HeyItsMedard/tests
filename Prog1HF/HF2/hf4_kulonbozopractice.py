"""
Olvass be 100 egész számot, majd írd ki, hány különböző volt köztük. randommal, dicttel: a kulcs a különbségek száma, a value az előfordulása!
"""
import random
lista = []
num_of_diffs = {}
for _ in range(100):
    lista = []
    for i in range(100):
        szam = random.randint(1, 100)
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
    diffcount = len(lista)
    if diffcount not in num_of_diffs:
        num_of_diffs[diffcount] = 1
    else:
        num_of_diffs[diffcount] += 1
sorted_num_of_diffs = dict(sorted(num_of_diffs.items()))

print(sorted_num_of_diffs)
max_occurrence = max(num_of_diffs.values())
max_entries = {key: value for key, value in num_of_diffs.items() if value == max_occurrence}
print(max_entries)