from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from sqlalchemy.engine.reflection import Inspector
import random

from models import db, Video, User
from game import Game
import ytapi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Prog2Beadandó/game.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CUSTOM_SESSION_TIMEOUT = timedelta(minutes=30)
app.permanent_session_lifetime = CUSTOM_SESSION_TIMEOUT
app.secret_key = 'super secret key'
bcrypt = Bcrypt(app)
db.init_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

@app.route('/')
def index():
    """Index page, redirects to login or register if no user is logged in, otherwise redirects to menu"""
    if "user" in session:
        if User.query.count() == 0:
            session.clear()
            return render_template("login_or_register.html")
        game_instance = Game(db)
        game_instance.reset()
        session['current_score'] = 0
        return render_template('menu.html')
    else:
        if User.query.count() == 0:
            session.clear()
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
            return render_template('register.html', message="Ez a felhasználónév már foglalt!")

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Remember registration date
        registration_date = datetime.utcnow()

        # Create new user
        user = User(username=username, password=hashed_password, registration_date=registration_date)
        db.session.add(user)
        db.session.commit()
        
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
            user.login_date = datetime.utcnow()
            session['session_expires'] = datetime.utcnow() + timedelta(minutes=30)
            db.session.commit()
            return redirect(url_for("index"))  # Redirect to menu successful login
        else:
            return render_template('login.html', message="Sikertelen bejelentkezés!")
    else:
        if "user" in session:
            return redirect(url_for("index"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" not in session:
        # Not logged in anyways
        return render_template("login_or_register.html")
    else:
        # Get session user
        username = session["user"]
        # Search them in the database
        user = User.query.filter_by(username=username).first()
        # Set the logout date
        logout_date = datetime.utcnow()
        user.logout_date = logout_date
        user.played_time += logout_date - user.login_date
        user.login_date = None
        db.session.commit() # and save it

        # Log out the session user
        session.pop("user", None) # not the same as list pop, logs user out
        return render_template("login_or_register.html")
    
@app.route('/drop_and_fetch', methods=['GET'])
def drop_and_fetch():
    # Drop the Video table
    Video.__table__.drop(db.engine)
    # Create new table
    db.create_all()
    # Fetch new data
    ytapi.fetch_data()

    return redirect(url_for('index'))

@app.route('/game')
def game():
    if Video.query.count() < 2:
        return render_template('game.html', message="A video táblában nincs elég adat. Kérlek, használd a Fetch gombot az adatok betöltéséhez!")

    game_instance = Game(db)
    
    video1, video2 = game_instance.get_random_videos()

    return render_template('game.html', video1=video1, video2=video2)

@app.route('/check_guess/<guess>', methods=['POST'])
def check_guess(guess):
    game_instance = Game(db)

    # Retrieve video IDs from the session
    video1_id = session.get('video1_id')
    video2_id = session.get('video2_id')

    # Retrieve video instances using IDs
    video1 = Video.query.get(video1_id)
    video2 = Video.query.get(video2_id)

    user = User.query.filter_by(username=session["user"]).first()

    if game_instance.check_guess(video1, video2, guess):
        # Correct guess, increase score
        user.current_score += 1

        # Check if the current score is higher than the best score
        if user.current_score > user.best_score:
            user.best_score = user.current_score

        db.session.commit()

        # Continue the game
        video1, video2 = game_instance.get_random_videos()

        # Store the video IDs in the session
        session['video1_id'] = video1.id if video1 else None
        session['video2_id'] = video2.id if video2 else None

        # Update the session
        session['current_score'] = user.current_score
        session['best_score'] = user.best_score

        session.modified = True  # Explicitly mark the session as modified

        return render_template('game.html', video1=video1, video2=video2)
    else:
        # Incorrect guess, redirect to menu - game over indev!
        user.current_score = 0
        user.games_played += 1
        # session['current_score'] = user.current_score - dobjuk át előbb gameoverbe!
        db.session.commit()
        return redirect(url_for('game_over'))

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/game_over')
def game_over():
    random_message = react_to_points(session['current_score'], Video.query.count()-1)
    return render_template('game_over.html', score=session['current_score'], message=random_message)

def react_to_points(points: int, length: int):
        """The game reacts with a message, based on how well the player was performing.

        Args:
            points (int): Points earned throughout the game by the player.
            length (int): The maximum possible questions' count. Necessary when the game runs out of questions.

        Prints:
            str: A funny response
        """
        zero = ["Te egy kő alatt élsz, vagy ennyire szerencsétlen kérdést kaptál? Próbálkozz újra!", 
                "Több mint a semmi! Ja nem...", "Hát lehetne ennél rosszabb?"]
        terrible = ["Felejtsük el, hogy ez megtörtént... Új játék?", f"... csak {points} pont? Rettenetes...", 
                    "Nagyjából ennyi pont választotta el a Dortmundot is egy bajnoki győzelemtől... idén is...",
                    "Ennél tudsz te jobbat is, hiszek benned!"]
        better = ["Szép szám bizony, de vajon tudsz ennél jobbat elérni?",
                  "Ügyes! Így tovább!", "Ez megérdemel egy virtuális hátveregést!",
                  "Ahogy VR Pisti is mondaná: \"Nem is rossz!\""]
        great = ["Aztamindenségit! Gratulálok az eredményhez!", "Ijesztően sokat tudsz!",
                 "Szép munka!"]
        max = ["Sikerült kivinned a játékot! Gratulálok!", 
               "A családod mikor látott utoljára? Csak egy kérdés... mert helyesen válaszoltál minden kérdésre! Lenyűgöző!",
               "Ez a játék vége. Tényleg. Nem vicc. Feladom. Le a kalappal. gg"]
        # The answer is chosen randomly, but based on earned points
        # Comment out playsound for Easter Eggs (note: sometimes they do not work).
        if points == 0:
            print(random.choice(zero))
            return random.choice(zero)
            # playsound('sounds\\zero1.mp3') -> gave up again, error handling doesn't work on it, only commenting helps
        elif points <= 2:
            print(random.choice(terrible))
            return random.choice(terrible)
            # playsound('sounds\\\\\\bad1.mp3') -> gave up again, error handling doesn't work on it, only commenting helps
        elif points <= 6:
            print(random.choice(better))
            return random.choice(better)
            # playsound('sounds\\notbad.mp3') -> gave up again, error handling doesn't work on it, only commenting helps 
        elif points < length:
            print(random.choice(great))
            return random.choice(great)
            # playsound('sounds\\nice.mp3')
        elif points == length:
            print(random.choice(max))
            return random.choice(max)
            # playsound('sounds\\\max1.mp3')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
