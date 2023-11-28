from dataclasses import dataclass
from flask import Flask, abort, jsonify, request, render_template, redirect, url_for
from os import path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join('.', 'db.sqlite')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

@dataclass
class User(db.Model):
  id: int
  username: str
  password: str
  todos: Mapped[int]

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String, nullable=False)
  todos = db.relationship('Todo', backref="user", lazy=True)

@dataclass
class Todo(db.Model):
  id: int
  text: str
  completed: int
  createdBy: int

  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String, nullable=False)
  completed = db.Column(db.Boolean, default=False)
  createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
  todos = Todo.query.all()
  return render_template('index.html', todos=todos)

@app.route('/todos')
@jwt_required()
def get_todos():
  order = request.args.get('order', 'asc')
  todos = Todo.query.filter_by(createdBy=get_jwt_identity()).order_by(Todo.id.desc() if order == "desc" else Todo.id.asc()).all()
  return todos

@app.post('/todos')
@jwt_required()
def add_todo():
  new_todo = Todo(text=request.json.get('text'), createdBy=get_jwt_identity())
  db.session.add(new_todo)
  db.session.commit()
  return jsonify(new_todo)

@app.get('/todos/<int:id>')
@jwt_required()
def get_todo(id):
  todo = Todo.query.get_or_404(id)
  if todo.createdBy == get_jwt_identity():
    return jsonify(todo)
  else:
    abort(401)

@app.patch('/todos/<int:id>')
@jwt_required()
def patch_todo(id):
  todo = Todo.query.get_or_404(id)
  if todo.createdBy != get_jwt_identity():
    abort(401)
  todo.text = request.json.get('text')
  db.session.add(todo)
  db.session.commit()
  return jsonify(todo)

@app.put('/todos/<int:id>')
@jwt_required()
def update_todo(id):
  todo = Todo.query.get_or_404(id)
  if todo.createdBy != get_jwt_identity():
    abort(401)
  todo.completed = True
  db.session.add(todo)
  db.session.commit()
  return jsonify(todo)

@app.delete('/todos/<int:id>')
@jwt_required()
def delete_todo(id):
  todo = Todo.query.get_or_404(id)
  if todo.createdBy != get_jwt_identity():
    abort(401)
  db.session.delete(todo)
  db.session.commit()
  return f'{id}'

@app.post('/users')
def register():
  username = request.form.get('username')
  password = request.form.get('password')
  hashed = bcrypt.generate_password_hash(password).decode('utf-8')
  user = User(username=username, password=hashed)
  db.session.add(user)
  db.session.commit()
  return jsonify(user)

@app.post('/login')
def login():
  username = request.form.get('username')
  password = request.form.get('password')
  user = User.query.filter_by(username=username).first()
  if user and bcrypt.check_password_hash(user.password, password):
    access_token = create_access_token(identity=username)
    return access_token
  else:
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', error=error), 404

@app.delete('/drop')
@jwt_required()
def drop():
  db.drop_all()
  # User.__table__.drop(db.engine)
  return ''

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True, host='0.0.0.0', port=4000)
