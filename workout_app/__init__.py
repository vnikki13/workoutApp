import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


# create the app
app = Flask(__name__)
# Create secrete key for CSRF protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

from workout_app import routes
