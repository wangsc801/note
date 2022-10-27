from flask import Blueprint, render_template

home_page = Blueprint('home_page', __name__,
                      template_folder='templates')


@home_page.route('/')
def home_index():
    return render_template('index.html', title="home")
