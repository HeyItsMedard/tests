"""
Implementáld az alábbi függvényeket!
"""

allergenek = ["glutén", "tej", "mogyoró", "tojás", "hal", "rákfélék", "szója"]

def collect_allergenes(menu):
    """Kap egy dictionaryt, melyben a kulcsok az ételek nevei, az értékek pedig a benne található allergének indexeinek listái. Az indexek a fenti allergenek listának megfelelően vannak megadva.
    Visszaad egy dictionaryt, melyben a kulcsok az allergének nevei, az értékek pedig az ételek listái, melyekben előfordulnak.
    Csak olyan allergének szerepeljenek a visszaadott dictionaryben, melyek valamilyen ételben előfordulnak!
    >>> collect_allergenes({"tészta": [0, 3], "krumplipüré": [0, 1, 3], "halászlé": [4, 5], "húsleves": []}) \
        == {'glutén': ['tészta', 'krumplipüré'], 'tej': ['krumplipüré'], 'tojás': ['tészta', 'krumplipüré'], 'hal': ['halászlé'], 'rákfélék': ['halászlé']}
    True
    """
    newdict = {}
    for dish, allergens in menu.items(): # pl. food: "halászlé" str, allergens: [4, 5], index lista
        for allergen_index in allergens: #4, 5
            allergen_name = allergenek[allergen_index] #hal = allergenek[4], rákfélék = allergenek[5]
            if allergen_name in newdict: #ha benne van hal a dictionaryben
                newdict[allergen_name].append(dish) #hosszabítsa meg és rendelje hozzá a halhoz az ételt
            else:
                newdict[allergen_name] = [dish] #első elem a halhoz
    return newdict


def filter_menu(menu, allergenes):
    """Kap egy olyan dictionaryt, mint a collect_allergenes, valamint egy listát egy vendég allergéneinek neveivel.
    Visszaad egy listát, melyben azok az ételek szerepelnek, melyekben nincs benne az allergének közül egy sem.
    >>> filter_menu({"tészta": [0, 3], "krumplipüré": [0, 1, 3], "halászlé": [4, 5], "húsleves": []}, ["glutén", "tej"])
    ['halászlé', 'húsleves']
    """
    allergen_dict = collect_allergenes(menu)
    recommended = []
    
    for dish in menu: #tészta, krumplipüré...
        allergen_found = False #alaphelyzet
        for allergen in allergenes: #Sándor: glutén, tej
            if allergen in allergen_dict and dish in allergen_dict[allergen]: #ha benne van a vendég allergénje az ételben
                allergen_found = True
                break #kilépünk a ciklusból, találtunk allergént, átmegyünk az if ágra
        if allergen_found:
            continue #átugorjuk azt a fogást, amiben allergén van
        
        recommended.append(dish) # végezetül a menteseket kiírjuk
    return recommended
