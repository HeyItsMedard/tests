import questionbase
from play import quiz


def main_menu():
    # TODO load questions from file
    while True:
        print("""
MAIN MENU
Choose an option:
1 - Play quiz
2 - Add questions
3 - Delete questions
0 - Exit""")
        option = int(input("Enter number: "))
        if option == 0:
            break
        elif option == 1:
            quiz()
        elif option == 2:
            questionbase.add_q()
            pass  # TODO
        elif option == 3:
            questionbase.delete_q()
            pass  # TODO
        else:
            print("Invalid option, try again.")
    print("Goodbye!")
    # TODO save questions to file


if __name__ == "__main__":
    main_menu()
