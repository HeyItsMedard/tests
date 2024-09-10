from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import mysql.connector

# Check if the database exists
connection = mysql.connector.connect(user='root', password='password', host='localhost')
cursor = connection.cursor()
cursor.execute("SHOW DATABASES LIKE 'db'")
database_exists = cursor.fetchone()

# Create the database if it doesn't exist
if not database_exists:
    cursor.execute("CREATE DATABASE db")
else:
    cursor.execute("DROP DATABASE db")
    cursor.execute("CREATE DATABASE db")

# Close the cursor and connection
cursor.close()
connection.close()

# Update the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:password@localhost/db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def hello():
    existing_user = User.query.filter_by(username='JohnDoe').first()
    if existing_user:
        return f'Welcome back, {existing_user.username}! Your email is {existing_user.email}'
    
    new_user = User(username='JohnDoe', email='johndoe@example.com')
    db.session.add(new_user)
    db.session.commit()

    return 'User created successfully! Welcome aboard, {}!'.format(new_user.username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()