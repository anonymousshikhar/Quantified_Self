from flask import Flask, request, jsonify
from flask import render_template, redirect
from flask import current_app as app
from application.database import db
from application.models import *
import sys, requests
from flask import jsonify
from flask_cors import cross_origin
from application import tasks
from datetime import datetime, timedelta
from jinja2 import Template
from weasyprint import HTML
import uuid
@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        name = json['name']
        email = json['email']
        password = json['pass']
        data = credentials(name, email, password)
        print(data)
        db.session.add(data)
        try:
            db.session.commit()
            return jsonify(json), 200
        except:
            return 'Error in committing', 401
    else:
        return 'NOT OK', 400

@app.route("/hello", methods=['GET'])
def create_report():
    uid = db.session.query(trackerlist.user_id).distinct().all()
    for id in uid:
        json_data = []
        tid = db.session.query(trackerlist).with_entities(trackerlist.tracker_id, trackerlist.tracker_name, trackerlist.tracker_desc).filter(trackerlist.user_id == id[0]).all()
        for t_id in tid:
            
            details = db.session.query(Log).filter(Log.tracker_id == t_id[0]).all()

            json_data.append({'uid': id[0],'tid': t_id[0], 'tname': t_id[1], 'tdesc': t_id[2], 'logs': details})

        create_pdf_report(data=json_data)
    return 'OK'


def format_report(template_file, data={}):
    with open(template_file) as file_:
        template = Template(file_.read())
        print("inside format")
        return template.render(data=data)

def create_pdf_report(data):
    message = format_report("report_template.html", data=data)
    html = HTML(string=message)
    u_name = db.session.query(credentials).filter(credentials.user_id == data[0]['uid']).first().user_name
    file_name = str(u_name) + "_Monthly_Report.pdf"
    html.write_pdf(target=file_name)
    print("inside creation")
    

@app.route('/time')
def send_alert():
    uid = db.session.query(trackerlist.user_id).distinct().all()
    curr_time = datetime.now()
    print(curr_time)
    a_day_ago = curr_time - timedelta(days=2)
    for id in uid:
        json_data = []
        tid = db.session.query(trackerlist).with_entities(trackerlist.tracker_id, trackerlist.tracker_name, trackerlist.tracker_desc).filter(trackerlist.user_id == id[0]).all()
        for t_id in tid:
            
            last_time = db.session.query(Log).with_entities(Log.timestamp).filter(Log.tracker_id == t_id[0]).order_by(Log.timestamp).all()
            print(last_time)
            if (last_time[0][-1] > a_day_ago):
                print('User_id: ' + str(id[0]) + ' -----Safe as last time is: ' + str(last_time[0][-1]))
                break

               
    return 'OK'