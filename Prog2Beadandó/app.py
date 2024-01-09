# app.py
from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models import db, Video
from game import Game
import ytapi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Prog2Beadandó/videos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'
db.init_app(app)

@app.route('/')
def index():
    return render_template('menu.html')

# Drop és fetch gombhoz útvonal
@app.route('/drop_and_fetch', methods=['GET'])
def drop_and_fetch():
    # Drop the previous table
    db.drop_all()
    # Create new table
    db.create_all()
    # Fetch new data
    ytapi.fetch_data()
    return redirect(url_for('index'))

@app.route('/game')
def game():
    # Hozz létre egy Game példányt és add át neki a db objektumot
    game_instance = Game(db)

    # Hívjuk meg a Game osztályt és vegyük le a videókat
    video1, video2 = game_instance.get_random_videos()

    # Hívjuk meg a Game osztályt és adjuk át a videókat a template-nek
    return render_template('game.html', video1=video1, video2=video2)

#PROBLEM: Az új körben bal oldalt kéne legyen az előző jobboldali videó és a jobboldalinek egy random videó, de mindkettő random lesz

@app.route('/check_guess/<guess>', methods=['POST'])
def check_guess(guess):
    game_instance = Game(db)

    # Retrieve video IDs from the session
    video1_id = session.get('video1_id')
    video2_id = session.get('video2_id')

    # Retrieve video instances using IDs
    video1 = Video.query.get(video1_id)
    video2 = Video.query.get(video2_id)

    if game_instance.check_guess(video1, video2, guess):
        # Helyes tipp, folytatjuk a játékot
        video1, video2 = game_instance.get_random_videos()
        
        # Tároljuk el az új videók ID-jait a session-ben
        session['video1_id'] = video1.id if video1 else None
        session['video2_id'] = video2.id if video2 else None

        session.modified = True  # Explicitly mark the session as modified
        return render_template('game.html', video1=video1, video2=video2)
    else:
        # Rossz tipp, visszatérünk a menühöz
        return redirect(url_for('index'))


@app.route('/stats')
def stats():
    return render_template('stats.html')

if __name__ == "__main__":
    app.run(debug=True)
