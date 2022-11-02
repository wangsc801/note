from flask import Blueprint, render_template, flash, request
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from app import login_manager
from dao.user_dao import get_by_id
from models.user import User


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.username = 'admin'
    user.password = 'admin'
    return user


sign_page = Blueprint('sign_page', __name__,
                      template_folder='templates')


class SigninForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(), Length(min=1, max=32)])
    password = PasswordField('password', validators=[
        DataRequired(), Length(min=1, max=32)])
    submit = SubmitField('submit')


@sign_page.route('/in', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User()
        user.username = 'admin'
        user.password = 'admin'
        login_user(user)
        flash('\n\n===\nlogined!!\n')
        # next = request.args.get('next')
        # print('\n---\n'+str(next))
        return render_template('/index.html', title="index")
    else:
        print("un valied....")
    return render_template('sign/signin.html', title="Sign in", form=form)
