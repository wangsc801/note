from models.user import User
from app import db

def add(user:User):
    db.session.add(user)
    db.session.commit()

def get_by_id(id:int):
    return User.query.filter(User.id==id and User.visable=='1').first()

def get_by_username(username:str):
    return User.query.filter(User.username==username and User.visable=='1').first()
