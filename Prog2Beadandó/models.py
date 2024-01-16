from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy import Interval
from datetime import timedelta

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
    best_score = db.Column(db.Integer, default=0)
    current_score = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    average_score = db.Column(db.Float, default=0.0)
    registration_date = db.Column(db.DateTime, nullable=False)
    login_date = db.Column(db.DateTime, nullable=True)  # Default is None
    logout_date = db.Column(db.DateTime, nullable=True) # Default is None
    played_time = db.Column(Interval, default=timedelta(seconds=0))

    def formatted_played_time(self):
        total_seconds = self.played_time.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        return f"{hours}H {minutes}M {seconds}S"
    
    def update_average_score(self, new_score):
        # Frissítsd az összpontszámot és a játékok számát
        self.total_score += new_score
        self.games_played += 1
        # Számold ki az átlagpontszámot
        self.average_score = self.total_score / self.games_played