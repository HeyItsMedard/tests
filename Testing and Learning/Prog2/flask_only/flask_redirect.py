from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return f"Welcome! <h1>HOME<h1>"

@app.route("/<name>") # a per után bármit beírva futtat egy oldalt
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run()