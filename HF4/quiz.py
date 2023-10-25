import random

import question


questions = list[question.Question]()


def take_quiz():
    score = 0
    random.shuffle(questions)
    for q in questions:
        result = q.ask()
        score += result
    print(f"You got {score} correct out of {len(questions)}.")


def add_question():
    print("Select question type:")
    types = [q for q in question.Question.__subclasses__()]
    for i, qtype in enumerate(types):
        print(f"{i + 1}. {qtype.__name__}")
    choice = int(input("Enter choice: "))
    qtype = types[choice - 1]
    questions.append(qtype.create_question())
    with open("questions.txt", "w", encoding="utf-8") as f:
        for q in questions:
            f.write(repr(q) + "\n")


def main_menu():
    while True:
        print("Welcome to the Quiz!")
        print("1. Take the Quiz")
        print("2. Add a question")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            take_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    try:
        with open("questions.txt", encoding="utf-8") as f:
            from question import *  # noqa: F401, F403
            for line in f:
                questions.append(eval(line))
        print(f"Successfully loaded {len(questions)} questions.")
    except FileNotFoundError:
        print("No questions found.")
    except Exception as e:
        print("Error loading questions:", e)
    main_menu()
