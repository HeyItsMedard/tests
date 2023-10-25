"""
Az alábbi dictionary fogja tárolni a hallgatók órai aktivitását.
Implementáld a függvényeket, melyekkel módosíthatók és lekérdezhetők az aktivitások!
"""

aktivitas = {}


def add_activity(name):
    """Növeli a megadott hallgató aktivitását eggyel.
    Ha még nem szerepel a hallgató a dictionaryben, akkor bekerül.
    >>> add_activity("Béla")
    >>> aktivitas
    {'Béla': 1}
    >>> add_activity("Béla")
    >>> aktivitas
    {'Béla': 2}
    >>> add_activity("Feri")
    >>> aktivitas
    {'Béla': 2, 'Feri': 1}
    >>> add_activity("Lilla")
    >>> add_activity("Béla")
    >>> add_activity("Lilla")
    >>> aktivitas
    {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    """
    aktivitas[name] = aktivitas.get(name, 0) + 1
    # if name not in aktivitas:
    #     aktivitas[name] = 1
    # else:
    #     aktivitas[name] += 1

add_activity("Béla")

def get_activity(name):
    """Visszaadja a megadott hallgató aktivitását.
    Ha a hallgató nem szerepel a dictionaryben, akkor 0-t ad vissza.
    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_activity("Béla")
    3
    >>> get_activity("Feri")
    1
    >>> get_activity("Anna")
    0
    """
    return aktivitas.get(name, 0)
print(get_activity("Béla"))

def get_most_active():
    """Visszaadja a legaktívabb hallgató nevét.
    Ha több hallgató is ugyanannyi aktivitással rendelkezik, akkor bármelyiket.
    Ha nincs hallgató, akkor adjon vissza None értéket.
    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_most_active()
    'Béla'
    """
    max = 0
    max_key=list(aktivitas.keys())[0]
    # for key in aktivitas:
    #     max_key = key
    #     break
    if not aktivitas:
        return None
    for key,val in aktivitas.items():
        if val > max:
            max = val
            max_key = key
    return max_key
print(get_most_active())

def get_least_active():
    """Visszaadja a legkevésbé aktív hallgató nevét.
    Ha több hallgató is ugyanannyi aktivitással rendelkezik, akkor bármelyiket.
    Ha nincs hallgató, akkor adjon vissza None értéket.
    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> get_least_active()
    'Feri'
    """
    min_val = min(aktivitas.values())+1
    min_key=list(aktivitas.keys())[0]
    if not aktivitas:
        return None
    for key,val in aktivitas.items():
        if val < min_val:
            min_val = val
            min_key = key
    return min_key
print(get_least_active())


def total_activity():
    """Visszaadja az összes hallgatói aktivitás összegét.
    >>> aktivitas = {'Béla': 3, 'Feri': 1, 'Lilla': 2}
    >>> total_activity()
    6
    """
    sumall = 0
    for key,val in aktivitas.items():
        sumall+=val
    return sumall
print(total_activity())