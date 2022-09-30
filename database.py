from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from application.config import LocalDevelopmentConfig

engine = create_engine("sqlite:////home/unknown-me/Stuffs/Project/Vue-js/healthify/backend/db_directory/quantified_self.sqlite3", echo=True)
print(engine)
Base = declarative_base()
db = SQLAlchemy()
db.metadata.create_all(bind=engine)