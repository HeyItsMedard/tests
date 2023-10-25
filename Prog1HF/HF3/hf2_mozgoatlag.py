"""
Implementáld az alábbi függvényeket!
A megoldás során használd fel a már megírt függvényeket!
"""


def average(numbers):
    """Visszaadja a kapott listában lévő számok átlagát.
    >>> average([1, 2, 3, 4])
    2.5
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


# Add meg a helyes paraméterlistát is!
def slice(numbers, start=0, stop=-1):
    """Viszaadja a kapott lista részét egy új listaként.
    A start paraméter megadja a rész kezdő indexét.
        Ha nincs megadva, akkor 0.
    A stop paraméter megadja a rész utáni első indexet.
        Ha nincs megadva, akkor a lista végéig tart a rész.
    >>> slice([1, 2, 3, 4], 1, 3)
    [2, 3]
    >>> slice([1, 2, 3, 4], 1)
    [2, 3, 4]
    >>> slice([1, 2, 3, 4], stop=3)
    [1, 2, 3]
    """
    if stop ==-1:
        stop = len(numbers)
    new_list = []
    for i in range(start, stop):
        new_list.append(numbers[i])
    return new_list


def moving_average(numbers, window_size):
    """Visszaadja a kapott listában lévő számok mozgóátlagait tartalmazó listát.
    A window_size az ablak mérete, azaz hogy hány szomszédos elem átlagát kell venni.
    Az eredmény listában minden elem a megfelelő ablak átlaga.
    >>> moving_average([1, 2, 3, 4, 5], 3)
    [2.0, 3.0, 4.0]
    >>> moving_average([1, 2, 3, 4, 5], 2)
    [1.5, 2.5, 3.5, 4.5]
    >>> moving_average([1, 2, 3, 4, 5], 1)
    [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> moving_average([1, 2, 3, 4, 5], 5)
    [3.0]
    """
    new_list = []
    count=len(numbers) - window_size + 1
    for i in range(count):
        avglist = slice(numbers, i, window_size+i)
        new_list.append(average(avglist))
    return new_list