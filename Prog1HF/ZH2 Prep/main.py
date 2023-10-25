import play
import scene
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=False)
    args = parser.parse_args()
    if args.directory is None or not os.path.isdir(args.directory):
        folder = input("Error: Directory not found. Invalid folder, try again:")
        while not os.path.isdir(folder):
            folder = input("Error: Directory not found. Invalid folder, try again:")
    else:
        folder = args.directory

    """The Main Menu of the program."""
    # TODO load play from argument or user input
    while True:
        print(f"\nCurrently opened play: {folder}")  # TODO
        print(f"Total number of speeches: {play.get_speech_count(play.load_play(folder))}")  # TODO
        print(
            """
Main menu:
1: Open a play from a directory
2: List scenes of a character
3: Display number of speeches by characters
0: Exit"""
        )
        choice = input("Select a menu option: ")
        # TODO handle choice with match-case
        match choice:
            case '0':
                break
            case '1':
                getdir = input("Input folder: ")
                if os.path.isdir(getdir):
                    folder = getdir
                else:
                    print("Error: Directory not found.")
            case '2':
                getchar = input("Input character: ").upper()
                play.get_char_scenes(getchar, folder)
            case '3':
                play.char_count(folder)
                pass
            case _:
                print("Error: Invalid option.")

if __name__ == "__main__":
    main()
