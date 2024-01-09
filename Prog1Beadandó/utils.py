import sys
import subprocess

class Utils:
    @staticmethod
    def check_answer(length: int, answer: str) -> int:
        """Checks if the user input is an existing menu option.
        If not, it keeps asking until player doesn't give an existing option.

        Args:
            length (int): the number of possible menu options.
            answer (str): the given input of the user.
        Returns:
            answer (int): the final given numeral input of the user.
        """
        while not answer.isdigit() or int(answer) > length or int(answer) < 0:
            answer = (input(f"Számot kell megadj 0-tól {length}-ig.\nSzám: "))
        return int(answer)

    @staticmethod
    def help():
        """Reads and prints the help file (README.md). Runs when selected in menu under 6th.
        UTF-8 is used for handling Hungarian letters.

        Prints:
            content: the help file's content.
        Raises:
            FileNotFoundError: when the help file is missing
        """
        try:
            with open("README.md", "r", encoding="utf-8") as file:
                content = file.read()
            print(content)
        except FileNotFoundError:
            print("Hiányzó HELP fájl a könyvtárban.")

    @staticmethod
    def restart_from_main():
        """Reloading the game.
        Necessary when operating with topics (json files).
        """
        python = sys.executable
        subprocess.Popen([python, "main.py"]).wait()
        sys.exit()
