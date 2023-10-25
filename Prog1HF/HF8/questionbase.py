import json
questions = list[dict]()

QUESTION_TYPES = ["MCQ", "text", "number", "true/false"]
DATABASE_FILE = "quiz.json"
def read_from_file(filename: str):
    with open(filename) as db:
        data = json.load(db)
    return data

data = read_from_file(DATABASE_FILE)
# for i, question in enumerate(data, 1):
#     print(f"\n{i}. kérdés: {question['question']}")

def write_to_file(filename: str, data):
    with open(filename, 'w') as update:
        json.dump(data, update, indent=4)

def mcq(question):
    print("Write the correct answer first, then add some other (wrong) options. Press Enter if you wish to stop.")
    options = []
    option = None
    while option != "":
        option = input("Input: ")
        options.append(option)
    options = options[:-1]
    round = {
        "question": question,
        "type": "MCQ",
        "answers": options
    }
    return round

def text(question):
    correct = input("Now write the correct answer.\nInput: ")
    round = {
        "question": question,
        "type": "text",
        "correct": str(correct)
    }
    return round

def number(question):
    correct = input("Now write the correct answer.\nInput: ")
    tolerance = input("Write tolerance (how far a player can guess at best for it to be still right). Can be any number.\nInput: ")
    round = {
        "question": question,
        "type": "number",
        "correct": correct,
        "tolerance": tolerance
    }
    return round

def tf(question):
    correct = input("Now write the correct answer.\nInput: ")
    round = {
        "question": question,
        "type": "true/false",
        "correct": bool(correct)
    }
    return round

def add_q():
    print("Choose one of the following question types:\n0) Exit")
    for i, type in enumerate(QUESTION_TYPES, 1):
        print(f"{i}) {type}")
    answer = input("Input a number: ")
    while not answer.isdigit() or int(answer) > len(data) or int(answer) < 0:
        answer = (input(f"You need to give a whole number between 0 and {len(data)+1}.\nInput: "))
    answer = int(answer)
    if (answer < len(data) and answer > 0):
        question = input(f"You have selected {QUESTION_TYPES[answer-1]}. Write the content of the question below.\nInput: ")
        if answer == 1:
            data.append(mcq(question))
        if answer == 2:
            data.append(text(question))
        if answer == 3:
            data.append(number(question))
        if answer == 4:
            data.append(tf(question))
        write_to_file(DATABASE_FILE, data)
        print("Done and dusted! Returning to menu...")
        return add_q()
    
    if answer == '0':
        print("Returning to main menu...")
        return

def delete_q():
    while True:
        print("Which question do you want deleted? Type a number. (0 - ESC)")
        for i, question in enumerate(data, 1):
            print(f"{i}. kérdés: {question['question']}") 
        answer = input("Input: ")
        while not answer.isdigit() or int(answer) > len(data) or int(answer) < 0:
            answer = (input(f"You need to give a whole number between 0 and {len(data)+1}.\nInput: "))
        
        if (int(answer) <= len(data) and int(answer) > 0):
            confirm = input("Are you sure you want the question deleted? Y/N\nInput: ")
            if any(confirm.lower() == valid_input.lower() for valid_input in ["true", "T", "yes", "Y"]):
                del data[int(answer)-1]
                print("Succesfully deleted.")
                write_to_file(DATABASE_FILE, data)
        
        if answer == '0':
            print("Returning to main menu...")
            return
        