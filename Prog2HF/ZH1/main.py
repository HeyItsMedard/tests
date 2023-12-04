from dataclasses import dataclass
from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import matplotlib.pyplot as plt
# from sqlalchemy import Table
# from sqlalchemy.orm import relationship

app = Flask(__name__)
app.secret_key = "super-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CUSTOM_SESSION_TIMEOUT = timedelta(minutes=30) # gyakorlásban használtam
app.permanent_session_lifetime = CUSTOM_SESSION_TIMEOUT
db = SQLAlchemy(app)

# book_member_relationship = Table('borrows',
#     db.metadata,
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
#     db.Column('member_id', db.Integer, db.ForeignKey('member.id'))
# )

@dataclass
class Book(db.Model):
    id: int
    isbn: str
    author: str
    title: str
    year: int
    publisher: str
    borrowed: bool
    borrow_date: datetime | None
    return_date: datetime | None
    borrow_count: int
    borrower: int
    
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, unique=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    borrowed = db.Column(db.Boolean, default=False)
    borrow_date = db.Column(db.DateTime, default=None, nullable=True) # első bevitelkor nem lehet kikölcsönözve
    return_date = db.Column(db.DateTime, default=None, nullable=True)
    borrow_count = db.Column(db.Integer, default=0, nullable=True)
    borrower = db.Column(db.Integer, default=None, nullable=True)

@dataclass
class Member(db.Model):
    id: int
    neptun: str
    name: str
    borrow_times: int
    
    id = db.Column(db.Integer, primary_key=True)
    neptun = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    borrow_times = db.Column(db.Integer, default=0, nullable=True)

# TODO: CREATE MAIN SITE

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

@app.route("/")
def home():
    return redirect(url_for("books"))

@app.route("/books", methods=["POST", "GET"])
def books():
    all_books = Book.query.all()
    all_members = Member.query.all()
    if request.method == "POST": #TODO: ADD BOOK
        isbn = request.form["isbn"]
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]

        # Megnézzük, hogy a könyv már bent van-e
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            flash("ISBN already exists in database.")
            return redirect(url_for("books"))
        
        new_book = Book(isbn=isbn, author=author, title=title, 
                        year=year, publisher=publisher, borrowed=False, 
                        borrow_date=None, return_date=None, borrow_count = 0, 
                        borrower= None)
        
        db.session.add(new_book)
        all_books.append(new_book)
        db.session.commit()
    return render_template("books.html", books=all_books, members=all_members)

@app.route("/members", methods=["POST", "GET"])
def members():
    all_members = Member.query.all()
    if request.method == "POST":
        neptun = request.form["neptun"]
        name = request.form["name"]

        member = Member.query.filter_by(neptun=neptun).first()
        if member:
            flash("This Neptun code is already in use.")
            return redirect(url_for("members"))
        
        new_member = Member(neptun=neptun, name=name, borrow_times=0)
        
        db.session.add(new_member)
        all_members.append(new_member)
        db.session.commit()
    return render_template("members.html", members=all_members)

@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
        book_id = request.form["id"]
        book = Book.query.filter_by(id=book_id).first()
        member_neptun = request.form["neptun"]
        member = Member.query.filter_by(neptun=member_neptun).first()
        
        if member and book:
            if member.id == book.borrower:
                print("returns book")
                # RETURN BOOK INSTEAD
                return_date = datetime.utcnow()
                book.return_date = return_date
                book.borrow_date = None
                book.borrowed = False
                book.borrower = None
                db.session.commit()
                flash(f"Book with code {book.isbn} was successfully returned by {member.name}.")
                return redirect(url_for("books"))
            elif member.id != book.borrower and book.borrowed is True:
                borrower_id = book.borrower
                borrower = Member.query.filter_by(id=borrower_id).first()
                flash(f"This book is already borrowed by: {borrower.name} ({borrower.neptun})")
                return redirect(url_for("books"))
            member.borrow_times += 1
            book.borrower = member.id
            book.borrowed = True
            book.borrow_count += 1
            book.borrow_date = datetime.utcnow()
            db.session.commit()
            flash(f"Book with code {book.isbn} was successfully borrowed by {member.name}.")
            return redirect(url_for("books"))
    return redirect(url_for("books"))

@app.route("/stats")
def stats():
    plt.figure(figsize=(8, 4))
    all_books = Book.query.all()
    borrowed_books = {}
    for book in all_books:
        if book.borrow_count > 0:
            borrowed_books[book.title] = book.borrow_count
    plt.bar(borrowed_books.keys(), borrowed_books.values(), color = "r", align="center")
    plt.yticks(range(0, max(borrowed_books.values())+1, 1))
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('static/borrowed_books.png')
    plt.show()

    plt.figure(figsize=(8, 4))
    all_members = Member.query.all()
    most_borrower = {}
    for member in all_members:
        if member.borrow_times > 0:
            most_borrower[member.neptun] = member.borrow_times
    plt.bar(most_borrower.keys(), most_borrower.values(), color = "r", align="center")
    plt.yticks(range(0, max(most_borrower.values())+1, 1))
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('static/most_borrower.png')
    plt.show()
    return render_template("stats.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)