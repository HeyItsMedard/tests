# # Old version
# res = {
#     "dob": "1999-01-01 12:00:00"
# }

# # New version
# res2 = {
#     "dob": {
#         "date": "1998-01-01 12:00:00",
#         "age": 25
#     }
# }

# def get_age(user):
#     match user:
#         case { "dob": { "age": int(age) } }:
#             return age
#         case { "dob": dob }:
#             from datetime import datetime
#             now = datetime.now()
#             dob_date = datetime.strptime(dob, '%Y-%m-%d %H:%M:%S')
#             return now.year - dob_date.year

# print(get_age(res))
# print(get_age(res2))

# def sum_list(numbers):
#     match numbers:
#         case []:
#             return 0
#         case [int(first) | float(first), *rest]:
#             return first + sum_list(rest)
#         case _:
#           raise ValueError("Can only sum numbers")


# print(sum_list([1.0, 2.0, 3.1]))

# def fizzbuzzbasic(number):
#     mod_3 = number % 3
#     mod_5 = number % 5
#     if mod_5 == 0 and mod_3 == 0:
#         print('fizzbuzz')
#     elif mod_3 == 0:
#         print('fizz')
#     elif mod_5 == 0:
#         print('buzz')
#     else:
#         print(number)

# def fizzbuzzmatch(number):
#     mod_3 = number % 3
#     mod_5 = number % 5

#     match (mod_3, mod_5):
#         case (0, 0):
#             print('fizzbuzz')
#         case (_, 0):
#             print('buzz')
#         case (0, _):
#             print('fizz')
#         case _:
#             print(number)

# fizzbuzzmatch(4)
# fizzbuzzbasic(4)

# def grade(score):
#     print(score)
#     match(score):
#         case s if s in range(90, 101):
#             return 'A'
#         case s if s in range(60, 90):
#             return 'B'
#         case _:
#             return 'F'

# print(grade(100))

# try:
#   print(0 / 1)
#   # raise ValueError('nono')
#   input_path = 'main.pyy'
#   fi = open(input_path)
#   with open(input_path) as f:
#      print(f.read())
# except ZeroDivisionError:
#   print('Please use correct math')
# except ValueError as e:
#   print('valami nem ok', e)
# except FileNotFoundError:
#   try:
#     with open('error.txt', 'r') as f:
#       f.write('valami error volt')
#   except:
#     print('valami nagyon nem ok')
# else:
#   print('ide értem')
# finally:
#   print('valamilyen futás van éppen')
#   with open('log.log', 'a') as f:
#     f.write('running')
#   fi.close()

dob = {
  "dob": 0
}
for i in range(10):
  try:
    dob['array'].append(i)
  except:
    dob['array'] = [i]
print(dob)
