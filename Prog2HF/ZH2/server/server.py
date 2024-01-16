import json
import os

from flask import Flask, abort, jsonify, request

# Change working directory to the directory of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

with open("votes.json", encoding="utf-8") as f:
    votes = json.load(f)
    candidates = {c["id"]: c for c in votes["candidates"]}
    print("Votes loaded:", json.dumps(votes, indent=4, ensure_ascii=False))


@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()
    print("Received vote:", data)
    c_id = data.get("candidate_id")

    if c_id:
        candidates[c_id]["votes"] += 1
        with open("votes.json", "w", encoding="utf-8") as f:
            json.dump(votes, f, indent=4, ensure_ascii=False)
        return jsonify({"message": "Vote recorded successfully"}), 200
    else:
        abort(400, "Invalid request")


@app.route("/results", methods=["GET"])
def results():
    return jsonify(votes)


if __name__ == "__main__":
    app.run(debug=True)
