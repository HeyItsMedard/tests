#scene directory: /workspaces/prog1-23t-zh2gyak-HeyItsMedard/hamlet-demo
def load_scene(filename: str) -> list[str]:
    """Loads the script of a scene and returns the speaking order of the characters.

    It is assumed that the file contains speeches and stage directions.
    Each speech:
    - starts with a line containing only the uppercase name of the speaking character
    - followed by the lines of the speech
    - ended by an empty line
    Stage directions are written in square brackets.

    Args:
        filename (str): Path to a textfile containing the script of a scene.

    Returns:
        A list containing the name of the speaking character for each speech.

    Raises:
        FileNotFoundError: The file was not found.

    >>> names = load_scene("hamlet-demo/act-1-scene-1.txt")
    >>> len(names)
    60
    >>> names[-5:]
    ['BARNARDO', 'HORATIO', 'MARCELLUS', 'HORATIO', 'MARCELLUS']
    """
    chars = []
    try:
        with open(f'{filename}',"r") as f:
            for line in f:
                if line.isupper():
                    chars.append(line.split('\n')[0])
        return chars
    except FileNotFoundError:
        print("File not found.")


# names = load_scene("act-1-scene-1.txt")
# print(len(names), names[-5:]) 