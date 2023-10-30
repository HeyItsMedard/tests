from dataclasses import dataclass
from datetime import datetime
from flask import Flask, jsonify, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import relationship
from sqlalchemy import Table
# from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
# currently used htmls: view, user, reset, register, login, index2, base, message, friends (from templates)
app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Testing and Learning/Prog2/flask_only/users.sqlite3' # csak így működik, aki tesztel, írja át
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CUSTOM_SESSION_TIMEOUT = timedelta(minutes=10)
app.permanent_session_lifetime = CUSTOM_SESSION_TIMEOUT

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define the many-to-many relationship table
friend_relationship = Table('friend_relationship',
    db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'))
)

@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    password: str
    registration_date: datetime
    login_date: datetime | None
    logout_date: datetime | None
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    login_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)  # Default is None
    logout_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True) # Default is None
    friends = relationship('User',
                          secondary= friend_relationship,
                          primaryjoin=(id == friend_relationship.c.user_id),
                          secondaryjoin=(id == friend_relationship.c.friend_id),
                          backref="friend_of", order_by=id)
    
    # Define the relationship for messages sent by the user
    sent_messages = relationship('Message', back_populates='sender', foreign_keys='Message.sender_id')

    # Define the relationship for messages received by the user
    received_messages = relationship('Message', back_populates='receiver', foreign_keys='Message.receiver_id')

@dataclass
class Message(db.Model):
    id: int
    text: str
    sender_id: int
    receiver_id: int
    timestamp: datetime
    seen: bool

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    seen = db.Column(db.Boolean, default=False)  # Default is False

    # Define the relationships with User
    sender = relationship('User', foreign_keys=[sender_id], back_populates='sent_messages')
    receiver = relationship('User', foreign_keys=[receiver_id], back_populates='received_messages')

@app.route("/")
def home():
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()
        unseen_messages = Message.query.filter((Message.receiver_id == user.id) & (Message.seen == 0)).all()
        message_count = len(unseen_messages)
        return render_template("index2.html", name=user_name, message_count=message_count)
    else:
        return render_template("index2.html")

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

@app.route("/friends")
def friends():
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()
        return render_template("friends.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/message/<friend_name>", methods=["GET", "POST"])
def message(friend_name):
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()
        friend = User.query.filter_by(name=friend_name).first()
        # Fetch all messages between the user and their friend
        messages = Message.query.filter(
            ((Message.sender == user) & (Message.receiver == friend)) |
            ((Message.sender == friend) & (Message.receiver == user))
        ).order_by(Message.timestamp).all()

        # Mark messages as "seen" - not okay, it sets every message before last input true
        for message in messages:
            if not message.seen and user.id == message.receiver_id:
                message.seen = True
        # Commit the changes
        db.session.commit()
        if request.method == "POST":
            message_text = request.form.get("message_text")
            if message_text:
                # Create a new message and save it in the database
                new_message = Message(text=message_text, sender=user, receiver=friend, seen=False)
                db.session.add(new_message)
                db.session.commit()
                # flash("Message sent!") #some reason shows up outside of messages now, but I'm not bothered
                # Add the newly posted message to the list of messages
                # messages.append(new_message)
                # js needs this for some reason lol
                response = {
                    'text': message_text,
                    'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M'),
                }
                return jsonify(response)
                
        messages = Message.query.filter(
                ((Message.sender == user) & (Message.receiver == friend)) |
                ((Message.sender == friend) & (Message.receiver == user))
            ).order_by(Message.timestamp).all()
        
        return render_template("message.html", user=user, friend=friend, messages=messages)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/unfriend/<friend_name>")
def unfriend(friend_name): # from friends.html, we pass the username of selected friend
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()
        friend = User.query.filter_by(name=friend_name).first()

        if friend in user.friends:
            # Remove the friendship
            user.friends.remove(friend)
            friend.friends.remove(user)

            # Remove associated messages
            Message.query.filter(
                (Message.sender == user) | (Message.receiver == user),
                (Message.sender == friend) | (Message.receiver == friend)
            ).delete(synchronize_session=False)

            db.session.commit()
            flash(f"You are no longer friends with {friend_name}.")
        else:
            flash("User is not your friend.")

        return redirect(url_for("friends"))
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/view")
def view():
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()
        since_registration = user.registration_date
        recent_users = User.query.filter(User.registration_date > since_registration).all()
        return render_template("view.html", values=recent_users)
    else:
        # Get the current date and time
        current_datetime = datetime.now()

        # Calculate the start of today (midnight)
        # Note: you have to set it manually. Date and DateTime can't be compared.
        today_start = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        today_users = User.query.filter(User.registration_date > today_start).all()
        return render_template("view.html", values=today_users)

