class Circle:
  PI = 3
  def __init__(self, radius, color = 'white'):
    self.radius = radius
    self.color = color

  def calculateArea(self):
    import math
    print(math.pi * self.radius**2, self.color)

# c1 = Circle(2, "black")
# c2 = Circle(4)
# c1.calculateArea()
# c2.calculateArea()

class Vehicle:
  DEFAUL_LICENSE = 'aaa-111'
  def __init__(self, license_plate = DEFAULT_LICENSE, color, tank, tank_size, usage = 1):
    self.__license_plate = license_plate
    self._color = color
    self._tank = tank
    self._tank_size = tank_size
    self._on = False
    self._usage = usage

  def fuel_up(self, amount):
    if self._tank + amount <= self._tank_size:
      self._tank += amount
      print(f'pouring in {amount}')
    else:
      print('nono')

  def turn_on(self):
    print('turning on the engine')
    self._on = True

  def turn_off(self):
    print('turning off the engine')
    self._on = False

  def drive(self):
    while self._tank > 0 and self._on:
      print('driving and using up fuel')
      self._tank -= self._usage
    self.turn_off()

  def __str__(self):
    return f'{self.__license_plate} car is {self._color} with a tank size of {self._tank_size} and the current level is {self._tank}'

  def __repr__(self):
    return f'{self.__license_plate}:{self._color},{self._tank},{self._tank_size},{self._usage}'

ford = Vehicle("ford-1", "blue", 0, 30, 2)
tesla = Vehicle("tesla-1", "white", 0, 20)
ford.fuel_up(5)
ford.turn_on()
ford._Vehicle__license_plate = "haha-2"
print(ford)
l = [ford, tesla]
print(l)
# ford.drive()
tesla.fuel_up(5)
tesla.turn_on()
# tesla.drive()
