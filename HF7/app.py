from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def calculate_progress(szavazatok):
    max_szavazat = max(szavazatok.values())
    progress = {}
    for valasztas, szavazat in szavazatok.items():
        progress[valasztas] = (szavazat / max_szavazat) * 100
    return progress, max_szavazat

@app.route('/')
def index():
    with open('szavazatok.json', 'r') as f:
        szavazatok = json.load(f)
        progress, max_szavazat = calculate_progress(szavazatok)

    return render_template('index.html', szavazatok=szavazatok, progress=progress, max_szavazat=max_szavazat)

@app.route('/szavaz', methods=['POST'])
def szavaz():
    valasztas = request.form['valasztas']
    
    with open('szavazatok.json', 'r') as f:
        szavazatok = json.load(f)

    szavazatok[valasztas] = szavazatok.get(valasztas, 0) + 1

    with open('szavazatok.json', 'w') as f:
        json.dump(szavazatok, f)
    
    progress, max_szavazat = calculate_progress(szavazatok)

    return jsonify({'success': True, 'progress': progress, 'max_szavazat': max_szavazat})

if __name__ == '__main__':
    app.run(debug=True)