from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from sqlalchemy.engine.reflection import Inspector

from models import db, Video, User
from game import Game
import ytapi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Prog2Beadandó/game.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CUSTOM_SESSION_TIMEOUT = timedelta(minutes=10)
app.permanent_session_lifetime = CUSTOM_SESSION_TIMEOUT
app.secret_key = 'super secret key'
bcrypt = Bcrypt(app)
db.init_app(app)

@app.route('/')
def index():
    if "user" in session:
        game_instance = Game(db)
        game_instance.reset()
        return render_template('menu.html')
    else:
        return render_template("login_or_register.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # Get inputs
        username = request.form["username"]
        password = request.form["password"]

        # Check if the user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for("register"))

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Remember registration date
        registration_date = datetime.utcnow()

        # Create new user
        user = User(username=username, password=hashed_password, registration_date=registration_date)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Get username and password
        username = request.form["username"]
        password = request.form["password"]

        # Look for user and check password hash
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session.permanent = True
            session["user"] = username
            session['session_expires'] = datetime.utcnow() + timedelta(minutes=30)  # Set your custom session timeout
            return redirect(url_for("index"))  # Redirect to the user page or any other desired page after successful login
        else:
            flash("Login failed. Invalid credentials.")
            return redirect(url_for("login"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
