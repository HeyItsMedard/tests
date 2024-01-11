# game.py
from models import Video
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from flask import session

db = SQLAlchemy()

class Game:
    displayed_video_ids = set() # Stores the IDs of the videos that have already been displayed
    def __init__(self, db):
        self.db = db

    def get_random_videos(self):
        """Returns two random videos from the database in first round, 
        any other rounds, a random for the second video and a video that is not in displayed_video_ids"""
        if session.get('video1_id') is None and session.get('video2_id') is None:
            # Get a random video from the database
            video1 = self.db.session.query(Video).order_by(func.random()).first()
            # Get another random video from the database
            video2 = self.db.session.query(Video).order_by(func.random()).first()

            session['video1_id'] = video1.id
            session['video2_id'] = video2.id

            self.displayed_video_ids.add(video1.id)
            self.displayed_video_ids.add(video2.id)

            self.print_videos(video1, video2) # kisegítésnek
        else:
            # Swap the videos
            video1 = self.db.session.query(Video).get(session['video2_id'])
            # Get another random video from the database that is not in displayed_video_ids
            video2 = self.db.session.query(Video).filter(Video.id.notin_(self.displayed_video_ids)).order_by(func.random()).first()
            
            session['video1_id'] = video1.id
            session['video2_id'] = video2.id

            self.displayed_video_ids.add(video2.id)

            self.print_videos(video1, video2) # kisegítésnek

        return video1, video2
            
    def print_videos(self, video1, video2):
        """Used for debugging purposes"""
        print("Video 1:")
        print(f"Title: {video1.title}")
        print(f"Thumbnail URL: {video1.thumbnail_url}")
        print(f"Views: {video1.views}")
        print('-------------------')
        
        print("Video 2:")
        print(f"Title: {video2.title}")
        print(f"Thumbnail URL: {video2.thumbnail_url}")
        print(f"Views: {video2.views}")
        print('-------------------')

    def check_guess(self, video1, video2, guess):
        """Returns True if the guess is correct, False otherwise"""
        if guess == 'more' and video2.views >= video1.views:
            return True
        elif guess == 'less' and video2.views < video1.views:
            return True
        else:
            return False
    
    def reset(self):
        """Resets the game"""
        print("Resetting game...")
        self.displayed_video_ids.clear()
        session.pop('video1_id', None)
        session.pop('video2_id', None)