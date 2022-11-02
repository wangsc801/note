from app import create_app, db
from blueprint.setting_bp import setting_page,categrory_page,subject_page
from blueprint.home_bp import home_page
from blueprint.upload_bp import upload_page
from blueprint.sign_bp import sign_page

from models.setting.category import Category
from models.setting.subject import Subject

app = create_app()

app.register_blueprint(home_page, url_prefix="/")
app.register_blueprint(upload_page, url_prefix="/upload")
app.register_blueprint(setting_page, url_prefix="/setting")
app.register_blueprint(categrory_page, url_prefix="/setting/category")
app.register_blueprint(subject_page, url_prefix="/setting/subject")
app.register_blueprint(sign_page, url_prefix="/sign")

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    print(f"urls -> \n{app.url_map}")
    app.run(port=5000,debug=True)
