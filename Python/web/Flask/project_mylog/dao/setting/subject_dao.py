from sqlalchemy import select
from models.setting.subject import Subject
from models.setting.category import Category
from app import db


def get_all():
    stmt = select(Subject.name,Category.name).join(Category, Subject.category_id == Category.id)
    return db.session.execute(stmt)
    # return Subject.query.filter(Subject.visable == '1')\
    #     .join(Category, Subject.category_id == Category.id, isouter=True).all()
    # return Subject.query.filter(Subject.visable == '1')\
    # .join(Category).filter(Subject.category_id == Category.id).all()


def add(subject: Subject):
    db.session.add(subject)
    db.session.commit()
