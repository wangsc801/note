from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import toml

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    myconfig = toml.load('config.toml')
    app.config['SECRET_KEY'] = myconfig['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = myconfig['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = myconfig['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    return app
