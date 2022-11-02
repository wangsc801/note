import service.setting.category_serv as category_serv
from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_login import login_required

categrory_page = Blueprint('categrory_page', __name__,
                           template_folder='templates/setting/category')


class CategoryForm(FlaskForm):
    name = StringField('name', validators=[
                       DataRequired(), Length(min=1, max=32)])


@categrory_page.route('/')
@login_required
def categrory_index():
    categories = category_serv.get_all()
    return render_template('setting/category/index.html', title="category", categories=categories)


@categrory_page.route('/add', methods=['GET', 'POST'])
@login_required
def category_add():
    form = CategoryForm()
    if form.validate_on_submit():
        category_serv.add(form.name.data)
        return redirect(url_for('categrory_page.categrory_index'))
    return render_template('setting/category/add.html', form=form)
