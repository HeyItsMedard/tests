from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("friends.html", content=["attila", "bandi", "cecil"]) #index.html előzőleg
# def home(name):
#     return render_template("uneven.html", content=name) #index.html előzőleg

if __name__ == "__main__":
    app.run()