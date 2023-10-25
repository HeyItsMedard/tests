import json
import pickle

with open('person.json') as f:
  p = json.load(f)
  print(p)
  # p.birthday()
  print(p)

from main import Person

with open('person.pickle', 'b+r') as f:
  p: Person = pickle.load(f)
  print(p)
  p.birthday()
  print(p.age)
  p.greet()

with open('calendar.pickle', 'b+r') as f:
  cal = pickle.load(f)
  print(cal)
  print(cal.weeks)
  cal.print_calendar()


with open('demo.pickle', 'b+r') as f:
  d = pickle.load(f)
  print(d)
  print(d.text)
