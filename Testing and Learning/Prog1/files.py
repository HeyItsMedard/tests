# file = open('demo.txt', "a")
# file.write('hello\n')
# file.write('world\n')
# file.close()

# file = open('demo.txt')
# print(file.read())
# file.readlines()
# for line in file:
#     print(line, end="")
# file.close()

# with open('demo.txt') as file:
#     for line in file:
#         print(line, end="")

# with open('demo.txt') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end="")

import json

room = {
    "students": [
        {
            "name": 'Bob',
            "age": 10
        },
        {
            'name': 'Alice',
            "age": 10,
        },
        {
            'name': 'Jane',
            "age": 10
        }
    ],
}

# print(room)
# room_as_json = json.dumps(room)
# print(room_as_json)
# file = open('room.json', 'a')
# json.dump(room, file)

# file = open('room.json')
# print(json.load(file))
# room_as_python = json.loads(room_as_json)
# print(room_as_python['students'])
# with open('room.json') as file:
#     data = file.readline()
#     data = json.loads(data)
#     print(data['students'])

# User nevét és az életkorát várja és kimenti a user.txt-be

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# with open('user.txt', "a") as file:
#     file.write(f'Name: {name}, Age: {age}')

# Same de json-ként lenne kimentve user.json-be

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# import json
# with open('user.json', 'w') as file:
#     json.dump({
#         "name": name,
#         "age": age
#     }, file)

# input.txt-ből olvas sorokat és kimenti az 5 karakternél hosszabb sorokat egy új fileba
# with open('input.txt') as file:
#     for line in file:
#         if len(line) > 5:
#             with open('output.txt', "a") as file2:
#                 file2.write(line)

# with open('input.txt') as input, open('output.txt', 'w') as output:
#     for line in input:
#         if len(line)> 5:
#             output.write(line)

# data.json benne name,age párok vannak dictionary-ben és ezeket szereném kiírni

# import json
# with open('data.json') as file:
#     data = json.load(file)
#     for person in data:
#         print(f"Name: {person['name']}, Age: {person['age']}")

# basket.json és össze kell számolni hogy mennyi a kosár tartalmának értéke

import json
with open('basket.json') as file:
    basket = json.load(file)
    sum = 0
    for item in basket:
        sum += item['count'] * item['price']
    print(sum)

import csv

with open('test.csv') as file:
    d = csv.reader(file)
    for (name, age, subject) in d:
        print(name, int(age) + 1, subject)
