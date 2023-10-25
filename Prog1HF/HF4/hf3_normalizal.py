"""
Implementáld az alábbi függvényeket!
"""


def normalize_lin(numbers):
    """A kapott listát 0 és 1 közé normalizálja úgy, hogy a legkisebb elem 0,
    a legnagyobb elem pedig 1 legyen (ha nem egyezik a legkisebbel).
    >>> v = [1, 2, 3, 4, 5]
    >>> normalize_lin(v)
    >>> v
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> v = [1, 1, 1, 1, 1]
    >>> normalize_lin(v)
    >>> v
    [0.0, 0.0, 0.0, 0.0, 0.0]
    >>> v = []
    >>> normalize_lin(v)
    >>> v
    []
    """
    # minden elemből ki kell vonni a minimumot és leosztani a maximum-minimum különbséggel (ha az nem 0)
    minnu=min(numbers)
    maxnu=max(numbers)
    diff=maxnu-minnu
    length = len(numbers)
    for i in range (length):
        numbers[i] -= minnu
        if diff !=0:
            numbers[i]/=diff
    return numbers
print (normalize_lin([1,2,3,4,5]))

def normalize_to_avg(numbers):
    """A kapott listát -1 és 1 közé normalizálja úgy, hogy az átlag 0 legyen.
    >>> v = [0, 1, 2, 3, 4]
    >>> normalize_to_avg(v)
    >>> v
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    >>> v = [3, 3, 4, 6]
    >>> normalize_to_avg(v)
    >>> v
    [-0.5, -0.5, 0.0, 1.0]
    >>> v = [1, 1, 1, 1, 1]
    >>> normalize_to_avg(v)
    >>> v
    [0.0, 0.0, 0.0, 0.0, 0.0]
    >>> v = []
    >>> normalize_to_avg(v)
    >>> v
    []
    """
    # minden elemből ki kell vonni az átlagot és
    # leosztani az átlagtól való legnagyobb abszolút eltérésel (ha az nem 0)
    # if len(numbers) !=0:
    #     avg = sum(numbers)/len(numbers)
    #     maxdiff = 0
    #     i = 0
    #     while i<len (numbers):
    #         diff = abs(numbers[i]-avg)
    #         if diff >= maxdiff:
    #             maxdiff=diff
    #         i += 1
    #     i = 0
    #     while i<len (numbers):
    #         numbers[i] -= avg
    #         if numbers[i] !=0:
    #             numbers.insert(i, numbers[i]/maxdiff)
    #             del numbers[i+1]
    #     i += 1
    # return numbers
# v = [0, 1, 2, 3, 4]
# normalize_to_avg(v)
#totál bebugult nálam a testing ennél, doctesting egyiknél se jó