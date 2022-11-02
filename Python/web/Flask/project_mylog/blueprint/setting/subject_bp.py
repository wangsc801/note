import service.setting.category_serv as category_serv
import service.setting.subject_serv as subject_serv
from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length
from flask_login import login_required

subject_page = Blueprint('subject_page', __name__,
                         template_folder='templates/setting/subject')


class SubjectForm(FlaskForm):
    name = StringField('name', validators=[
                       DataRequired(), Length(min=1, max=32)])
    category_list = SelectField(
        'categories', validators=[DataRequired()], coerce=int)


@subject_page.route('/')
@login_required
def subject_index():
    subjects = subject_serv.get_all()
    return render_template('setting/subject/index.html', title="subject", subjects=subjects)


@subject_page.route('/add', methods=['GET', 'POST'])
@login_required
def subject_add():
    form = SubjectForm()
    category_name_list = [(int(c.id), c.name)
                          for c in category_serv.get_all()]
    form.category_list.choices = category_name_list
    if form.validate_on_submit():
        subject_serv.add(form.name.data, form.category_list.data)
        return redirect(url_for('subject_page.subject_index'))
    return render_template('setting/subject/add.html', form=form)
