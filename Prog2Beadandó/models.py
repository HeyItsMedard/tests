from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    video_id = db.Column(db.String(11), nullable=False, unique=True)
    views = db.Column(db.Integer)
    creator = db.Column(db.String(255))
    thumbnail_url = db.Column(db.String(255))
    maxres_thumbnail = db.Column(db.Boolean)

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    played_time = db.Column(db.Integer, default=0)
    best_score = db.Column(db.Integer, default=0)
    current_score = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    average_score = db.Column(db.Float, default=0.0)
    registration_date = db.Column(db.DateTime, nullable=False)
    login_date = db.Column(db.DateTime, nullable=True)  # Default is None
    logout_date = db.Column(db.DateTime, nullable=True) # Default is None