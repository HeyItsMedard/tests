from questionbase import read_from_file
import random
from string import ascii_lowercase as abc
from fractions import Fraction


def mcq(question):
    correct = question['answers'][0]
    random.shuffle(question['answers'])
    print("Válasszon a következő lehetőségek közül karakterrel:")
    for i in range(len(question['answers'])):
        print(f"{abc[i]}) {question['answers'][i]}")
        if (question['answers'][i] == correct):
            correct_input = abc[i]
    answer = input("Input: ")
    if (answer.lower() == correct_input.lower()):
        return 1
    else:
        return 0

def is_float(input_str):
    try:
        float_value = float(input_str)
        return True
    except ValueError:
        return False

def check_type(getvalue, answer):
    if getvalue['type'] == 'text' and answer.lower() == getvalue['correct'].lower():
        return 1
    if getvalue['type'] == 'true/false' and (any(answer.lower() == valid_input.lower() for valid_input in ["true", "T", "yes", "Y", "false", "F", "no", "N"])):
        if answer.lower() == str(getvalue['correct']).lower():
            return 1
    if getvalue['type'] == 'number': #isdigit és társai nem jó törtre
        try:
            if is_float(Fraction(answer)):
                if float(answer) == float(getvalue['correct']):
                    return 1
                elif 'tolerance' in getvalue:
                    guess = float(answer) - float(getvalue['correct']) #44.5-44=0.5, 43.5-44=-0.5
                    if abs(guess) <= float(getvalue['tolerance']):
                        return 1
                    else:
                        return 0
        except ValueError:
            return 0
    else:
        return 0
            
def quiz():

    questions = read_from_file("quiz.json")
    count = len(questions)
    random.shuffle(questions)

    rounds = (input(f"There are {count} rounds available. How many rounds do you want to play? (0 - ESC)\nInput: "))
    if rounds == '0':
        return
    while not rounds.isdigit() or int(rounds) > count or int(rounds) < 1:
        rounds = (input(f"You need to give a whole number between 1 and {count+1}.\nInput: "))
    
    rounds = int(rounds)
    questions = questions[:rounds]

    score = 0
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. kérdés: {question['question']}")
        if question['type'] == 'MCQ': # ki kell írni a tartalmát, mielőtt választ adunk
            print("Answer with letter!")
            score += mcq(question)
        else:
            print(f"Answer with {question['type']}!")
            answer = input("Input: ")
            score += check_type(question, answer)

    print(f"\nScore: {score}/{rounds} correct answer.")
    return
   