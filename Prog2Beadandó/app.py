# app.py
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models import db, Video
import ytapi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Prog2Beadandó/videos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    # Vegyük le két véletlenszerű videót az adatbázisból
    video1 = Video.query.order_by(func.random()).first()
    video2 = Video.query.filter(Video.id != video1.id).order_by(func.random()).first()

    # Ellenőrizzük, hogy van-e két különböző videó
    if video1 is None or video2 is None:
        return "Nem sikerült két különböző videót kiválasztani az adatbázisból."

    # Az olvasott videókat adjuk át a game.html template-nek
    return render_template('game.html', video1=video1, video2=video2)

@app.route('/stats')
def stats():
    return render_template('stats.html')

# drop table? yes/no; append sqlalchemy db

if __name__ == "__main__":
    app.run(debug=True)
