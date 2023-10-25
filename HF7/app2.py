from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Adatbázis a wisecrack-ek tárolásához (ideális esetben valós adatbázist használnál)
wisecracks = []

@app.route('/')
def index():
    return render_template('2index.html', wisecracks=wisecracks)

@app.route('/new_wisecrack', methods=['GET', 'POST'])
def new_wisecrack():
    if request.method == 'POST':
        text = request.form['wisecrack']
        if text.strip():  # Ellenőrzés: csak nem üres szöveg mentése
            wisecracks.append(text)
        return redirect(url_for('new_wisecrack'))

    return render_template('2new_wisecrack.html')

if __name__ == '__main__':
    app.run(debug=True)