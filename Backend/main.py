import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_cors import CORS
app = None
def create_app():
    app = Flask(__name__, template_folder = "templates")
    CORS(app)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)

    app.app_context().push()
    return app

app = create_app()

from application.controllers import *

if __name__ == '__main__':
    app.run(debug=True, port= 8080)