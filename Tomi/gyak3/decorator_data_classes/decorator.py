import time

def timer(cb):
  def wrapper(*args):
    start = time.time()
    print("before")
    cb(*args)
    print('after', time.time() - start)
  return wrapper

@timer # fg = timer(fg)
def fg(*args):
  print('hello', *args)

# fg = timer(fg)
fg(3, 3, 3)

def input_add(cb):
  def wrapper(count = 0):
    if not count:
      var = int(input('Give number: '))
      print('Calling method with', var)
      cb(var)
    else:
      cb(count)
  return wrapper

@input_add
def printer(count):
  print('hello' * count)

printer()
