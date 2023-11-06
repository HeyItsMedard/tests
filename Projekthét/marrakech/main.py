from flask import Flask, render_template, request, redirect, url_for
import random

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Projekthét/marrakech/marrakech.db'
db = SQLAlchemy(app)

# Lista a játékosok neveinek és színeinek tárolásához
player_data = []

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(20))
    money = db.Column(db.Integer)
    # Kapcsolat a szőnyegekhez
    carpet_count = db.Column(db.Integer)

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
    
    # Játékosok létrehozása és hozzáadása az adatbázishoz
    for i in range(num_players):
        player_name = player_data[i]
        player_color = available_colors[i]
        
        player = Player(name=player_name, color=player_color, money=money_per_player, carpet_count=carpet_count)
        db.session.add(player)
    
    # Adatok mentése az adatbázisba
    db.session.commit()
    
    return redirect(url_for('game_board'))

@app.route('/game_board')
def game_board():
    # Játéktáblát és állapotot jelenítse meg
    pass

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)
