"""
Implementáld az alábbi függvényeket!
"""


def insert_zeros(numbers):
    """A kapott számlistába nullákat szúr be minden olyan szomszédos számpár közé,
    melyek ellentétes előjelűek (az egyik pozitív, a másik negatív).
    >>> seq = [1, -2, 3, -4, -5, -6]
    >>> insert_zeros(seq)
    >>> seq
    [1, 0, -2, 0, 3, 0, -4, -5, -6]
    >>> insert_zeros(seq)
    >>> seq
    [1, 0, -2, 0, 3, 0, -4, -5, -6]
    """
    i = 0
    while i < len(numbers) - 1:
        if (numbers[i] < 0 and numbers[i+1] > 0) or (numbers[i] > 0 and numbers[i+1] < 0):
            numbers.insert(i+1, 0)
            i +=1
        i +=1
    return numbers

def add_coupon(prices, discount):
    """A legdrágább termék ára után beszúr egy negatív számot, ami megfelel a megadott kedvezménynek.
    Ha több max. árú termék is van, akkor az első után szúr be.
        prices (list): a megvásárolt termékek árai 
        discount (int): a kedvezmény mértéke százalékban (1-100)
    >>> prices = [100, 200, 300, 250, 300]
    >>> add_coupon(prices, 10)
    >>> prices
    [100, 200, 300, -30.0, 250, 300]
    """
    percentage = discount/100
    most_valuable = max(prices)
    prices.insert(prices.index(most_valuable)+1, -most_valuable*percentage)
    return prices
