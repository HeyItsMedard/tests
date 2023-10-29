from dataclasses import dataclass
from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import Table
# from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
# currently used htmls: view, user, reset, register, login, index2, base
app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Testing and Learning/Prog2/flask_only/users.sqlite3' # csak így működik, aki tesztel, írja át
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) # session véget ér 5 perc után, vagyis logout lesz

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
    name: str
    email: str
    password: str
    
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    friends = relationship('User',
                          secondary= friend_relationship,
                          primaryjoin=(_id == friend_relationship.c.user_id),
                          secondaryjoin=(_id == friend_relationship.c.friend_id),
                          backref="friend_of", order_by=_id)
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

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Define the relationships with User
    sender = relationship('User', foreign_keys=[sender_id], back_populates='sent_messages')
    receiver = relationship('User', foreign_keys=[receiver_id], back_populates='received_messages')

@app.route("/")
def home():
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

        if request.method == "POST":
            message_text = request.form.get("message_text")
            if message_text:
                # Create a new message and save it in the database
                message = Message(text=message_text, sender=user, receiver=friend)
                db.session.add(message)
                db.session.commit()
                flash("Message sent!")

        # Fetch all messages between the user and their friend
        messages = Message.query.filter(
            ((Message.sender == user) & (Message.receiver == friend)) |
            ((Message.sender == friend) & (Message.receiver == user))
        ).order_by(Message.timestamp).all()

        return render_template("message.html", user=user, friend=friend, messages=messages)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/unfriend/<friend_name>")
def unfriend(friend_name):
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
    return render_template("view.html", values=User.query.all())

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
        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        # You can add more fields here

        # Check if the user already exists
        user = User.query.filter_by(name=name).first()
        if user:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for("register"))

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["nm"]
        password = request.form["password"]

        user = User.query.filter_by(name=name).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session.permanent = True
            session["user"] = name
            flash("Login successful! Confirm your details.")
            return redirect(url_for("user"))
        else:
            flash("Login failed. Invalid credentials.")
            return redirect(url_for("login"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = User.query.filter_by(name=user).first()
            found_user.email = email

            new_username = request.form.get("new_username")
            new_password = request.form.get("new_password")

            if new_username:
                found_user.name = new_username
                session["user"] = new_username  # Update the session with the new username

            if new_password:
                found_user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

            db.session.commit()
            flash("Changes saved!")
        else:
            if "email" in session:
                email = session["email"]
            else:
                found_user = User.query.filter_by(name=user).first()
                email = found_user.email if found_user else ""
                session["email"] = email

        return render_template("user.html", user=user, email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" not in session:
        return redirect(url_for("user"))
    else:
        flash(f"You have been logged out!", "info") #info is empty
        session.pop("user", None) # not the same as list pop
        session.pop("email", None)
        return redirect(url_for("login"))
    
@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST': 
        db.drop_all()
        db.create_all()
        return redirect(url_for('home'))
    return render_template('reset.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) # website updates each save