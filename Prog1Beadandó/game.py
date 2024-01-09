from database import Database
from highscore import Highscore
import random
# from playsound import playsound # sound for game overs, unused for now
from inputimeout import inputimeout # timer

class Game:
    def __init__(self):
        pass
    
    @staticmethod
    def get_playlist(data) -> list:
        """Puts together a list of videos from a chosen topic.

        Args:
            data (list): The entire list of content creators and contents from a topic json file.

        Returns:
            playlist (list): Every video of a topic.
        """
        playlist = []
        for creator in data:
            for video in creator['contents'].items():
                playlist.append(video)
        return playlist

    @staticmethod
    def get_playlist(data) -> list:
        """Puts together a list of videos from a chosen topic.

        Args:
            data (list): The entire list of content creators and contents from a topic json file.

        Returns:
            playlist (list): Every video of a topic.
        """
        playlist = []
        for creator in data:
            for video in creator['contents'].items():
                playlist.append(video)
        return playlist

    @staticmethod
    def get_difficulty() -> bool:
        """Asks the player whether they want to play in Hard Mode.

        By default returns False, except when player answers with a possible combination of "igen".

        Returns:
            bool: False if Normal Mode, True if Hard Mode
        """
        show_creator = input("Nehéz fokozat bekapcsolása? (I/N)\nSzöveges bemenet: ")
        if any(show_creator.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
            return True
        return False

    def get_creator_of_content(content: tuple, data: list) -> str:
        """Gets the creator of content. Used for normal difficulty and music topic.

        Args:
            content (tuple): A specific content.
            data (list): The entire list of content creators and contents from a topic json file. This is where we look for a specific content.

        Returns:
            str: The creator's name of the content.
        """
        for creator in data:
            if (content[0], content[1]) in creator["contents"].items():
                return creator["creator"]

    @staticmethod
    def get_correct_answer(first_views: int, second_views: int) -> int:
        """Gets the correct answer. Comes into play when comparing to player answer.

        If it returns with 1, the first content has more views.
        If it returns with 2, the second content has more views.
        Finally, if 0, both content have equal views on it.

        Args:
            first_views (int): First content's viewcount.
            second_views (int): Second content's viewcount.

        Returns:
            int: The correct answer (0 if they are equal)
        """
        if second_views < first_views:
            return 1
        elif second_views > first_views:
            return 2
        return 0

    @staticmethod
    def react_to_points(points: int, length: int):
        """The game reacts with a message, based on how well the player was performing.

        Args:
            points (int): Points earned throughout the game by the player.
            length (int): The maximum possible questions' count. Necessary when the game runs out of questions.

        Prints:
            str: A funny response
        """
        zero = ["Te egy kő alatt élsz, vagy ennyire szerencsétlen kérdést kaptál? Próbálkozz újra!", 
                "Több mint a semmi! Ja nem...", "Hát lehetne ennél rosszabb?"]
        terrible = ["Felejtsük el, hogy ez megtörtént... Új játék?", f"... csak {points} pont? Rettenetes...", 
                    "Nagyjából ennyi pont választotta el a Dortmundot is egy bajnoki győzelemtől... idén is...",
                    "Ennél tudsz te jobbat is, hiszek benned!"]
        better = ["Szép szám bizony, de vajon tudsz ennél jobbat elérni?",
                  "Ügyes! Így tovább!", "Ez megérdemel egy virtuális hátveregést!",
                  "Ahogy VR Pisti is mondaná: \"Nem is rossz!\""]
        great = ["Aztamindenségit! Gratulálok az eredményhez!", "Ijesztően sokat tudsz!",
                 "Szép munka!"]
        max = ["Sikerült kivinned a játékot! Gratulálok!", 
               "A családod mikor látott utoljára? Csak egy kérdés... mert helyesen válaszoltál minden kérdésre! Lenyűgöző!",
               "Ez a játék vége. Tényleg. Nem vicc. Feladom. Le a kalappal. gg"]
        # The answer is chosen randomly, but based on earned points
        # Comment out playsound for Easter Eggs (note: sometimes they do not work).
        if points == 0:
            print(random.choice(zero))
            # playsound('sounds\\zero1.mp3') -> gave up again, error handling doesn't work on it, only commenting helps
        elif points <= 2:
            print(random.choice(terrible))
            # playsound('sounds\\\\\\bad1.mp3') -> gave up again, error handling doesn't work on it, only commenting helps
        elif points <= 6:
            print(random.choice(better))
            # playsound('sounds\\notbad.mp3') -> gave up again, error handling doesn't work on it, only commenting helps 
        elif points < length:
            print(random.choice(great))
            # playsound('sounds\\nice.mp3')
        elif points == length:
            print(random.choice(max))
            # playsound('sounds\\\max1.mp3')

    def play():
        # Player chooses topic
        answer = Database.get_topic_index()
        if answer == 0:
            return
        
        #Loads topic data and filename
        topic = Database.get_topic_file(answer)
        topic_name = Database.get_topic_name(answer)

        # Gets the list of content based on chosen topic, randomises order
        content_list = Game.get_playlist(topic)

        # If player answers to every question right, the game will print out a special message (referring to function "react_to_points")
        length_for_reaction = len(content_list)

        # There are not enough questions in the topic to be playable.
        if length_for_reaction <= 1:
            # Empty topic given
            print("Ez a téma jelenleg üres. Visszatérés...")
            return
        
        # Gets difficulty based on player input
        hard_difficulty = Game.get_difficulty()

        FirstRound = True
        points = 0

        # Game must end if there is only one content left
        while len(content_list) >= 2:

            # Check if this is the first round
            if FirstRound:
                # Generate first content randomly
                first = random.choice([i for i in range(len(content_list))])
                f_title, f_views = content_list[first]
                f_creator = Game.get_creator_of_content(content_list[first], topic)    
                FirstRound = False

            # Generate second content randomly
            second = random.choice([i for i in range(len(content_list)) if i != first])
            s_title, s_views = content_list[second]
            s_creator = Game.get_creator_of_content(content_list[second], topic) 

            # Gets correct answer based on views
            correct_answer = (Game.get_correct_answer(f_views, s_views))
            player_answer = ""

            # Player plays on normal difficulty
            if not hard_difficulty:
                
                print(f"""Melyiknek van több nézettsége?
            1) {f_creator}: {f_title} -> {f_views} nézőszám
            2) {s_creator}: {s_title} -> ??? nézőszám""")
                player_answer = (input("Szám: "))
                try:
                    # Awaits player input
                    player_answer = int(player_answer)
                # If they give a wrong input
                except ValueError:
                    break
            
            # Player plays on hard difficulty
            elif hard_difficulty:
                # Music artists should still appear next to the song title, but player still has limited to answer
                if topic_name == "zene":
                    print(f"""Melyiknek van több nézettsége? Van 10 másodperced válaszolni!
            1) {f_creator}: {f_title} -> {f_views} nézőszám
            2) {s_creator}: {s_title} -> ??? nézőszám""")
                # Player is basing decisions on which title sounds more interesting and who might have created it
                else:
                    print(f"""Melyiknek van több nézettsége? Van 10 másodperced válaszolni!
            1) {f_title} -> {f_views} nézőszám
            2) {s_title} -> ??? nézőszám""")
                try:
                    # Counting to 10 while awaiting player input
                    player_answer = int(inputimeout(prompt='Szám: ', timeout=10))
                # If they run out of time, or give a wrong input
                except Exception:
                    # Game Over
                    break
            
            # The answer isn't right and the two options' views are not equal
            if correct_answer != 0 and player_answer != correct_answer:
                # Game Over, prints out which was higher
                if correct_answer == 1:
                    print(f"1) {f_views} > 2) {s_views}")
                elif correct_answer == 2:
                    print(f"1) {f_views} < 2) {s_views}")
                break
            
            # Correct answer
            else:
                # Game continues, prints out earned points so far
                points += 1
                print(f"Korrekt! Eddig {points} pont, jöhet a következő...")

            # Remove the first content, so it does not appear again
            content_list.pop(first)
            # # Fixing list order
            if second > first:
                second -= 1
            # Swapping second content to be the first in next round
            first, f_title, f_views, f_creator = second, s_title, s_views, s_creator
        
        if points >= 0:
            if len(content_list) == 1 and points > 0: 
            # Last remaining question in-game
                # Game Over and game completed
                points += 1
            print(f"Játék vége, elért pontszám: {points}")
            Game.react_to_points(points, length_for_reaction)
            Highscore.write_highscore_if_eligible(topic_name, hard_difficulty, points)
