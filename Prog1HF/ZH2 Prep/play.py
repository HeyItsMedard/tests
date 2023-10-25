import os
#scene directory: /workspaces/prog1-23t-zh2gyak-HeyItsMedard/hamlet-demo
def load_play(directory: str) -> dict[str, list[str]]:
    """Loads the scenes of a play from the given directory.

    Args:
        directory (str): Path to the directory which contains the scenes.

    Returns:
        A dict where the keys are the scene names (filename without ext.), values are
        lists containing the names of the speaking characters.

    Raises:
        FileNotFoundError: The directory was not found.
    """
    scene_dict = {}
    for filename in os.listdir(directory):
        with open(f'{directory}/{filename}',"r") as f:
            key = filename.split('.')[0]
            value = []
            for line in f:
                if line.isupper():
                    value.append(line.split('\n')[0])
            scene_dict[key] = value
    return scene_dict

# print(load_play("/workspaces/prog1-23t-zh2gyak-HeyItsMedard/hamlet-demo"))

def get_speech_count(play: dict[str, list[str]]) -> int:
    """Counts the total number of speeches in all scenes of a play.

    Args:
        play (dict[str, list[str]]): Scene names and character names.

    Returns:
        int: The total number of speeches.
    """
    speeches = 0
    #print(play)
    for values in play.values():
        # print(values)
        for speech in values:
            speeches+=1
    return speeches

#print(get_speech_count(load_play("/workspaces/prog1-23t-zh2gyak-HeyItsMedard/hamlet-demo")))

def inorder(s):
    parts = s.split('-')
    return int(parts[1]), int(parts[3])

def get_char_scenes(char, folder):
    found = False
    scene_dict = load_play(folder)
    char_in_scenes = []
    for key, values in scene_dict.items():
        if char in values:
            char_in_scenes.append(key)
    scenes_in_order = sorted(char_in_scenes, key=inorder)
    for scene in scenes_in_order:
        print(scene)
    if len(scenes_in_order) == 0:
        print("Error: No character with this name.")

def char_count(folder):
    scene_dict = load_play(folder)
    speech_per_char = {}
    for values in scene_dict.values():
        for speech in values:
            if speech not in speech_per_char:
                speech_per_char[speech] = 1
            else:
                speech_per_char[speech] += 1
    for key, val in speech_per_char.items():
        print(f'{key}: {val}')