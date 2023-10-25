"""
Implementáld az alábbi függvényeket!
"""


def remove_divisors(numbers, multiple):
    """A kapott listából kitörli a multiple paraméterben megadott szám osztóit
        és visszaadja őket egy új listában.
    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> remove_divisors(numbers, 30)
    [1, 2, 3, 5, 6]
    >>> numbers
    [4, 7, 8, 9]
    """
    new_list = []   
    for number in numbers[:]:
        if multiple % number == 0:
            new_list.append(number)
            numbers.remove(number)

    return new_list


def prime_factors(number):
    """Visszaadja a kapott szám prímtényezőinek listáját.
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(24)
    [2, 2, 2, 3]
    >>> prime_factors(1)
    []
    >>> prime_factors(2)
    [2]
    >>> prime_factors(3)
    [3]
    """
    prime = []
    i = 2
    while i <= number:
        if number % i == 0:
            prime.append(i)
            number = number / i
            i = 2
        else:
            i +=1
    return prime

print(prime_factors(12))

def nontrivial_divisors(number):
    """Visszaadja a kapott szám valódi osztóit.
    >>> nontrivial_divisors(12)
    [2, 3, 4, 6]
    >>> nontrivial_divisors(24)
    [2, 3, 4, 6, 8, 12]
    >>> nontrivial_divisors(1)
    []
    """
    divisors = []
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(nontrivial_divisors(12))

def common_divisors(numbers):
    """Visszaadja a kapott számok közös osztóinak listáját.
    >>> common_divisors([12, 24])
    [1, 2, 3, 4, 6, 12]
    >>> common_divisors([15, 24])
    [1, 3]
    >>> common_divisors([60, 120, 16, 20])
    [1, 2, 4]
    """
    alldivisors = []
    # for i in range(len(numbers)):
    #     for j in range(1, numbers[i]):
    #         if numbers[i] % j == 0:
    #             divisors[:].append(i)
    min = numbers[0]
    for i in range(len(numbers)):
        if min >= numbers[i]:
            min = numbers[i]
    for i in range(1, min+1):
        for j in range(len(numbers)):
            if numbers[j] % i == 0:
                alldivisors.append(i)
    cdivisors = []
    for i in range(1, min+1):
        if alldivisors.count(i) == len(numbers):
            cdivisors.append(i)
    return cdivisors
print(common_divisors([60, 120, 16, 20]))
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(remove_divisors(numbers, 30))
# print(numbers)