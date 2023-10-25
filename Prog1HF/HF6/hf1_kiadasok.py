"""
Implementáld az alábbi függvényeket, melyek a személyes kiadások követését segítik.
Készíthetsz további segédfüggvényeket is.
"""


def read_monthly_expenses(filename: str, year: int = 2023) -> list[int]:
    """Beolvassa a megadott logfájlt, és visszaad egy 12 elemű listát,
    melyben a megadott év kiadásainak havi összegei szerepelnek (jan., feb., ...).

    A logfájl minden sora egy kiadás dátumát (yyyy-mm-dd) és mértékét (int) tartalmazza,
    szóközzel elválsztva:
    2023-03-31 1000
    A sorok nincsenek dátum szerint rendezve, és lehetnek hiányzó hónapok, évek.

    >>> read_monthly_expenses("hf1_pelda.log", 2022)
    [2054, 0, 11639, 4046, 11236, 6043, 16739, 11111, 26344, 5845, 6805, 5938]
    """
    monthly_paid = [0] * 12
    
    with open(filename) as f:
        for line in f:
            date, paid = line.split(" ")
            y, m = date.split("-")[:2]
            if int(y) == year:
                monthly_paid[int(m)-1] += int(paid)
        
    return monthly_paid
print(read_monthly_expenses("hf1_pelda.log", 2022))

def export_expenses(log_file: str) -> None:
    """Beolvassa a kiadásokat a logfájlból, és minden a fájlban szereplő évhez készít
    egy kimutatás fájlt {évszám}.txt néven, mely a havi kiadásokat tartalmazza.
    A kimeneti fájlnak minden sora egy hónap kiadását tartalmazza, pl.:
    2054
    0
    11639
    4046
    ...
    Ha a fájl létezik, akkor felülírja.
    """
    years = [] #set(), elemei kapcsos zárójellel

    with open(log_file) as log:
        for line in log:
            date, _ = line.split(" ")
            y = date.split("-")[0]
            if y not in years:
                yearly = read_monthly_expenses(log_file, int(y)) #év helyett pl. 2011
                with open(f"{y}.txt", "w") as f:
                    for monthly in yearly:
                        f.write(f"{monthly}\n")
            years.append(y) #set esetén add fv.

export_expenses("hf1_pelda.log")
def get_most_expensive_month(log_file: str) -> str:
    """Visszaadja a legtöbb kiadást tartalmazó hónapot yyyy-mm formátumban.
    Ha több hónap is ugyanannyi kiadással rendelkezik, akkor a legkorábbit.

    >>> get_most_expensive_month("hf1_pelda.log")
    '2011-03'
    """
    per_month = {}
    with open(log_file, 'r') as f:
        for line in f:
            date, value = line.strip().split()
            date = date[:7] #csak év és hónap
            if date not in per_month:
                per_month[date] = int(value)
            else:
                per_month[date] += int(value)
    monthly = list(per_month.values())
    maxval = max(monthly)
    maxmonth = None
    for month, val in per_month.items():
        if val == maxval and (maxmonth is None or maxmonth >month):
            maxmonth = month
    return maxmonth
    
print(get_most_expensive_month("hf1_pelda.log"))