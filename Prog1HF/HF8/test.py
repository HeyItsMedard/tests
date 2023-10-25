# from fractions import Fraction
# #answer = input("Number: ")
# num = 0.543

# #print(float(answer), num, float(num), float(answer)+num, float(answer)+float(num), abs(float(answer)+ float(num)))
# #print(str(num).is)
# answer = input("Number: ")
# print(str(float(Fraction(answer))).isnumeric())

# def is_float(input_str):
#     try:
#         float_value = float(input_str)
#         return True
#     except ValueError:
#         return False
# print(is_float(Fraction(answer)))
# input_str = input("Enter a value: ").lower()
# valid_inputs = ["true", "T", "yes", "Y", "false", "F", "no", "N"]

# is_match = any(input_str == valid_input.lower() for valid_input in valid_inputs)
# print(is_match)
# DATABASE_FILE= "quiz.json"
# import json
# def get_q_and_num():
#     with open(DATABASE_FILE) as db:
#             data = json.load(db)
#             count = 0
#             for question in data:
#                 count += 1
#     return count, data
# _, data = get_q_and_num()
# print(len(data), data[0])
options = []
option = None
while option != "":
    option = input("Input: ")
    options.append(option)
options = options[:-1]
print(options)
# numb = 0.6
# print(round(numb))
# import json
# with open("quiz.json") as db:
#     data = json.load(db)
# print(data)
