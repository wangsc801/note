from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import func
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    create_at = db.Column(db.DateTime, server_default=func.now())
    visable = db.Column(db.String(1), nullable=False, default="1")
    UniqueConstraint("id", "name")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
