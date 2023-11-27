from dataclasses import dataclass
from flask import Flask, abort, jsonify, request, render_template, redirect, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped
from os import path
import base64
from io import BytesIO
from matplotlib.figure import Figure

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join('.', 'db.sqlite')
db = SQLAlchemy(app)

@dataclass
class Person(db.Model):
  id: int
  name: str
  neptun: str
  booking_count: int
  books: Mapped[int]

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  neptun = db.Column(db.String, nullable=False, unique=True)
  booking_count = db.Column(db.Integer, default=0)
  books = db.relationship('Book', backref="user", lazy=True)

@dataclass
class Book(db.Model):
  id: int
  isbn: str
  author: str
  title: str
  publisher: str
  year_of_publish: int
  owned_by: int
  booking_count: int

  id = db.Column(db.Integer, primary_key=True)
  isbn = db.Column(db.String, nullable=False)
  author = db.Column(db.String, nullable=False)
  title = db.Column(db.String, nullable=False)
  publisher = db.Column(db.String, nullable=False)
  year_of_publish = db.Column(db.Integer, nullable=False)
  owned_by = db.Column(db.Integer, db.ForeignKey('person.neptun'), nullable=True)
  booking_count = db.Column(db.Integer, default=1)

@app.route('/', methods=['GET', 'POST'])
def index():
  books = Book.query.all()
  people = Person.query.all()
  return render_template('books.html', books=books, people=people)

@app.post('/books')
def add_book():
  new_book = Book(isbn=request.form.get('isbn'), author=request.form.get('author'), title=request.form.get('title'), publisher=request.form.get('publisher'), year_of_publish=request.form.get('year_of_publish'))
  db.session.add(new_book)
  db.session.commit()
  return redirect(url_for('index'))

@app.get('/books/<string:isbn>')
def get_book(isbn):
  book = Book.query.filter_by(isbn=isbn).first()
  print(book)
  if book == None:
    abort(404, 'Book does not exist!')
  return render_template('book.html', book=book)

@app.post('/return')
def return_book():
  book = Book.query.get(request.form.get('id'))
  if book == None:
    abort(404, 'Book does not exist!')
  book.owned_by = None
  db.session.add(book)
  db.session.commit()
  person = Person.query.filter_by(neptun=request.form.get('neptun')).first()
  if person == None:
    abort(404, 'Person does not exist!')
  return redirect(url_for('get_person', neptun=person.neptun))

@app.post('/booking')
def book_book():
  book = Book.query.get(request.form.get('id'))
  if book == None:
    abort(404, 'Book does not exist!')
  if book.owned_by != None:
    abort(400, 'Book is already owned by someone!')
  person = Person.query.filter_by(neptun=request.form.get('neptun')).first()
  if person == None:
    abort(400, 'Person does not exist!')
  book.owned_by = person.neptun
  book.booking_count += 1
  person.booking_count += 1
  db.session.add(person)
  db.session.add(book)
  db.session.commit()
  return redirect(url_for('index'))

@app.get('/people')
def get_people():
  people = Person.query.all()
  return render_template('people.html', people=people)

@app.post('/people')
def add_person():
  new_person = Person(name=request.form.get('name'), neptun=request.form.get('neptun'))
  db.session.add(new_person)
  db.session.commit()
  return redirect(url_for('get_people'))

@app.get('/people/<string:neptun>')
def get_person(neptun):
  person = Person.query.filter_by(neptun=neptun).first()
  books = Book.query.filter_by(owned_by=neptun).all()
  if person == None:
    abort(404, 'Person does not exist!')
  return render_template('person.html', person=person, books=books)

@app.get('/books/top')
def get_top_booked_books():
  books = Book.query.order_by(Book.booking_count.desc()).limit(10).all()
  fig = Figure()
  ax = fig.subplots()
  ax.bar([book.title for book in books], [book.booking_count for book in books])
  ax.set_title('Top booked books')
  ax.set_xlabel('Book Title')
  ax.set_ylabel('Booking count')
  img = BytesIO()
  fig.savefig(img, format="png")
  img.seek(0)
  return send_file(img, mimetype='image/png')

@app.get('/people/top')
def get_top_booked_people():
  people = Person.query.order_by(Person.booking_count.desc()).limit(10).all()
  fig = Figure()
  ax = fig.subplots()
  ax.bar([person.name for person in people], [person.booking_count for person in people])
  ax.set_title('Top readers')
  ax.set_xlabel('Name')
  ax.set_ylabel('Booking count')
  img = BytesIO()
  fig.savefig(img, format="png")
  img.seek(0)
  return send_file(img, mimetype='image/png')

@app.get('/toplist')
def toplist():
  books = Book.query.order_by(Book.booking_count.desc()).limit(10).all()
  people = Person.query.order_by(Person.booking_count.desc()).limit(10).all()
  return render_template('toplist.html', books=books, people=people)

if __name__ == '__main__':
  with app.app_context():
    # db.drop_all()
    db.create_all()
  app.run(debug=True, host='0.0.0.0', port=4000)
