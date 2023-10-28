## Extensions:  
- Live Preview (HTML)
- Python, Pylance
- SQLite
- mplstyle
- Python Image Preview

## Command install:
```bash
$ pip install flask
$ pip install flask-bcrypt
$ pip3 install flask-sqlalchemy
$ pip install matplotlib
```

### SQLite explorer: 
kiválasztod a db filet, Open Database, bal alul SQLITE EXPLORER, táblázat megtekintéséhez Show Table.

### Flask és SQLAlchemy:

```python
app = Flask(__name__)
app.secret_key = "super-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{nameoffile}.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
