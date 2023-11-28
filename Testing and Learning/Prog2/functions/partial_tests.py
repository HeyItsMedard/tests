#nesting (currying)
from functools import partial

def multiply(a: float, b:float, name:str|None=None) -> float:
    if name is not None:
        print(f'\n{name}: (a: {a}, b: {b})')

    return a*b

double = partial(multiply, 2, name='Double') # by default, a is given 2
triple = partial(multiply, b=3, name='Triple')

print(double(10))
print(triple(10)) # we've given b 3, so this gives 10 to a

"""Máté példája"""

def multiple_print(count: int, text:str):
    for _ in range(count):
        print(text)


multiple_print(5, "hello")

sokszia = partial(multiple_print, text="szia")
sokszia(5)
sokhello = partial(multiple_print, text="hellobello")
sokhello(10)


doubleprint = partial(multiple_print, count=2)
doubleprint(text="Double")