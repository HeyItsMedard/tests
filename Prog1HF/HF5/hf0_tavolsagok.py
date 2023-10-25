"""
Implementáld az alábbi függvényt!
"""

def distance(places, start, end):
    """Kap egy listát, melynek elemei [name, x, y] kulcsokkal rendelkező dictionary-k,
    valamint a kezdő és végpont neveit,
    és visszaadja a két pont közötti légvonalbeli távolságot.
    >>> distance([{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 1, "y": 0}, {"name": "C", "x": 1, "y": 1}], "A", "C")
    1.4142135623730951
    """
    for place in places:
        if place.get("name") == start:
            ax = place.get("x") 
            ay = place.get("y")
        if place.get("name") == end:
            bx = place.get("x") 
            by = place.get("y")
    return ((ax-bx) ** 2 + (ay - by) **2 ) ** 0.5
print(distance([{"name": "A", "x": 0, "y": 0}, {"name": "B", "x": 1, "y": 0}, {"name": "C", "x": 1, "y": 1}], "A", "C"))