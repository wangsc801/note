from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import func
from app import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    create_at = db.Column(db.DateTime, server_default=func.now())
    visable = db.Column(db.String(1), nullable=False, default="1")
    # db.relationship('Category',backref="subject")
    UniqueConstraint("id")

    def __init__(self, name, category_id):
        self.name = name
        self.category_id = category_id

    def __repr__(self):
        return '<Category %r>' % self.name
