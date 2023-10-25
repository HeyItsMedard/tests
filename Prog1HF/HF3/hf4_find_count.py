"""
Implementáld az alábbi függvényeket!
"""


def find_indexes(values, to_find):
    """Visszaadja egy listaként, hogy a megadott listában mely indexeken szerepel a keresett érték.
    >>> find_indexes([1, 2, 3, 1, 2, 1, 4], 1)
    [0, 3, 5]
    >>> find_indexes([1, 2, 3, 1, 2, 1, 4], 2)
    [1, 4]
    >>> find_indexes([1, 2, 3, 1, 2, 1, 4], 4)
    [6]
    >>> find_indexes([1, 2, 3, 1, 2, 1, 4], 5)
    []
    """
    found = []
    for i in range(len(values)):
        if to_find == values[i]:
            found.append(i)
    return found




def to_counts(numbers):
    """Visszaad egy olyan listát, melynek elemei megadják
    a megadott listában szereplő 0-k, 1-k, 2-k, ... számát.
    A lista hossza a megadott lista legnagyobb eleme + 1.
    >>> to_counts([3, 2, 3, 1, 2, 4])
    [0, 1, 2, 2, 1]
    >>> to_counts([])
    []
    >>> to_counts([1])
    [0, 1]
    """
    lista = []
    i = 0
    max = 0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i+=1
    i = 0
    while i<max+1:
        if len(numbers)==0:
            break
        j=0
        db=0
        while j<len(numbers):
            if i==numbers[j]:
                db+=1
            j+=1
        lista.append(db)
        i+=1
    return lista


def barchart(values):
    """Visszaad egy listát, amely a kapott lista értékeivel egyenlő hosszúságú,
    '*' karakterekből álló stringeket tartalmaz.
    >>> barchart([3, 0, 2, 3, 1, 2, 4])
    ['***', '', '**', '***', '*', '**', '****']
    """
    lista = []
    for i in range(len(values)):
        lista.append("*"*values[i])
    return lista
