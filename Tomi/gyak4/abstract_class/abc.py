# Abstract Base Classes

from abc import ABC, abstractmethod
import math

class Shape(ABC):
  @abstractmethod
  def get_area(self):
    pass

  @abstractmethod
  def get_perimeter(self):
    pass

  def welcome(self):
    print('Hi i am a shape')


class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius**2

  def get_perimeter(self):
    return math.pi * 2 * self.radius

  def welcome(self):
    print("Hi i am a circle")

class Rectangle(Shape):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def get_area(self):
    return self.a * self.b

  def get_perimeter(self):
    return 2 * (self.a + self.b)

sh1 = Circle(4)
sh2 = Rectangle(2, 3)

def method(s1: Shape, s2: Shape) -> (float, float):
  return (s1.get_area() + s2.get_area(), s1.get_perimeter() + s2.get_perimeter())

print(method(sh1, sh2))
sh1.welcome()
sh2.welcome()

len([1, 2, 3])
len({ 'A': 1 })
len((1, 2))
