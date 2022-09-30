from celery.schedules import crontab
from application.celery_workers import celery
# from celery import Celery
from datetime import datetime, timedelta
import smtplib
from flask import current_app as app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from application.database import db
from application.models import *
from jinja2 import Template
from weasyprint import HTML
import uuid


# celery = Celery()
celery.conf.timezone = 'Asia/Kolkata'

SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS = 'email@test.com'
SENDER_PASSWORD = ""

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=20, minute=47),create_report.s())
    sender.add_periodic_task(crontab(hour=21, minute=50),send_alert.s())

@celery.task
def send_mail(to_address='shikhar@test', subject="HELLO", message="WElcome!!! PFA", attachment_file = None):
    msg = MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['TO'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(message, "html"))

    if attachment_file:
        with open(attachment_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={attachment_file}",
        )

        msg.attach(part)

    s = smtplib.SMTP(host=SMPTP_SERVER_HOST, port=SMPTP_SERVER_PORT)
    s.login(SENDER_ADDRESS, SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()

    return True

@celery.task
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
    u_mail = db.session.query(credentials).filter(credentials.user_id == data[0]['uid']).first().user_email
    
    file_name = str(u_name) + "_Monthly_Report.pdf"
    html.write_pdf(target=file_name)
    print("inside creation")

    send_mail.delay(to_address=u_mail, subject="Monthly Report by The LOGIT", attachment_file=file_name)

@celery.task
def print_curr_time():
    print("Start")
    now = datetime.now()
    print("Now : ",now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and time =", dt_string)
    print("Conplete")
    return dt_string 



@celery.task
def send_alert():
    uid = db.session.query(trackerlist.user_id).distinct().all()
    curr_time = datetime.now()
    print(curr_time)
    a_day_ago = curr_time - timedelta(days=1)
    for id in uid:
        safe = False
        u_name = db.session.query(credentials).filter(credentials.user_id == id[0]).first().user_name
        u_mail = db.session.query(credentials).filter(credentials.user_id == id[0]).first().user_email
        json_data = []
        tid = db.session.query(trackerlist).with_entities(trackerlist.tracker_id, trackerlist.tracker_name, trackerlist.tracker_desc).filter(trackerlist.user_id == id[0]).all()
        for t_id in tid:
            
            last_time = db.session.query(Log).with_entities(Log.timestamp).filter(Log.tracker_id == t_id[0]).order_by(Log.timestamp).all()
            print(last_time)
            if (last_time[0][-1] > a_day_ago):
                print('User_id: ' + str(id[0]) + ' -----Safe as last time is: ' + str(last_time[0][-1]))
                safe = True
                break
        if (not safe): 
            message = f'''
                        Hello {u_name}, 
                        {{ space }}
                        It has been detected that you have not logged in any of the trackers since more than 24 hours.
                        Therefore, we kindly request you to login to your dashboard and log your activity in the tracker.
                        {{ space }}
                        Warm Regards
                        Team 'The LOGIT'''
            send_mail.delay(to_address=u_mail, subject="Missed logging alert by The LOGIT", message=message)