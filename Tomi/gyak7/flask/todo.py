from flask import Flask, abort, request, render_template, redirect, url_for
import json
from os import path


app = Flask(__name__)

if path.exists('db.json'):
  with open('db.json', 'r') as f:
    db = json.load(f)
    todos = db
else:
  todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html', todos=todos)

@app.route('/todos')
def get_todos():
  return todos

@app.post('/todos')
def add_todo():
  new_todo = {
    'id': len(todos) + 1,
    'completed': False,
    'text': request.json.get('text')
  }
  todos.append(new_todo)
  return new_todo

@app.get('/todos/<int:id>')
def get_todo(id):
  todo = [todo for todo in todos if todo['id'] == id]
  if len(todo) > 0:
    return todo[0]
  abort(404)

@app.patch('/todos/<int:id>')
def patch_todo(id):
  todo = [todo for todo in todos if todo['id'] == id]
  if len(todo) > 0:
    todo = todo[0]
    todo['text'] = request.json.get('text')
    return todo
  abort(404)

@app.put('/todos/<int:id>')
def update_todo(id):
  # todo = list(filter(lambda todo: todo['id'] == id, todos))
  todo = [todo for todo in todos if todo['id'] == id]
  if len(todo) > 0:
    todo = todo[0]
    todo['completed'] = True
    return todo
  else:
    abort(404)

@app.delete('/todos/<int:id>')
def delete_todo(id):
  global todos
  filtered_todos = [todo for todo in todos if todo['id'] != id]
  todos = filtered_todos
  return f'{id}'

@app.post('/login')
def login():
  password = request.form.get('password', '')
  if password == 'password':
    return redirect(url_for('index'))
  abort(401)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html', error=error), 404

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=3000)


with open('db.json', 'w') as f:
  print(todos, 'save')
  json.dump(todos, f)
