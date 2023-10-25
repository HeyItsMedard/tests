class Stack:
  def __init__(self, items=[]):
    self._items = items

  def push(self, item):
    self._items.append(item)

  def pop(self):
    return self._items.pop()

  def __repr__(self):
    return f'{self._items}'

s = Stack()
s.push(10)
s.push(5)
s.push(3)
s.push(7)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
