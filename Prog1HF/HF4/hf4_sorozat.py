"""
Implementáld az alábbi függvényeket!
"""


def arithmetic_seq(first, diff, n):
    """Visszaad egy számtani sorozatot tartalmazó listát, a megadott kezdőértékkel,
    lépésközzel, és elemszámmal.
    >>> arithmetic_seq(0, 1, 5)
    [0, 1, 2, 3, 4]
    >>> arithmetic_seq(5, -2, 4)
    [5, 3, 1, -1]
    """
    # minden elemből ki kell vonni a minimumot és leosztani a maximum-minimum különbséggel (ha az nem 0) #???
    seq = []
    number = first
    for i in range(n):
        seq.append(number)
        number = number + diff

    return seq
print(arithmetic_seq(5, -2, 4))

def geometric_seq(first, ratio, n):
    """Visszaad egy mértani sorozatot tartalmazó listát, a megadott kezdőértékkel,
    kvócienssel, és elemszámmal.
    >>> geometric_seq(1.0, 2.0, 5)
    [1.0, 2.0, 4.0, 8.0, 16.0]
    >>> geometric_seq(1.0, 0.5, 4)
    [1.0, 0.5, 0.25, 0.125]
    """
    # minden elemből ki kell vonni a minimumot és leosztani a maximum-minimum különbséggel (ha az nem 0) 
    seq = []
    number = first
    for i in range(n):
        seq.append(number)
        number = number * ratio

    return seq
print(geometric_seq(1.0, 2.0, 5))
def is_arithmetic(sequence):
    """Visszaadja, hogy a megadott lista egy számtani sorozat-e."""
    diff = sequence[1] - sequence [0]
    for i in range(len(sequence)-1):
        if (sequence[i+1] - sequence[i] != diff):
            return False 

    return True


def is_geometric(sequence):
    """Visszaadja, hogy a megadott lista egy mértani sorozat-e."""
    diff = sequence[1] / sequence [0]
    for i in range(len(sequence)-1):
        if (sequence[i+1] / sequence[i] != diff):
            return False 
    return True


def resize_seq(sequence, new_size):
    """Ha a megadott lista egy legalább 3 elemű számtani vagy mértani sorozat,
    akkor a megadott méretűre bővíti vagy csökkenti a sorozatot a listában.
    Különben nem csinál semmit.
    >>> seq = [1, 2, 3]
    >>> resize_seq(seq, 5)
    >>> seq
    [1, 2, 3, 4, 5]
    >>> resize_seq(seq, 3)
    >>> seq
    [1, 2, 3]
    """
    if (is_arithmetic(sequence) or is_geometric(sequence)) and (len(sequence) >= 3) and new_size > 0:
        if len(sequence) > new_size:
            return sequence[:new_size-len(sequence)]
        elif len(sequence) == new_size:
            return sequence
        else:
            # start = len(sequence)
            # end = new_size       
            # if is_arithmetic(sequence):
            #     diff = sequence[1] - sequence[0]
            #     for i in range(start, end):
            #         number = sequence[i-1] + diff
            #         sequence.append(number)
            # elif is_geometric(sequence):
            #     diff = sequence[1] / sequence[0]      
            #     for i in range(start, end):
            #         number = sequence[i-1] * diff
            #         sequence.append(number)
            # return sequence
            if is_arithmetic(sequence):
                return arithmetic_seq(sequence[0], sequence[1] - sequence[0], new_size)
            elif is_geometric(sequence):
                return geometric_seq(sequence[0], sequence[1] / sequence[0], new_size) #1, 2/1=2, 2
    else:
        return sequence
    # hasznos lehet a list .extend() metódusa
print(resize_seq([1, 1, 1], 10))