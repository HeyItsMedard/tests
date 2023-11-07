from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Lista a játékosok neveinek és színeinek tárolásához
player_data = []

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
    
    # Játékosok számának alapján pénzérmék és szőnyegek inicializálása
    money_per_player = 120 // num_players
    carpet_count = 12 if num_players == 4 else (15 if num_players == 3 else 24)
    
    available_colors = ['Red', 'Blue', 'Green', 'Yellow']
    random.shuffle(available_colors)
    
    # Játékosok létrehozása és hozzáadása a player_data listához
    players = []
    for i in range(num_players):
        player_name = player_data[i]
        player_color = available_colors[i]
        
        player = {'name': player_name, 'color': player_color, 'money': money_per_player, 'carpet_count': carpet_count}
        players.append(player)
    print(players)
    return redirect(url_for('game_board'))

@app.route('/game_board')
def game_board():
    # Játékosok adatainak lekérése a dataclassból
    players = get_players_data()  # Adatainak lekérése a megfelelő függvénnyel

    return render_template('game_board.html', players=players)

# Új függvény a játékosok adatainak lekéréséhez
def get_players_data():
    players = []  # Ebben a listában tároljuk majd a játékosok adatait

    # Itt le kell kérni a játékosok adatait a dataclassból és hozzáadni a players listához

    return players

if __name__ == '__main__':
    app.run(debug=True)