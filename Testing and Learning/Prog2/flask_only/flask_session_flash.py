from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5) # session véget ér 5 perc után, vagyis logout lesz

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login succesful!") #?
        return redirect(url_for("user")) # mint ahogy eddig is, lekérjük az adatot htmlből (usr), majd átmegyünk a user oldalára
    else:
        if "user" in session:
            print("Ok")
            flash("Already logged in!") #?
            return redirect(url_for("user"))
        return render_template("login.html") # még nem történt bevitel

@app.route("/user")
def user():
    if "user" in session:
        print("runs user sesh")
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        print("runs incorrect")
        flash(f"You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" not in session:
        return redirect(url_for("user"))
    else:
        flash(f"You have been logged out!", "info") #info most üres
        session.pop("user", None) # nem ugyanaz, mint list pop
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True) # website updates each save