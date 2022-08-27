from datetime import time
from sqlalchemy.sql.operators import desc_op
from .database import db

class Dashboard_db(db.Model):
    __tablename__ = 'all_trackers'
    Tracker_id = db.Column(db.Integer, primary_key = True)
    Tracker_name = db.Column(db.String)
    Tracker_desc = db.Column(db.String)
    Last_review = db.Column(db.String)

    def __init__(self, name, desc, time=None):
        self.Tracker_name = name
        self.Tracker_desc = desc
        self.Last_review = time