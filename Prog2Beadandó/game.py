# game.py
from models import Video
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game:
    def __init__(self, db):
        self.db = db
        self.video1 = None
        self.video2 = None
        self.displayed_video_ids = set()  # Az eddig megjelenített videók azonosítóit tartalmazó halmaz

    def get_random_videos(self):
        print("get_random_videos")
        # Az első körben mindkét videónak válasszunk randomot
        if self.video1 is None or self.video2 is None:
            self.video1 = Video.query.order_by(func.random()).first()
            self.video2 = Video.query.filter(Video.id != self.video1.id).order_by(func.random()).first()
        else:
            # A következő körökben csak video2 kapjon randomot
            self.video1 = self.video2
            self.video2 = Video.query.filter(~Video.id.in_([self.video1.id] + list(self.displayed_video_ids))).order_by(func.random()).first()

        # Ellenőrizd a konzolon, hogy a videók helyesen lettek-e kiválasztva
        print("Video 1:")
        print(f"Title: {self.video1.title}")
        print(f"Thumbnail URL: {self.video1.thumbnail_url}")
        print(f"Views: {self.video1.views}")
        print('-------------------')
        
        print("Video 2:")
        print(f"Title: {self.video2.title}")
        print(f"Thumbnail URL: {self.video2.thumbnail_url}")
        print(f"Views: {self.video2.views}")
        print('-------------------')

        # Ellenőrizzük, hogy van-e két különböző videó
        if self.video1 is None or self.video2 is None:
            return None, None

        # Hozzáadjuk az azonosítókat a megjelenített videók halmazához
        self.displayed_video_ids.add(self.video1.id)
        self.displayed_video_ids.add(self.video2.id)

        return self.video1, self.video2
