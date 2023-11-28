from flask import Flask, request, jsonify

app = Flask(__name__)

# Running on http://127.0.0.1:5000
@app.route('/get-user/<int:user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'username': 'test',
        'password': 'password'
    }
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200

# Check inside Postman
@app.route('/create-user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_data = request.get_json()
        return jsonify(user_data), 201

if __name__ == '__main__':
    app.run()
