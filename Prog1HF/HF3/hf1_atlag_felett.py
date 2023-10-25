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

def count_greater_than(numbers, threshold):
    """Visszaadja a számokból azokat, amik nagyobbak, mint a küszöbérték.
    >>> count_greater_than([1, 2, 3, 4], 2)
    2
    """
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count

def count_greater_than_average(numbers):
    """Visszaadja a számokból azokat, amik nagyobbak, mint az átlag.
    >>> count_greater_than_average([1, 2, 3, 4])
    2
    """
    return count_greater_than(numbers, average(numbers))


