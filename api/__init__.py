from flask import Flask
from api.config import Config
from flask_sqlalchemy import SQLAlchemy

# from model import Task

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from api.routes import config_routes
config_routes(app, db)

