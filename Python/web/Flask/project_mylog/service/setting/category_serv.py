import dao.setting.category_dao as category_dao
from models.setting.category import Category


def get_all():
    return category_dao.get_all()


def add(name: str):
    category = Category(name)
    category_dao.add(category)
