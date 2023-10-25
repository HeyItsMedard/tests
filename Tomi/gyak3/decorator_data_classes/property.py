import math
class Circle:
  def __init__(self, radius):
    self.__radius = radius

  @property
  def radius(self):
    return self.__radius

  @radius.setter
  def radius(self, value):
    print('overwrite radius')
    self.__radius = value

  @property
  def diameter(self):
    return 2 * self.__radius

  @diameter.setter
  def diameter(self, value):
    self.__radius = value / 2

  @property
  def area(self):
    return self.__radius ** 2  * math.pi

  @property
  def circumference(self):
    return 2 * self.__radius * math.pi


circle = Circle(5)
circle.radius = 10
circle.diameter = 40
print('radius', circle.radius)
print('diameter', circle.diameter)
print('area', circle.area)
print('circum', circle.circumference)
