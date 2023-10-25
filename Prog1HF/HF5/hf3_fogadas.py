"""
Implementáld az alábbi függvényt!
"""

def calc_profit(bets, results):
    """Kap egy dict-et, amelyben a fogadáson megtett tétek szerepelnek és egy listát a befutók sorrendjéről,
    és visszaadja a fogadáson elért nyereséget (veszteség esetén negatív).
    A fogadások kulcsai a versenyzők nevei, az értékei pedig a pénzmennyiségek.
    Az 1. helyezett eltalálásáért a tét 3-szorosa, a 2. helyezett eltalálásáért a tét 2-szorosa jár,
    a 3. helyezett eltalálásáért a tét visszajár, a többi helyezésért pedig nem jár semmi.
    A profit a nyeremények és a tétek összegeinek különbsége.
    >>> calc_profit({"A": 100, "B": 200, "C": 50}, ["A", "D", "B", "C"])
    150
    A fenti példában a nyeremény 3*100 + 1*200 = 500, a tétek összege 100 + 200 + 50 = 350,
    a profit 500 - 350 = 150.
    """
    sumbet = 0
    for bet in bets.values():
        sumbet += bet
    winning = 0
    for i in range(len (results)):
        if i > 2:
            winning += 0
        else:
            if results[i] in bets and i == 0:
                winning += bets[results[i]]*3
            elif results[i] in bets and i == 1:
                winning += bets[results[i]]*2
            elif results[i] in bets and i == 2:
                winning += bets [results[i]]
    return winning - sumbet
print(calc_profit({"A": 100, "B": 200, "C": 50}, ["A", "D", "B", "C"])) #test fail???