"""
Implementáld az alábbi függvényeket!
"""


def remove_duplicates(values):
    """A kapott listában az egymást követő azonos értékekből csak az elsőt hagyja meg,
    a többit törli a listából.
    >>> v = [1, 1, 2, 2, 3, 3, 3, 1]
    >>> remove_duplicates(v)
    >>> v
    [1, 2, 3, 1]
    >>> v = [1, 1, 1, 1, 1]
    >>> remove_duplicates(v)
    >>> v
    [1]
    >>> remove_duplicates(v)
    >>> v
    [1]
    """
    i = 0
    while i < len(values)-1:
        if values[i] == values[i+1]:
            del values[i+1]
        else:
            i+=1
    return values

def remove_all(values, to_remove):
    """A kapott listában az összes előfordulását törli a to_remove értéknek.
    >>> v = [1, 1, 2, 2, 3, 3, 3, 1]
    >>> remove_all(v, 2)
    >>> v
    [1, 1, 3, 3, 3, 1]
    >>> v = [1, 1, 1, 1, 1]
    >>> remove_all(v, 1)
    >>> v
    []
    """
    while to_remove in values:
        values.remove(to_remove)
    return values

def remove_values(values, to_remove):
    """A kapott listában az összes előfordulását törli a to_remove listában szereplő értékeknek.
    >>> v = [1, 1, 2, 2, 3, 3, 3, 1]
    >>> remove_values(v, [1, 2])
    >>> v
    [3, 3, 3]
    >>> remove_values(v, [3])
    >>> v
    []
    """
    for number in to_remove:
        remove_all(values, number)
    return values
