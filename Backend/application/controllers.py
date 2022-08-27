from flask import Flask
from flask import render_template, redirect
from flask import current_app as app
from application.database import db
from application.models import *
import sys, requests
from flask import jsonify



@app.route('/dashboard', methods = ['GET','POST'])
def index():
    # return render_template('index.html')
    tracker_details = db.session.query(Dashboard_db).all()
    json_obj = {'Tracker_id' : tracker_details[0].Tracker_id,
                'Tracker_name' : tracker_details[0].Tracker_name,
                'Tracker_desc' : tracker_details[0].Tracker_desc}
    return jsonify(json_obj) 

@app.route('/done', methods = ['GET','POST'])
def call():
    return 'OK'