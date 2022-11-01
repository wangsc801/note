from models.user import User
from app import db

def add(user:User):
    db.session.add(user)
    db.session.commit()

def get_by_id(id:int):
    return User.query.filter(User.visable=='1' and User.id==id).first()
