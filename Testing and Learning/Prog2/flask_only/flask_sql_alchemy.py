from dataclasses import dataclass
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/medav/Documents/GitHub/tests/Testing and Learning/Prog2/flask_only/users.sqlite3' # csak így működik, aki tesztel, írja át
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) # session véget ér 5 perc után, vagyis logout lesz

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        found_user = User.query.filter_by(name=user).first() # delete() egy külön fvben pl.
        if found_user:
            session["email"] = found_user.email
        else:
            usr = User(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login succesful!")
        return redirect(url_for("user")) # mint ahogy eddig is, lekérjük az adatot htmlből (usr), majd átmegyünk a user oldalára
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html") # még nem történt bevitel

@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = User.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
            else:
                # If email is not in the session, fetch it from the database
                found_user = User.query.filter_by(name=user).first()
                email = found_user.email if found_user else ""
                session["email"] = email  # Store email in the session
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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) # website updates each save