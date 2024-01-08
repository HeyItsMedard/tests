# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/fetch')
def fetch():
    return render_template('fetch.html') # drop table? yes/no; append sqlalchemy db

if __name__ == "__main__":
    app.run(debug=True)
