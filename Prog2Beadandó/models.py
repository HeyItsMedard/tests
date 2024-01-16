from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy import Interval
from datetime import timedelta
import threading
import os
from sqlalchemy import ARRAY

import matplotlib
matplotlib.use('Agg')  # Háttérhasználat beállítása
import matplotlib.pyplot as plt

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
    last_10_scores = db.Column(MutableList.as_mutable(JSON), default=[])

    def create_plot_thread(self):
        print("Creating plot thread")
        self.plot_thread = threading.Thread(target=self.generate_plot, daemon=True)

    def add_score(self, score):
        self.last_10_scores.append(score)
        self.last_10_scores = self.last_10_scores[-10:]

    def generate_plot(self):
        print("Generating plot")
        plt.switch_backend('Agg')
        plt.plot(range(1, len(self.last_10_scores) + 1), self.last_10_scores)
        plt.xlabel('Kísérlet száma')
        plt.ylabel('Elért pontszám')
        plt.title('Előző legfeljebb 10 játék eredménye')
        plt.grid(True)

        # Beállítja az x tengely számait egész számokra
        plt.xticks(range(1, len(self.last_10_scores) + 1))

        # Ellenőrzi, hogy a kép létezik-e, és ha igen, törli
        image_path = os.path.join('Prog2Beadandó', 'static', 'stats', 'last_10_scores_plot.png')
        if os.path.exists(image_path):
            os.remove(image_path)

        plt.savefig(image_path)
        plt.close()


    def formatted_played_time(self):
        total_seconds = self.played_time.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours}H {minutes}M {seconds}S"
    
    def update_average_score(self, new_score):
        self.total_score += new_score
        self.games_played += 1
        self.average_score = self.total_score / self.games_played