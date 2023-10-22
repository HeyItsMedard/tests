from flask import Flask, redirect, url_for, request, render_template, abort
from markupsafe import escape

app = Flask(__name__)

# @app.get('/hello/<string:name>')
# @app.post('/hello/<string:name>')
@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def hello(name):
  return f'<p>Hello {escape(name)}</p>'

@app.post('/')
def index():
  return redirect(url_for('login'))

@app.route('/sign_in')
def login():
  return 'login'

@app.post('/greet')
def greet():
  name = ''
  password = ''
  if len(request.args) > 1:
    name = request.args.get('username', 'Anonymous')
    password = request.args.get('password')
  else:
    name = request.form.get('username')
    password = request.form.get('password')
  print(name, password)
  return f'{name}: {password}'

@app.get('/input')
def input():
  return render_template('main.html')

@app.get('/create')
def create():
  print('hello')
  abort(500)
  print(request.json)


@app.get('/<name>')
def index_2(name):
  return render_template('hello.html', name=name)

if __name__ == '__main__':
  app.run(port=3000, debug=True, host='0.0.0.0')
