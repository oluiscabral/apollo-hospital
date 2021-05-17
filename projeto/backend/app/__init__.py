'''
@author: oluiscabral
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import api

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)

Migrate(app, db)

from . import models

app.register_blueprint(api)
