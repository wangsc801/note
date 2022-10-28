from app import create_app, db
from blueprint.setting import setting_page,categrory_page,subject_page
from blueprint.home import home_page
from blueprint.upload import upload_page

from models.setting.category import Category
from models.setting.subject import Subject

app = create_app()

app.register_blueprint(home_page, url_prefix="/")
app.register_blueprint(upload_page, url_prefix="/upload")
app.register_blueprint(setting_page, url_prefix="/setting")
app.register_blueprint(categrory_page, url_prefix="/setting/category")
app.register_blueprint(subject_page, url_prefix="/setting/subject")

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    print(f"urls -> \n{app.url_map}")
    app.run(port=5000,debug=True)
