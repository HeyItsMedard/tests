from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#THIS SHOULD BE THE MAIN PAGE
@app.route('/menu')
def menu():
    pass

@app.route('/fetch')
def fetch():
    pass #onpress, update db (drop previous)

@app.route('/game')
def game():
    pass

@app.route('/game_over')
def game_over():
    pass

@app.route('/statistics')
def statistics():
    pass

if __name__ == "__main__":
    app.run(debug=True)
