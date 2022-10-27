from flask import Blueprint, render_template

upload_page = Blueprint('upload_page', __name__,
                        template_folder='templates/upload')


@upload_page.route('/')
def index():
    return render_template('index.html', title="upload")
