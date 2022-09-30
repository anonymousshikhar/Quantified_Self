from flask_restful import Resource, reqparse
from application.database import db
from application.models import *
from flask import jsonify, request
from flask_cors import cross_origin
from datetime import datetime


class login_validate(Resource):
    
    @cross_origin()
    def post(self):  
        user_req = reqparse.RequestParser()
        user_req.add_argument('email', type = str, help = 'Email is a string')
        user_req.add_argument('pass', type = str, help = 'Password is a string')

        data = user_req.parse_args()
        registered_user = credentials.query.filter_by(user_email = data['email']).all()
        if(registered_user):
            if(registered_user[0].user_email == data['email'] and registered_user[0].password == data['pass']):
                data_json = {'email':registered_user[0].user_email, 'password':registered_user[0].password, 'user_id':registered_user[0].user_id, 'user_name': registered_user[0].user_name }
                return jsonify(data_json), 200
            else:
                return 'Credentials not matched', 301
        else:
            return 'User not registered', 300

class signup(Resource):
    
    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            email_list = db.session.query(credentials.user_email).all()
            
            name = json['name']
            email = json['email']
            password = json['pass']
            for i in email_list:
                if (email == i[0]):
                    return 'Email Already Registered', 302
            user_id = str('2022') + str(len(email_list))
            data = credentials(user_id, name, email, password)
            db.session.add(data)
            try:
                db.session.commit()
                return jsonify(json), 200
            except:
                return 'Error in committing', 401
        else:
            return 'NOT OK', 400


class get_trackerlist(Resource):
 
    @cross_origin()
    def get(self):
        args = request.args
        tracker_list = trackerlist.query.filter(trackerlist.user_id == args.get('uid')).all()
        data= []
        for tracker in tracker_list:
            data.append({'tracker_id': tracker.tracker_id, 'tracker_name':tracker.tracker_name, 'tracker_desc': tracker.tracker_desc, 'tracker_type':tracker.tracker_type, 'tracker_pri_question': tracker.tracker_pri_question})
        return jsonify(data)
    
    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            # model = get_model(json['tracker_name'])
            # print(model)
            user_info = json['user_info']
            user_id = str(user_info['user_id'])
            tracker_name = json['tracker_name']
            tracker_desc = json['tracker_desc']
            tracker_type = json['tracker_type']
            tracker_pri_question = json['tracker_pri_question']
            initial = tracker_name[0].capitalize()
            tracker_id = str(initial) + str(user_info['user_id'])
            data = trackerlist(user_id,tracker_id, tracker_name, tracker_desc, tracker_type, tracker_pri_question)
            db.session.add(data)
            try:
                db.session.commit()
                return jsonify(json),200
            except:
                return 'Error in commiting', 401


class get_tracker_detail(Resource):

    @cross_origin()
    def get(self):
        arg = request.args
        curr_tracker_id = arg.get('tid')
        tracker_details = Log.query.filter(Log.tracker_id == curr_tracker_id).all()
        tracker_type = trackerlist.query.filter(trackerlist.tracker_id == curr_tracker_id).first().tracker_type
        print(tracker_details, tracker_type )
        json_data = []
        if (tracker_details):
            for details in tracker_details:
                json_data.append({'tid': details.tracker_id, 'value': details.log_value, 'remark':details.remark, 'timestamp': details.timestamp, 'ttype': tracker_type, 'vid': details.log_id})
        else:
            json_data.append({'tid': curr_tracker_id, 'ttype': tracker_type})
        print(json_data)
        return jsonify(json_data)
    
    
    
    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            curr_time = datetime.now() 
            # dd/mm/YY H:M:S
            # curr_time = curr_time.strftime("%d-%m-%Y %H:%M:%S")
            print(json, curr_time)
            tracker_id = json['tracker_id']
            log_value = json['log_value']
            log_note = json['log_note']
            data = Log(tracker_id, log_value, log_note, curr_time)
            db.session.add(data)
            try:
                db.session.commit()
                return jsonify(json), 200        
            except Exception as e:
                return 'Error in committing' + str(e), 401


    @cross_origin()
    def put(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            tid = json['tid']
            print(tid)
            tques = db.session.query(trackerlist).filter(trackerlist.tracker_id == tid).first()
            print(tques)
            tques.tracker_pri_question= json['tques']
            print(tques)
            db.session.add(tques)
            try:
                db.session.commit()
                return {'status':'success'}, 200
            except:
                return {'status': 'Error in committing'}
class get_tracker_by_id(Resource):
    @cross_origin()
    def get(self):
        arg = request.args
        log_id = arg.get('id')
        log_details = Log.query.filter(Log.log_id == log_id).first()
        print(log_id, log_details)
        data = {'vid': log_id, 'log_value': log_details.log_value, 'log_note': log_details.remark}
        return jsonify(data)

    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)
            log_details = Log.query.filter(Log.log_id == json['log_id']).first()

            log_details.log_value = json['log_value']
            log_details.log_note = json['log_note']
            curr_time = datetime.now() 
            log_details.timestamp = curr_time
            try:
                db.session.commit()
                return {'status': 'success'},200
            except:
                return {'status': 'Error in committing'}, 401
        else:
            return {'status': 'failed'}, 300


    def delete(self):
        arg = request.args
        log_id = arg.get('id')
        log_details = Log.query.filter(Log.log_id == log_id).first()
        print(log_details)
        db.session.delete(log_details)
        try:
            db.session.commit()
            return {'status': 'success'},200
        except:
            return {'status': 'Error in committing'}, 401



class tracker_setting(Resource):
    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)
            tracker_details = trackerlist.query.filter(trackerlist.tracker_id == json['tid']).first()
            print(tracker_details)
            tracker_details.questions = str(json['questions'])
            print(tracker_details.questions)
            try:
                db.session.commit()
                return {'status': 'success'},200
            except Exception as e:
                return {'status': 'Error in committing'+ str(e)}, 401

class Report_generation(Resource):
    @cross_origin()
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json) 
            return {'status':'success'}, 200
