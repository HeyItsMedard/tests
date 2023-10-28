from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import Mapped
# from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Testing and Learning/Prog2/flask_only/users.sqlite3' # csak így működik, aki tesztel, írja át
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) # session véget ér 5 perc után, vagyis logout lesz

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@dataclass
class User(db.Model):
    name: str
    email: str
    password: str
    
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        # You can add more fields here

        # Check if the user already exists
        user = User.query.filter_by(name=name).first()
        if user:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for("register"))

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        new_user = User(name=name, password=hashed_password)
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
        flash(f"You have been logged out!", "info") #info most üres
        session.pop("user", None) # nem ugyanaz, mint list pop
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