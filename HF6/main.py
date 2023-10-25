import os
import time
import threading
from board import Board
import text_view

def monster_movement(board):
    while not board.is_game_over():
        os.system("cls" if os.name == "nt" else "clear")
        board.move_monsters()
        print(text_view.render(board.get_cells()))
        time.sleep(1)

board = Board(10)

if __name__ == "__main__":
    start_time = time.time()
    monster_thread = threading.Thread(target=monster_movement, args=(board,))
    monster_thread.daemon = True
    monster_thread.start()
    while True:
        while not board.is_game_over():
            try:
                direction = input()[0]
                if direction != "":
                    board.move_player(direction)
            except Exception:
                pass

        if board.is_game_won():
            # Játék győzelem esetén kérjük be a nevet és frissítsük a ranglistát
            end_time = time.time()
            board.win_animation()
            play_time = round(end_time - start_time, 2)

            player_name = input("Gratulálok! Kérlek add meg a neved: ")
            while len(player_name) < 3 or "-" in player_name:
                print("Adj meg legalább három karaktert!")
                player_name = input("Gratulálok! Kérlek add meg a neved: ")
            leaderboard = board.update_leaderboard(player_name, play_time)

            # Megjelenítjük a ranglistát a top 10 bejegyzéssel
            print("\nTop 10 ranglista:")
            for i, entry in enumerate(leaderboard):
                print(f"{i + 1}. {entry[0]} - {entry[1]} mp")

        elif not board.is_game_won():
            board.lose_animation()
            print("Vesztettél!")
            
        quit = input("Kilépés (Q): ") # nincs sok értelme, de ok
        if quit == "Q":
            break
        else:
            break # ígyis kilép, mivel nem tud mást tenni igazából
        
        
