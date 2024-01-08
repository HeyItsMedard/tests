# app.py
from flask import Flask, render_template

app = Flask(__name__)

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
