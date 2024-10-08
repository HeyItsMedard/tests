import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

username = os.getenv('DB_USER', 'root')
password = os.getenv('DB_PASSWORD', 'password')
db_url = os.getenv('DB_URL', '127.0.0.1')
port = os.getenv('DB_PORT', 3306)
database = os.getenv('DB_NAME', 'demo')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{username}:{password}@{db_url}:{port}/{database}"

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
