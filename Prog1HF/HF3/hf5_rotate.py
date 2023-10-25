"""
Implementáld az alábbi függvényeket!
"""

def shift(values):
    """Visszaadja a kapott values lista elcsúsztatott változatát.
    Az eredmény egy olyan lista, ahol minden elem 1 hellyel jobbra kerül,
    az utolsót kivéve, ami az elejére kerül.
    >>> shift([1, 2, 3, 4])
    [4, 1, 2, 3]
    >>> shift([5, 4, 3, 2, 1])
    [1, 5, 4, 3, 2]
    >>> shift([2])
    [2]
    >>> shift([])
    []
    """
    return values[-1:] + values[:-1] #utolsó elemet leválasztja és hozzáilleszti a másik listához, ahol le van választva az első elem

def rotate(values, shift_by):
    """Visszaadja a kapott values lista "elforgatott" mását.
    Az elforgatás során minden elem shift_by hellyel jobbra kerül,
    az utolsó index után az elején folytatva a sort.
    Negatív shift_by esetén balra mozdulnak el az elemek.
    >>> rotate([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotate([1, 2, 3, 4, 5], -2)
    [3, 4, 5, 1, 2]
    >>> rotate([1, 2, 3, 4, 5], 0)
    [1, 2, 3, 4, 5]
    >>> rotate([1, 2, 3, 4, 5], 5)
    [1, 2, 3, 4, 5]
    >>> rotate([1, 2, 3, 4, 5], 51)
    [5, 1, 2, 3, 4]
    """
    # Szorgalmi: próbáld meg a shift() használata nélkül,
    # minden elemet egyből a helyére téve megoldani.
    if shift_by == 0 or len(values) == 0:
        return values
    oszto = shift_by % len(values)
    return values[-oszto:] + values[:-oszto]
print(rotate([1, 2, 3, 4, 5], -2))

def is_palindrome(values):
    """Visszaadja, hogy a kapott values lista palindrom-e,
    azaz ugyanaz-e visszafelé is.
    >>> is_palindrome([1, 2, 3, 2, 1])
    True
    >>> is_palindrome([1, 2, 3, 4, 5])
    False
    >>> is_palindrome([1, 3, 3, 1])
    True
    >>> is_palindrome([])
    True
    """
    for i in range(int(len(values)/2)):
        if values[i] != values[len(values)-i-1]:
            return False
    return True