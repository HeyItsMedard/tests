from dataclasses import dataclass
from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)
player_data= []
@dataclass
class Player:
    name: str
    color: str
    money: int
    carpet_count: int

# Lista a játékosok adatainak tárolására
players = []

@app.route('/')
def start_game_form():
    return render_template('start_game.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    num_players = int(request.form['num_players'])
    
    return render_template('enter_player_names.html', num_players=num_players)

@app.route('/enter_player_names', methods=['POST'])
def enter_player_names():
    num_players = int(request.form['num_players'])
    
    for i in range(num_players):
        player_name = request.form[f'player_{i}']
        player_data.append(player_name)
    carpet_count = 12 if num_players == 4 else 15
    available_colors = ['Red', 'Blue', 'Green', 'Yellow']
    random.shuffle(available_colors)
    for i in range(num_players):
        player_name = request.form[f'player_{i}']
        player_color = available_colors[i]
        
        # Létrehozunk egy Player objektumot és hozzáadjuk a players listához
        player = Player(name=player_name, color=player_color, money=120//num_players, carpet_count=carpet_count)
        players.append(player)
    print(players)
    # A játékosokat átadjuk a game_board nézetnek
    return render_template('game_board.html', players=players, num_players=num_players)

@app.route('/game_board')
def game_board():
    # TODO: írd meg a függvényt és a htmlt! írja ki a játékosokat és tulajdonaikat, az első elem kezdjen egy körben és haladjon végig
    pass

if __name__ == '__main__':
    app.run(debug=True)