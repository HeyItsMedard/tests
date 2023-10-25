def logger(cb):
  def wrapper(*args):
    print('before')
    cb(*args)
    print('after')

  return wrapper

@logger # fg = logger(fg)
def fg():
  print('hello')

from functools import partial

def add(a, b):
  print(a + b)

add(1, 2)

add_2 = partial(add, b=2)
add_5 = partial(add, 5)
add_2(1)

print(add_5)
