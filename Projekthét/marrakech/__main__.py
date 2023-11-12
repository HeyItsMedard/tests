from flask import Flask, render_template, request, url_for, redirect
from .model.player import create_players
from .model.game_state import GameState
from .model.rug import RugPos
from .model.position import Pos
from .model.directions import Direction
import random

app = Flask(__name__)

# Lista a játékosok adatainak tárolására
players = []
game = GameState()

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
    player_data = []  # Ezt itt definiáljuk

    for i in range(num_players):
        player_name = request.form[f'player_{i}']
        player_data.append(player_name)

    # Hívjuk meg a create_players függvényt a megfelelő adatokkal
    global players
    players = create_players(player_data)
    #GameStatebe tároljuk el
    game_state = GameState()
    game_state.add_players(players)
    # A játékosokat átadjuk a game_board nézetnek
    # Pozíció és irány
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    figure_dir = str(game.figure_dir)
    game.current_player = players[0]
    print(game.current_player)
    return render_template('board.html', players=players, 
                           css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir)

@app.route('/roll_dice')
def roll_dice():
    kocka = [1,2,3,4,3,2]
    dobas = random.choice(kocka)
    game.move_figure(dobas)
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    figure_dir = str(game.figure_dir)
    possible_rug_row_up = figure_row +1
    possible_rug_row_down = figure_row -1
    possible_rug_col_left = figure_col -1
    possible_rug_col_right = figure_col +1

    return render_template("board.html", players = players, dobas = dobas, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir, rug_left=possible_rug_col_left, 
                           rug_right=possible_rug_col_right, rug_up=possible_rug_row_up, rug_down=possible_rug_row_down)

@app.route('/turn_left', methods=['GET'])
def turn_left():
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    if game.figure_dir != Direction.LEFT and game.figure_dir != Direction.RIGHT:
        game.figure_dir = Direction.LEFT
    figure_dir = str(game.figure_dir)
    return render_template("board.html", players = players, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir)

@app.route('/turn_right', methods=['GET'])
def turn_right():
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    if game.figure_dir != Direction.LEFT and game.figure_dir != Direction.RIGHT:
        game.figure_dir = Direction.RIGHT
    figure_dir = str(game.figure_dir)
    print(figure_dir)
    return render_template("board.html", players = players, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir)

@app.route('/turn_up', methods=['GET'])
def turn_up():
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    if game.figure_dir != Direction.UP and game.figure_dir != Direction.DOWN:
        game.figure_dir = Direction.UP
    figure_dir = str(game.figure_dir)
    return render_template("board.html", players = players, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir)

@app.route('/turn_down', methods=['GET'])
def turn_down():
    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    if game.figure_dir != Direction.UP and game.figure_dir != Direction.DOWN:
        game.figure_dir = Direction.DOWN
    figure_dir = str(game.figure_dir)
    return render_template("board.html", players = players, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir)


@app.route('/game_over')
def game_over(): 
    return render_template("eredmeny.html")

@app.route('/placing_rug', methods=['POST'])
def placing_rug():
    selected_row = int(request.form['selected_row'])
    selected_col = int(request.form['selected_col'])
    selected_direction = request.form['rug_dir']
    if selected_direction == "Direction.LEFT":
        game.place_rug(RugPos(Pos(selected_row, selected_col), Direction.LEFT))
    if selected_direction == "Direction.RIGHT":
        game.place_rug(RugPos(Pos(selected_row, selected_col), Direction.RIGHT))
    if selected_direction == "Direction.UP":
        game.place_rug(RugPos(Pos(selected_row, selected_col), Direction.UP))
    if selected_direction == "Direction.DOWN":
        game.place_rug(RugPos(Pos(selected_row, selected_col), Direction.DOWN))

    figure_row = game.figure_pos.row
    figure_col = game.figure_pos.col
    figure_dir = str(game.figure_dir)

    return render_template("board.html", players = players, css_url=url_for('static', filename='css/board.css'), figure_row=figure_row, 
                           figure_col=figure_col, figure_dir=figure_dir, selected_direction=selected_direction,
                           selected_col = selected_col, selected_row = selected_row)

if __name__ == '__main__':
    app.run(debug=True)