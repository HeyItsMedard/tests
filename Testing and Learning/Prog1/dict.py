# Tuple, Dictionary

# tuple = ("alma", "korte", "banan")

# for gyumolcs in tuple:
#     print(gyumolcs)

# if "alma" in tuple:
#     print("van alma")

# print(len(tuple))

# Dictionary
# student = { "name": "Alice", "classes": ["Math", "English"] }

# print(student["name"])
# print(student.get("name"))
# classes = student["classes"]
# print(classes[1])

# student["name"] = "Bob"
# student["classes"] = ["Math", "English", "History"]
# student["age"] = 18
# print(student)
# for key in student:
#     print(key)

# for key in student:
#     print(key, student[key])

# if "name" in student:
#     print("van neve")

# print(len(student))

# student.pop("name")
# del student["name"]
# print(student)

# Python program, ami 1->n (felhasználó által van megadva) olyan dictionary-t adjon vissza, amiben {x: x*x} x->1:n

# n = int(input('Meddig írjuk ki? '))
# d = dict() # {}
# for x in range(n):
#   d[x] = x ** 2

# print(d)
# osztaly = [
#     {"name": "Alice", "classes": ["Math"], "age": 19},
#     {"name": "Bob"},
#     {"name": "Bob", "classes": ["English"], "age": 20},
# ]
# print(osztaly[0]["classes"][0])

# Az összeg egy dict-ben levő értéket összeadni?

# kosar = {
#     "item": 10,
#     "item2": 10,
#     "item3": 8,
#     "item4": 10,
#     "item5": 0,
#     "item6": 6,
#     "item7": 1,
# }
# sum = 0

# for key in kosar:
#   sum += kosar[key]
# print(sum)
# sum = 0
# for value in kosar.values():
#   sum += value
# print(sum)

# students = {
#     "id1": {"name": "Alice", "class": "C"},
#     "id2": {"name": "Alice", "class": "C"},
#     "id3": {"name": "Bob", "class": "C"},
#     "id4": {"name": "John", "class": "D"},
# }
# szűrjük ki a duplikált elemeket
# clean_students = {}

# def exists(name):
#   for x in clean_students:
#     if clean_students[x]['name'] == name:
#       return True
#   return False

# for student in students:
#   if not exists(students[student]['name']):
#     clean_students[student] = students[student]

# print(clean_students)

students = [
    {"id": 1, "name": "Alice", "success": False},
    {"id": 2, "name": "Bob", "success": True},
    {"id": 3, "name": "John", "success": True},
]
# # számoljuk meg, hogy hányan mentek át (success == True)
# sum = 0
# for student in students:
#   if student['success']:
#     sum += 1
# print(sum)

# bemeneti string a felhasználótól, illetve egy eltolási szám, 'h' + 1 -> 'i'
# hello, 4 -> 'lipps'
# ord(character) -> number
# chr(number) -> character

# szoveg = input('Mi legyen a bemenet? ')
# shift_num = int(input('Mennyivel legyen eltolva? '))

# def shift(char, num):
#   new_c = ord(char) + num
#   return chr(new_c)

# def unshift(char, num):
#   new_c = ord(char) - num
#   return chr(new_c)

# def encode(string, num):
#   code = ""
#   for c in string:
#     code += shift(c, num)
#   return code

# def decode(t):
#   code = ""
#   for c in t[0]:
#     code += unshift(c, t[1])
#   return code
# string = 'hello'
# num = 4
# encoded = (encode(string, num), num)
# decoded = decode(encoded)
# print(decoded, encoded)

# n_string = ''
# for c in szoveg:
#   n_string += chr(ord(c) + shift_num)

# print(n_string)

# morse kódoló illetve dekódoló
alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
}
encode_morse = 'hello' #input('Mit szeretnél lemorse-zni? ')
# decode_morse = input('Mit szeretnél visszafejteni? ')

def encode(string):
  code = ''
  for c in encode_morse:
    code += alphabet[c.upper()] + ' '
  return code

def decode(string):
  pass


print(decode(encode(encode_morse)))
