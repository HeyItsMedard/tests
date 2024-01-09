import json
import os
from utils import Utils

class MissingTopicsError(Exception):
    "Raised when there are no topic files to."
    
# Set the path to the folder
folder_path = "Prog2Beadandó"

# Change the current working directory to the specified folder
os.chdir(folder_path)

# Print the list of files in the current directory
print(os.listdir())

# List of JSON file names in the current directory
json_file_names = [filename for filename in os.listdir() if filename.endswith('.json')]
print(json_file_names)

if len(json_file_names) == 0:
    raise MissingTopicsError("Hiányzó téma adatbázis fájlok a könyvtárban.")

class Database:
    @staticmethod
    def read_from_file(filename: str) -> list:
        """Reads and returns a list of contents from a json topic file.
        UTF-8 is used for handling Hungarian letters.

        Args:
            filename (str): the topic json file's full name

        Returns:
            data (list): contains content creators and their contents.
        """
        try:
            with open(filename, 'r', encoding="utf8") as db:
                data = json.load(db)
            return data
        except json.decoder.JSONDecodeError:
            with open(filename, 'w', encoding="utf8") as update: #creating empty json file and then reading it 
                # a highscore problem, when the json gets empty upon facing a problem, this won't be necessary anywhere but here (also see JSONERROR.txt)
                # help is much appreciated for handling this error elsehow
                json.dump([], update, ensure_ascii=False, indent=4)
            with open(filename, 'r', encoding="utf8") as db:
                data = json.load(db)
            return data

    @staticmethod
    def write_to_file(filename: str, data):
        """Writes into topic json file.
        UTF-8 is used for handling Hungarian letters.

        Args:
            filename (str): the full name of the topic json file.
            data (list): the updated content of a topic.
        """
        with open(filename, 'w', encoding="utf8") as update:
            json.dump(data, update, ensure_ascii=False, indent=4)

    @staticmethod
    def confirm_deletion(answer: int, where: list, filedata:list, filename: str):
        """Deletes the selected data on confirmation.

        Args:
            filename (str): the full name of the topic json file.
            answer (int): the given input of the user.
            where (list/dict): the list where we are looking for chosen data (creator/video)
            filedata (list): the content of a topic.

        Calls:
            write_to_file: updates data of json file
        """
        confirm = input("Biztos szeretnéd törölni az adatot? I/N\nSzöveges bevitel: ")
        if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
            if isinstance(where, list):
                del where[answer-1]
            else:
                keys = list(where.keys())
                del where[keys[answer-1]]
            print("Törölve.")
            Database.write_to_file(filename, filedata)

    @staticmethod
    def get_topic_index():
        """Prints out possible topics, then asks the player for input.

        Returns:
            answer (int): the final given input of the user.
        Calls:
            check_answer(length: int, answer: str): checks if the user has given a correct input.
        """
        print("Válassz témát (0 - ESC):")
        for i, jsonf in enumerate(json_file_names, 1):
            print(f"{i}) {(jsonf.split('.')[0]).capitalize()}")
        answer = input("Szám: ")
        answer = Utils.check_answer(len(json_file_names), answer)
        return answer

    @staticmethod
    def get_topic_file(answer: int) -> list:
        """Gets the data of a topic chosen by user
        Arg:
            answer (int): the given input of the user.
        Returns:
            list: data of a topic.
        """
        return Database.read_from_file(json_file_names[answer-1])

    @staticmethod
    def get_topic_name(answer: int) -> str:
        """Gets the name of the topic.
        Arg:
            answer (int): the given numeral input of the user.
        Returns:
            str: the name of the topic.
        """
        return json_file_names[answer-1].split('.')[0].lower()

    @staticmethod
    def list_creators(filedata: list) -> str:
        """Lists creators of a topic.
        Arg:
            filedata (list): the content of a topic.
        Prints:
            str: the list of creators in topic.
        """
        print("Melyik tartalomgyártó? (0 - ESC)")
        for i, creator in enumerate(filedata, 1):
            print(f"{i}) {creator['creator']}")

    @staticmethod
    def list_content(creator_data: list) -> str:
        """Lists contents of a creator.
        Arg:
            creator_data (list): the content of a topic.
        Prints:
            str: the list of contents of a creator.
        """
        print("Melyik tartalom? (0 - ESC)")
        for i, content in enumerate(creator_data, 1):
            print(f"{i}) {content}")

    @staticmethod
    def print_change_data():
        """Prints out which data should be changed."""
        print("""
    Min szeretnél változtatni?
    1) Tartalomgyártó
    2) Tartalom
    3) Téma
    0) Kilépés\r""")
    
    @staticmethod
    def write_content_for_creator() -> dict:
        """Writing content for creator by user.
        Returns:
            dict(dict(str: int)): list of videos written by user.
        """
        video_dict = {}
        while True:
            video_name = input("Add meg a tartalom nevét (Enterre kilép): ")
            
            # User presses Enter
            if video_name == "":
                break
            
            TitleFound = False
            # Check if user input matches a title from the same creator
            for dictionary in video_dict:
                if video_name in dictionary:
                    print("A tartalom létezik már a listában!")
                    TitleFound = True
                    break
            
            # Write views and add to list of videos if it already doesn't exist
            if not TitleFound:
                views = input("Add meg a tartalom nézettségét (szám): ")
                while not views.isdigit() or int(views) < 0:
                    views = (input(f"0-nál nagyobb számot kell megadj! \nSzám: "))
                                
                video = {video_name: int(views)}
                video_dict.update(video) #UPDATE
        if len(video_dict) > 0:
            return video_dict

    @staticmethod
    def delete_topic(filename: str):
        """Deleting topic by user.
        Arg:
            filename (str): the chosen topic of user.
        Calls:
            restart_from_main(): restarting for applying changes
        """
        
        confirm = input("VIGYÁZAT! Ez a művelet töröl egy egész témát és annak highscore listáit! Folytatod? I/N: ")
        if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
            topic = filename.split('.')[0]  

            # Delete the JSON file in main folder
            if os.path.exists(filename):
                os.remove(filename)
                print(f"'{filename}' eltávolítva.")

            # Delete any JSON file in the highscores folder with the topic name as a substring
            for filename in os.listdir("highscores"):
                if topic in filename and filename.endswith(".json"):
                    file_path = os.path.join("highscores", filename)
                    os.remove(file_path)
                    print(f"'{file_path}' eltávolítva.")
            
            # Restarting to update data - else, changes won't be visible in current process
            print("Újraindítás...")
            Utils.restart_from_main()

    @staticmethod
    def add_data():
        """'Add data' menu from main"""
        while True:

            # choosing data
            Database.print_change_data()

            num_vid = input("Szám: ")
            num_vid = Utils.check_answer(3, num_vid)

            # create a brand new topic file - a separate action from others
            if num_vid == 3: #topic
                filename = input("Mi legyen a téma?\nSzöveges bemenet: ")
                if filename != "":
                    Database.write_to_file(f"{filename.lower()}.json", [])
                    print("Létrehozva. További adatokat az 'adat hozzáadása' menüben tudsz hozzáadni!")
                    print("Újraindítás...")
                    Utils.restart_from_main()

            # check if esc
            elif num_vid != 0:
                # choosing topic with a number
                answer = Database.get_topic_index()
                if answer == 0:
                    return

                # gets topic data and filename
                topic_data = Database.get_topic_file(answer)
                print(topic_data)
                topic_file = (f"{Database.get_topic_name(answer)}.json")
                content_creators = [creator_data['creator'] for creator_data in topic_data]

                # check if user has chosen channel or content
                channel_dict = {}
                if num_vid == 1: # channel
                    while True:
                        channel_name = input("Add meg a csatorna nevét (Enterre kilép): ")

                        # User presses Enter
                        if channel_name == "":
                            break

                        # Check if channel already exists
                        if channel_name in content_creators:
                            print("Ez a csatorna már létezik az adatbázisban!")

                        # User writes content for creator
                        else:
                            video_dict = Database.write_content_for_creator()
                            channel_dict["creator"] = channel_name
                            channel_dict["contents"] = video_dict
                            topic_data.append(channel_dict)
                            Database.write_to_file(topic_file, topic_data)
                            print("Mentve.")
                            break

                if num_vid == 2: # video
                    Database.list_creators(topic_data)

                    # User chooses a channel
                    answer = input("Szám: ")
                    answer = Utils.check_answer(len(topic_data), answer)
                    if answer == 0:
                        print("Visszatérés főmenübe...")
                        return

                    # User writes content for existing creator
                    video_dict = Database.write_content_for_creator()
                    if video_dict is not None:
                        creator = topic_data[answer-1]
                        list_of_titles = []
                        for content in creator["contents"].keys():
                            list_of_titles.append(content)
                        print(list_of_titles)
                        for video, views in video_dict.items():
                            if video not in list_of_titles:
                                creator["contents"].update({video: views})
                        Database.write_to_file(topic_file, topic_data)
                        print("Mentve.")
                    break

            else:
                print("Visszatérés főmenübe...")
                return

    @staticmethod
    def delete_data():
        """'Delete data' menu from main"""
        while True:

            # choosing data
            Database.print_change_data()

            num_vid = input("Szám: ")
            num_vid = Utils.check_answer(3, num_vid)

            # check if esc
            if num_vid != 0:
                answer = Database.get_topic_index()
                if answer == 0:
                    return

                # gets topic data and filename
                topic_data = Database.get_topic_file(answer)
                topic_file = (f"{Database.get_topic_name(answer)}.json")

                if num_vid == 3: # topic
                    Database.delete_topic(topic_file)
                else: # creator/content
                    Database.list_creators(topic_data)
                    answer = input("Szám: ")
                    answer = Utils.check_answer(len(topic_data), answer)

                    if answer == 0: # esc
                        print("Visszatérés főmenübe...")
                        return

                    if num_vid == 1: # creator
                        Database.confirm_deletion(answer, topic_data, topic_data, topic_file) #szám, adat, fájl

                    if num_vid == 2: # content
                        # gets chosen channel's content
                        creator_contents = topic_data[answer-1]['contents']
                        Database.list_content(creator_contents)
                        answer = input("Szám: ")
                        if answer == 0: # esc
                            print("Visszatérés főmenübe...")
                            return
                        answer = Utils.check_answer(len(creator_contents), answer)
                        Database.confirm_deletion(answer, creator_contents, topic_data, topic_file)

            else:
                print("Visszatérés főmenübe...")
                return

    @staticmethod
    def edit_data():
        """'Edit data' menu from main"""
        while True:
            # choosing data
            Database.print_change_data()

            num_vid = input("Szám: ")
            num_vid = Utils.check_answer(3, num_vid)

            # check if esc
            if num_vid != 0: 
                answer = Database.get_topic_index()
                if answer == 0: # esc
                    return

                topic_data = Database.get_topic_file(answer)
                topic_file = (f"{Database.get_topic_name(answer)}.json")

                content_creators = [creator_data['creator'] for creator_data in topic_data]

                if num_vid == 3: # topic
                    confirm = input("Témánál nevet tudsz szerkeszteni. Folytatod? I/N: ")
                    if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
                        # rename topic
                        new_filename = input(f"{topic_file.split('.')[0].capitalize()} átírása: ")
                        # handling None
                        if new_filename != "":
                            os.rename(topic_file, f"{new_filename}.json")
                            print("Újraindítás...")
                            Utils.restart_from_main()
                else:
                    Database.list_creators(topic_data)
                    answer = input("Szám: ")
                    answer = Utils.check_answer(len(topic_data), answer)
                    if answer == 0:
                        print("Visszatérés főmenübe...")
                        return

                    if num_vid == 1: # creator
                        confirm = input("Tartalomgyártóknál nevet tudsz szerkeszteni. Folytatod? I/N: ")
                        if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
                            creator = topic_data[answer-1]["creator"]
                            # rename creator
                            new_creator_name = input(f"{creator} átírása: ")
                            # checking channel's existence
                            if new_creator_name in content_creators:
                                # returns
                                print("Ez a csatorna már létezik az adatbázisban!")
                            # handling None
                            elif new_creator_name != "":
                                topic_data[answer-1]["creator"] = new_creator_name
                                Database.write_to_file(topic_file, topic_data)

                    if num_vid == 2: # video
                        num_of_data = answer-1
                        creator_contents = topic_data[num_of_data]['contents']
                        Database.list_content(creator_contents)
                        answer = input("Szám: ")
                        answer = Utils.check_answer(len(creator_contents), answer)
                        if answer == 0:
                            print("Visszatérés főmenübe...")
                            return 
                        keys_list = list(creator_contents.keys())  # Convert dictionary keys to a list
                        record_key = keys_list[answer-1]  # Access the record key by index
                        selected_content = {record_key: creator_contents[record_key]}
                        # print(content)
                        confirm = input("Tartalomnál a videó címét és a nézettségét lehet szerkeszteni. Folytatod? I/N: ")
                        if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
                            # rename video
                            new_content_name = input(f"{record_key} átírása (Enter lenyomása után változatlan marad): ")
                            # check if title already exists by that creator
                            TitleFound = False
                            if new_content_name in keys_list:
                                print("A videó létezik már a listában!")
                                TitleFound = True
                                break
                            # title is not in list
                            if not TitleFound:
                                # handling None
                                if new_content_name == "":
                                    new_content_name = record_key
                                new_content_views = input(f"{creator_contents[record_key]} átírása (szám, Enter lenyomása után változatlan marad): ")
                                # handling None
                                if new_content_views == "":
                                    new_content_views = creator_contents[record_key]

                                elif new_content_views != "":
                                    # ask for a number
                                    while (not new_content_views.isdigit() or int(new_content_views) < 0):
                                        new_content_views = (input(f"0 vagy nagyobb számot kell megadj!\nSzám: "))
                                    del topic_data[num_of_data]['contents'][keys_list[answer-1]]
                                    topic_data[num_of_data]['contents'].update({new_content_name: int(new_content_views)})
                                    Database.write_to_file(topic_file, topic_data)

            else:
                print("Visszatérés főmenübe...")
                return
