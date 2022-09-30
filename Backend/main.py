import os
from flask import Flask
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_cors import CORS
from application import celery_workers



app = None
api = None
celery = None
def create_app():
    app = Flask(__name__, template_folder = "templates")
    CORS(app)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()


    celery = celery_workers.celery

    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config['CELERY_RESULT_BACKEND']
    )

    celery.Task = celery_workers.ContextTask
    app.app_context().push()
    
    return app, api, celery

app, api, celery = create_app()

from application.controllers import *

from application.api import *
api.add_resource(login_validate, '/api/login_validation')
api.add_resource(signup, '/api/signup')
api.add_resource(get_trackerlist, '/api/trackerlist')
api.add_resource(get_tracker_detail, '/api/tracker_data')
api.add_resource(get_tracker_by_id, '/api/tracker_data_by_id')
api.add_resource(tracker_setting, '/api/tracker_update')
api.add_resource(Report_generation, '/api/daily_report')

if __name__ == '__main__':
    app.run(debug=True, port= 5000)