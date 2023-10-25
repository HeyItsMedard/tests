"""
List comperehension ami számok listáját kapja és csak a páros számokat tartalmazó listát ad vissza."""

numbers = [1, 2, 3, 4 ,4 ,5 ,6, 7,8, 10]

evens = [number for number in numbers if number % 2 == 0]

"""
List comprehension, ami sztringek listáját kapja és csak azokat a sztringeket tartalmazó listát adja vissza, amik a betűvel kezdődnek."""

strings = ['apple', 'banana', 'cherry', 'alma', 'ananas', 'a']

starts_a = [string for string in strings if string[0] == 'a']

"""Dict comprehension, ami sztringek listáját kapja és egy új dict-et ad vissza, ahol a kulcsok a sztringek, a valuek pedig a sztringek hossza."""

lengths = { string: len(string) for string in strings }

"""Set comprehension, ami számok listáját kapja és csak a unique számokat tartalmazó set-et ad vissza."""

numbers = [1, 2, 3, 3, 1, 2, 3, 4]
unique_numbers = { number for number in numbers }

"""
List comprehension ami listák listáját kapja vissza és csak a páros számokat tartalmazó listát adja vissza."""
lists = [[], [2, 3, 4], [2, 4, 6, 10, 12], [2, 3, 4, 5]]
nested_evens = [num for l in lists for num in l if num % 2 == 0]

"""List comprehension ami dictionarik listáját kapja meg és visszaadja a neveket, akiknek a koruk nagyobb mint 30."""

users = { 'a1': 28, 'a2':  32, 'b1': 34, 'b2': 12}
old_users = { key: value for key, value in users.items() if value > 30}

"""
Dictek listája amiben emberek vannak és kellene egy sima dict amiben benne vannak az emberek és az adataik is.
"""
users = [
  { 'name': 'asd', 'age': 21, 'city': 'Sopron', 'felesleges_adat': 1 },
  { 'name': 'asd2', 'age': 23, 'city': 'Budapest' },
  { 'name': 'user3', 'age': 21, 'city': 'Sopron'},
  { 'name': 'user4', 'age': 23, 'city': 'Budapest'}
]

flattened_users = { user['name']: { 'age': user['age'], 'city': user['city']} for user in users }

users = { 'a1': 28, 'a2':  32, 'b1': 34, 'b2': 12}
for key, value in users.items():
  print(key, value)

for index, _ in enumerate(users):
  print(index)

fruits = ['apple', 'banana', 'cherry', 'alma', 'ananas', 'a']

for index in range(len(fruits)):
  fruit = fruits[index]
  if fruit[0] == 'a':
    print(fruit, index)

for index, fruit in enumerate(fruits):
  if fruit[0] == 'a':
    print(index, fruit)

for index, (key, value) in enumerate(users.items()):
  print(index, key, value)
