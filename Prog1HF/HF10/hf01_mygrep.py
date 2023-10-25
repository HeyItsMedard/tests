import argparse
import os

def search_string_in_file(file_path, search_string, ignore_case):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if ignore_case:
                    if search_string.upper() in line.upper():
                        print(f"{file_path}:{line_number}: {line.rstrip()}")
                else:
                    if search_string in line:
                        print(f"{file_path}:{line_number}: {line.rstrip()}")
                        # for each line that contains the searched string, print it in this format:
                        # filename:line_number: line
                        # example: targyak/2022_osz.csv:2: ABC123;1;4
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def search_string_in_directory(directory, search_string, ignore_case, recursive):
    for root, _, files in os.walk(directory): #nem keresünk több folderben
        for file in files:
            file_path = os.path.join(root, file)
            search_string_in_file(file_path, search_string, ignore_case)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Searches for a string in one or more files."
    )
    parser.add_argument("string", help="the string to search for")
    parser.add_argument(
        "path", nargs="+", type=str, help="file or directory to search in"
    )
    parser.add_argument(
        "-i",
        "--ignore-case",
        action="store_true",
        help="make the search case-insensitive",
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="search directories recursively"
    )
    
    # TODO: parse arguments
    args = parser.parse_args()
    search_string = args.string
    paths = args.path
    ignore_case = args.ignore_case
    recursive = args.recursive
    
    for path in paths:
        if os.path.isfile(path):
            search_string_in_file(path, search_string, ignore_case) # search for the string in the given path(s)
        elif os.path.isdir(path): # if the path is a directory, search in all files in that directory
            if recursive: # if the recursive flag is set, search in all subdirectories too
                search_string_in_directory(path, search_string, ignore_case, recursive)
            else:
                for file in os.listdir(path):
                    file_path = os.path.join(path, file)
                    if os.path.isfile(file_path):
                        search_string_in_file(file_path, search_string, ignore_case)
        else:
            print(f"Invalid path: {path}")