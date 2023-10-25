import json
import pickle
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def birthday(self):
    self.age += 1

  def greet(self):
    print(f'Hello from {self.name}')

class Calendar:
  def __init__(self, weeks):
    self.weeks = weeks

  @staticmethod
  def print_calendar():
    print("CALENDAR\n1, 2, 3,4")

class Demo:
  def __init__(self):
    self.text = 'asda'

class SaveAs:
  def __init__(self, data):
    self._data = data

  def to_json(self, file_name):
    with open(f'{file_name}.json', "w") as f:
      json.dump(self._data.__dict__, f)

  def to_pickle(self, file_name):
    with open(f'{file_name}.pickle', 'w+b') as f:
      pickle.dump(self._data, f)


bob = Person('Bob', 15)
save = SaveAs(bob)
save.to_json('person')
save.to_pickle('person')

cal = Calendar(52)
save_c = SaveAs(cal)
save_c.to_pickle('calendar')

d = Demo()
save_d = SaveAs(d)
save_d.to_pickle('demo')
