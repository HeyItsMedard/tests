from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user)) # mint ahogy eddig is, lekérjük az adatot htmlből (usr), majd átmegyünk a user oldalára
    else:
        return render_template("login.html") # még nem történt bevitel

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True) # website updates each save