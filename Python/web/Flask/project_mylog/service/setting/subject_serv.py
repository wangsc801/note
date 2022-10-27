import dao.setting.subject_dao as subject_dao
from models.setting.subject import Subject


def get_all():
    return subject_dao.get_all()


def add(name: str, category_id: int):
    category = Subject(name, category_id)
    subject_dao.add(category)
