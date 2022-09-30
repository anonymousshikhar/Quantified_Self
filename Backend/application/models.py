from datetime import time
# from sqlalchemy import ForeignKey
from sqlalchemy.sql.operators import desc_op
# from sqlalchemy.orm import relationship
from application.database import *

engine = create_engine("sqlite:////home/unknown-me/Stuffs/Project/Vue-js/healthify/backend/db_directory/quantified_self.sqlite3", echo=True)


class credentials(db.Model):
    __tablename__ = 'credentials'
    user_id = db.Column(db.String, primary_key = True)
    user_name = db.Column(db.String)
    user_email = db.Column(db.String)
    password = db.Column(db.String)
    tracker_detail = db.relationship("trackerlist", backref = 'User')

    def __init__(self, id, name, email, passw):
        self.user_id = id
        self.user_name = name
        self.user_email = email
        self.password = passw

class trackerlist(db.Model):
    __tablename__ = 'trackerlist'
    user_id = db.Column(db.String, db.ForeignKey("credentials.user_id"))
    tracker_id = db.Column(db.String, primary_key = True)
    tracker_name = db.Column(db.String)
    tracker_desc = db.Column(db.String)
    tracker_type = db.Column(db.String)
    tracker_pri_question = db.Column(db.String)
    each_tracker = db.relationship('Log')
    
    def __init__(self, uid, tid, name, desc, type, ques=None):
        self.user_id = uid
        self.tracker_id = tid
        self.tracker_name = name
        self.tracker_desc = desc
        self.tracker_type = type
        self.tracker_pri_question = ques

class Log(db.Model):
    __tablename__ = 'logs'
    tracker_id = db.Column(db.String, db.ForeignKey('trackerlist.tracker_id'))
    log_id = db.Column(db.Integer, primary_key=True)
    log_value = db.Column(db.String)
    remark = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def __init__(self, tid, value, note, time):
        self.tracker_id = tid
        self.log_value = value
        self.remark = note
        self.timestamp = time

db.metadata.create_all(bind=engine)

# class tracker(db.Model):
#     __abstract__ = True
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     value = db.Column(db.Integer)
#     timestamp = db.Column(db.Time)
#     note = db.Column(db.String)

# def get_model(tab_name):
#     tablename = tab_name
#     class_name = tab_name
#     Model = type(class_name, (tracker,), {
#         '__tablename__': tablename
#     })


#     return Model
    