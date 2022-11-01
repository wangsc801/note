from flask import Blueprint, render_template
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from app import login_manager
from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


sign_page = Blueprint('sign_page', __name__,
                      template_folder='templates')


class SigninForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(), Length(min=1, max=32)])
    password = PasswordField('password', validators=[
        DataRequired(), Length(min=1, max=32)])
    submit = SubmitField('submit')


@sign_page.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        login_user()
    return render_template('index.html', title="home")
