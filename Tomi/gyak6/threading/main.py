
cica = lambda x: print(x)

isOdd = lambda x: x % 2 == 1

def isEven(x):
  return x % 2 == 0

l = [1, 2, 3, 4]
l2 = filter(isEven, l)
print(list(l2))
l3 = list(filter(lambda x: x % 2 == 1, l))
print(l3)


print(list(map(lambda x: x**2, [1, 2, 3])))
print([x**2 for x in [1, 2, 3]])


add = lambda a, b: a + b

print(add(1, 2))
