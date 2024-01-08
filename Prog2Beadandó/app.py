# app.py
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db
import ytapi_fetch as fetch_logic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Prog2Beadandó/videos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')

# Fetch gombhoz útvonal
@app.route('/fetch', methods=['GET'])
def fetch():
    return render_template('fetch.html')

# Drop és fetch gombhoz útvonal
@app.route('/drop_and_fetch', methods=['GET'])
def drop_and_fetch():
    # Drop the previous table
    db.drop_all()
    # Create new table
    db.create_all()
    # Fetch new data
    fetch_logic.fetch_data()
    return redirect(url_for('fetch'))

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

# drop table? yes/no; append sqlalchemy db

if __name__ == "__main__":
    app.run(debug=True)
