import json
import os
from database import write_to_file, read_from_file, check_answer

def highscore_lists():
    """'Highscore lists' menu from main"""
    json_file_names = [filename for filename in os.listdir('highscores') if filename.endswith('.json')]
    print("Válassz egy highscore listát!")
    for i, filename in enumerate(json_file_names, 1):
        print(f"{i}) {filename}")
    answer = input("Szám: ")
    answer = check_answer(len(json_file_names), answer)
    highscore_list = read_from_file(f"highscores/{json_file_names[int(answer)-1]}")
    print(f"\n{json_file_names[int(answer)-1].split('_')[0].capitalize()} - {json_file_names[int(answer)-1].split('_')[1].split('.')[0].capitalize()} Difficulty")
    for i, player in enumerate(highscore_list, 1):
        print(f'{i}. hely: {player["name"]}: \t{player["points"]} pont')

def order_highscore(filedata: list):
    """Orders the highscore list after added new data.
    Arg:
        filedata (list): data of the highscore list.
    Returns:
        list: ordered and reversed list based on earned points by players.
    """
    return sorted(filedata, key=lambda x: x['points'], reverse=True)

def playerFound(filedata: list, filename: str, highscore: int, player_name: str) -> bool:
    """A returning legend!... meaning they already appear on the top 10 list.
    Saves their record new record only if they have earned more points and sorts the list again.

    Args:
        player_name (str): player's name based on player input.
        filedata (list): data of the highscore list.
        filename (str): the highscore json files full name.
        highscore (int): points earned by current player.
    
    Returns:
        bool: used in write_highscore to decide if other function calls are necessary.
    """
    for i, player in enumerate(filedata):
        if player["name"] == player_name and player_name != "Anonymus": 
            PlayerFound = True
            if highscore > filedata[i]["points"]:
                filedata[i]["points"] = highscore
                filedata = order_highscore(filedata)
                write_to_file(filename, filedata)
                print("Mentve. A highscore lista a 6. menüpontban megtekinthető a főmenüből.")
            else:
                print("Ez a játékos ennél jobb vagy ugyonalyan pontszámot ért már el, nincs mentés!")
            return True
    return False

def newPlayer(player_name: str, highscore: int, filename: str, filedata: list):
    """A new player joins the list of legends!... meaning the top 10 players in a topic and difficulty.
    Saves new player and their record and sorts the list.

    Args:
        player_name (str): player's name based on player input.
        filedata (list): data of the highscore list.
        filename (str): the highscore json files full name.
        highscore (int): points earned by current player.
    
    """
    new_dict = {}
    new_dict['name'] = player_name
    new_dict['points'] = highscore
    filedata.append(new_dict)
    filedata = order_highscore(filedata)
    write_to_file(filename, filedata)
    print("Mentve. A highscore lista a 6. menüpontban megtekinthető a főmenüből.")

def write_highscore_if_eligible(topic_name: str, hard_difficulty: bool, highscore: int):
    """
    Saves record if the player has earned points to get a spot on the highscore list
    (that is by earning more than the last place on a full 10 player list, or simply getting added onto a highscore list if it's not full.)
    The player's name and highscore will be saved (if eligible and higher than zero, otherwise, nothing happens).
    Same player's highscore is saved only if they earned more than before (exc. "Anonymus"). On a full list, the last place won't be deleted in that case.
    
    Args:
        topic_name (str): the topic's name.
        highscore (int): points earned by current player.
        hard_difficulty (bool): the difficulty of the game.

    Calls: 
        newPlayer: if the name input wasn't found in the list.
        playerFound: if the name was found on the highscore. Updates the player's highscore if higher.
    """

    diff_name = "normal"
    if hard_difficulty is True:
        diff_name = "hard"

    highscore_path =  f"highscores/{topic_name}_{diff_name}.json"
    
    if not os.path.isfile(highscore_path):
        with open(highscore_path, 'w', encoding="utf8") as update:
            json.dump([], update, ensure_ascii=False, indent=4)

    highscore_data = read_from_file(highscore_path)

    try:
        min_value = min(highscore_data, key=lambda x: x['points'])['points']
    except KeyError:
        min_value = 0
    except ValueError:
        min_value = 0
        # Remove dictionaries with the minimum value
    if len(highscore_data) == 10 and min_value < highscore:
        player_name = input("A highscore listához írd be a neved: ")
        if player_name == "":
            player_name = "Anonymus"
        # update if player got a better score, don't include more times (except Anonymus) 
        PlayerFound = playerFound(highscore_data, highscore_path, highscore, player_name)
        if not PlayerFound:
            # if len(highscore_data) == 10 and min_value < highscore:
            highscore_data.pop(9)
            newPlayer(player_name, highscore, highscore_path, highscore_data)
    elif len(highscore_data) < 10 and highscore > 0:
        player_name = input("A highscore listához írd be a neved (Enter esetén Anonymus): ")
        if player_name == "":
            player_name = "Anonymus"
        # update if player got a better score, don't include more times (except Anonymus)
        PlayerFound = playerFound(highscore_data, highscore_path, highscore, player_name)
        # if new player
        if not PlayerFound:
            newPlayer(player_name, highscore, highscore_path, highscore_data)