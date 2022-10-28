import service.setting.category_serv as category_serv
import service.setting.subject_serv as subject_serv
from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

setting_page = Blueprint('setting_page', __name__,
                         template_folder='templates/setting')
categrory_page = Blueprint('categrory_page', __name__,
                           template_folder='templates/setting/category')
subject_page = Blueprint('subject_page', __name__,
                         template_folder='templates/setting/subject')


@setting_page.route('/')
def setting_index():
    return render_template('setting/index.html', title="setting")


# ######
# category
# ######

class CategoryForm(FlaskForm):
    name = StringField('name', validators=[
                       DataRequired(), Length(min=1, max=32)])


@categrory_page.route('/')
def categrory_index():
    categories = category_serv.get_all()
    return render_template('setting/category/index.html', title="category", categories=categories)


@categrory_page.route('/add', methods=['GET', 'POST'])
def category_add():
    form = CategoryForm()
    if request.method == 'GET':
        return render_template('setting/category/add.html', form=form)
    if form.validate_on_submit():
        category_serv.add(form.name.data)
        return redirect(url_for('categrory_page.categrory_index'))

# ######
# subject
# ######


class SubjectForm(FlaskForm):
    name = StringField('name', validators=[
                       DataRequired(), Length(min=1, max=32)])
    category_list = SelectField(
        'categories', validators=[DataRequired()], coerce=int)


@subject_page.route('/')
def subject_index():
    subjects = subject_serv.get_all()
    return render_template('setting/subject/index.html', title="subject", subjects=subjects)


@subject_page.route('/add', methods=['GET', 'POST'])
def subject_add():
    form = SubjectForm()
    category_name_list = [(int(c.id), c.name)
                          for c in category_serv.get_all()]
    form.category_list.choices = category_name_list
    if request.method == 'GET':
        return render_template('setting/subject/add.html', form=form)
    if form.validate_on_submit():
        subject_serv.add(form.name.data, form.category_list.data)
        return redirect(url_for('subject_page.subject_index'))
