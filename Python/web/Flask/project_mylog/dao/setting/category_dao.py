from models.setting.category import Category
from app import db


def get_all():
    return Category.query.filter(Category.visable=='1').all()


def add(category: Category):
    db.session.add(category)
    db.session.commit()
