from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import toml

db = SQLAlchemy()

myconfig = toml.load('config.toml')


def create_app():
    app = Flask(__name__)
    CORS(app, resources=r'/*')
    app.config['SECRET_KEY'] = myconfig['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = myconfig['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = myconfig['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    return app
