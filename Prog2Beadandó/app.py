from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

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

        user = User.query.filter_by(username=session['user']).first()
        user.create_plot_thread()
        user.plot_thread.start() 

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
    #Not enough data, alert
    if Video.query.count() < 2:
        return render_template('game.html', message="A video táblában nincs elég adat. Kérlek, használd a Fetch gombot az adatok betöltéséhez!")

    game_instance = Game(db)
    
    # Starting off with getting the first two videos
    video1, video2 = game_instance.get_random_videos()

    return render_template('game.html', video1=video1, video2=video2)

@app.route('/check_guess/<guess>', methods=['POST'])
def check_guess(guess):
    
    game_instance = Game(db)

    # Retrieve video IDs from the session
    video1_id = session.get('video1_id')
    video2_id = session.get('video2_id')

    if video1_id is None or video2_id is None:
        # User probably tried to access this page directly (sneakely, after game over)
        return redirect(url_for('index'))
    
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

        # Update the session
        session['current_score'] = user.current_score
        session['best_score'] = user.best_score

        db.session.commit()
        
        # Check if the user guessed all videos correctly
        if user.current_score == Video.query.count()-1:
            # Game over, user "won"
            user.update_average_score(user.current_score)
            user.add_score(user.current_score)
            user.current_score = 0
            db.session.commit()
            return redirect(url_for('game_over'))

        # Continue the game
        video1, video2 = game_instance.get_random_videos()

        # Store the video IDs in the session
        session['video1_id'] = video1.id if video1 else None
        session['video2_id'] = video2.id if video2 else None

        session.modified = True  # Explicitly mark the session as modified

        return render_template('game.html', video1=video1, video2=video2)
    else:
        # Incorrect guess, game over screen
        user.update_average_score(user.current_score)
        user.add_score(user.current_score)
        user.current_score = 0
        db.session.commit()
        return redirect(url_for('game_over'))

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/individual_stats')
def individual_stats():
    if 'user' in session:
        username = session['user']
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('individual_stats.html', user=user)
    
    return redirect(url_for('index'))

@app.route('/community_stats')
def community_stats():
    total_users, total_games_played, average_score_community = User.get_community_stats()
    return render_template('community_stats.html', total_users=total_users, total_games_played=total_games_played, average_score_community=average_score_community)

@app.route('/game_over')
def game_over():
    random_message, gif_name = Game.react_to_points(session['current_score'], Video.query.count()-1)
    return render_template('game_over.html', score=session['current_score'], message=random_message, gif_name=gif_name)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
