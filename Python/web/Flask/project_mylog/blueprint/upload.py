from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from app import myconfig

upload_page = Blueprint('upload_page', __name__,
                        template_folder='templates/upload')


class AttachmentForm(FlaskForm):
    attachment = StringField('Your attachment', validators=[DataRequired()])


@upload_page.route('/', methods=('GET', 'POST'))
def index():
    form = AttachmentForm()
    if request.method == 'GET':
        return render_template('upload/index.html', title="upload", form=form)
    if form.validate_on_submit():
        f = form.attachment.data
        filename = secure_filename(f.filename)
        upload_filepath=Path.joinpath(myconfig['UPLOAD_ROOT_DIR'], filename)
        print(f"\n===\n{upload_filepath}\n===\n")
        f.save(upload_filepath)
        # return redirect(url_for('upload_page.index'))
        return render_template('upload/index.html', title="upload", form=form)
