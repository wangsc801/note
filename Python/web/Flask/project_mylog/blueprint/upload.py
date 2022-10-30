from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import Blueprint, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from app import myconfig

upload_page = Blueprint('upload_page', __name__,
                        template_folder='templates/upload')


class AttachmentForm(FlaskForm):
    attachment = FileField('Your attachment', validators=[
                           FileRequired(), FileAllowed(['jpg', 'png', 'mp4', 'm4v'], "media file only")])


@upload_page.route('/', methods=('GET', 'POST'))
def index():
    form = AttachmentForm()
    if form.validate_on_submit():
        f = form.attachment.data
        secured_filename = secure_filename(f.filename)
        root_path = Path(myconfig['UPLOAD_ROOT_DIR'])
        upload_filepath = root_path.joinpath(secured_filename)
        print(f"\n\n=====\n{secured_filename}\n-------\n{upload_filepath}\n")
        f.save(upload_filepath)
        return redirect(url_for('upload_page.index'))
    return render_template('upload/index.html', title="upload", form=form)