@app.route("/befriend", methods=["POST"])
def befriend():
    if "user" in session:
        user_name = session["user"]
        friend_name = request.form.get("friend_name")

        # Check if the friend's name is valid
        if not friend_name:
            flash("Invalid friend name.")
            return redirect(url_for("view"))

        # Check if the user and friend are not the same
        if user_name == friend_name:
            flash("You cannot befriend yourself.")
            return redirect(url_for("view"))

        # Retrieve the user and friend from the database
        user = User.query.filter_by(name=user_name).first()
        friend = User.query.filter_by(name=friend_name).first()

        # Check if the user and friend exist
        if user and friend:
            # Check if they are already friends
            if friend in user.friends:
                flash(f"You are already friends with {friend_name}.")
                return redirect(url_for("view"))

            # Add the friend to the user's friend list
            user.friends.append(friend)
            friend.friends.append(user)  # Establish friendship in both directions
            db.session.commit()

            flash(f"You are now friends with {friend_name}.")
            return redirect(url_for("view"))
        else:
            flash("User or friend not found.")
            return redirect(url_for("view"))
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # Get inputs
        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        # Check if the user already exists
        user = User.query.filter_by(name=name).first()
        if user:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for("register"))

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Remember registration date
        registration_date = datetime.utcnow()

        # Create new user
        new_user = User(name=name, password=hashed_password, email=email, 
                        registration_date=registration_date, login_date=None, logout_date=None)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    # User tries logging in
    if request.method == "POST":
        # Get name and password
        name = request.form["nm"]
        password = request.form["password"]

        # Look for user and check password hash
        user = User.query.filter_by(name=name).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session.permanent = True
            session["user"] = name
            session['session_expires'] = datetime.utcnow() + CUSTOM_SESSION_TIMEOUT
            # Set the login date
            login_date = datetime.utcnow()
            user.login_date = login_date
            db.session.commit()

            flash("Login successful! Confirm your details.")
            return redirect(url_for("user")) # check settings
        # User not found or incorrect password
        else:
            flash("Login failed. Invalid credentials.")
            return redirect(url_for("login"))
    # User in session, already logged in
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    # Make sure the user is logged in
    if "user" in session:
        user = session["user"]
        found_user = User.query.filter_by(name=user).first()

        # Give email to the session
        email = found_user.email
        session["email"] = email

        # User made changes
        if request.method == "POST":
            # Get all usernames and emails from the database
            all_usernames = [user.name for user in User.query.all()]
            all_emails = [user.email for user in User.query.all()]

            # Requesting new input from HTML
            new_username = request.form.get("new_username")
            new_password = request.form.get("new_password")
            new_email = request.form.get("new_email")

            if new_username:
                # compare to current and existing usernames
                if new_username != user and new_username not in all_usernames:
                    found_user.name = new_username  # Update name in the database
                    session["user"] = new_username  # Update the session with the new username
                else:
                    new_username = user # for display, change it back to the original
                    flash("Username already in use or same as the current username. Changes not saved.")

            if new_email:
                # compare to current and existing emails
                if new_email != email and new_email not in all_emails:
                    found_user.email = new_email
                else:
                    new_email = email # for display, change it back to the original
                    flash("Email already in use or same as the current email. Changes not saved.")

            if new_password:
                # Save the hashed password to the database
                found_user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

            # Save the changes to the database
            db.session.commit()
            flash("Changes saved!")
            return render_template("user.html", user=new_username, email=new_email)

        return render_template("user.html", user=user, email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/delete_user", methods=["POST"])
def delete_user():
    if "user" in session:
        user_name = session["user"]
        user = User.query.filter_by(name=user_name).first()

        # User found in database
        if user:
            # Delete user's messages
            Message.query.filter(
                (Message.sender == user) | (Message.receiver == user)
            ).delete(synchronize_session=False)

            # Remove the user from their friends' lists
            for friend in user.friends:
                friend.friends.remove(user)

            # Delete the user
            db.session.delete(user)
            db.session.commit()

            # Log the user out
            session.pop("user", None)
            session.pop("email", None)
            flash("Your account has been deleted.")
        else:
            flash("User not found.")
    else: # how do you even get here if you are not logged in? :D
        flash("You are not logged in!")

    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" not in session:
        # You are not logged in flash in user, redirect to login
        return redirect(url_for("user"))
    else:
        # Get session user
        name = session["user"]
        # Search them in the database
        user = User.query.filter_by(name=name).first()
        # Set the logout date
        logout_date = datetime.utcnow()
        user.logout_date = logout_date
        db.session.commit() # and save it

        # Log out the session user
        flash(f"You have been logged out!", "info") #info is empty
        session.pop("user", None) # not the same as list pop, logs user out
        session.pop("email", None)
        return redirect(url_for("login"))

# In case of inactivity, the last time a request was made is going to be the the logout time
@app.teardown_request
def teardown_request(exception=None):
    if 'user' in session:
        name = session['user']
        user = User.query.filter_by(name=name).first()
        if user:
            logout_date = datetime.utcnow()
            user.logout_date = logout_date
            db.session.commit()

@app.route('/reset', methods=['GET', 'POST'])
def reset(): #TODO: RESET HAS A PROBLEM WITH HOME WHERE IT THINKS ITS IN SESSION
    # Warning in html
    if request.method == 'POST':
        # empties the databases and sets the formats back - watch out for unused tables
        db.drop_all()
        db.create_all()
        session.pop("user", None)
        session.pop("user", None)
        return redirect(url_for('home'))
    return render_template('reset.html')
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) # website updates each save