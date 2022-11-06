# Flask Start

## A Minimal Application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

### app = Flask(__name__)

__Create an instance of this class__. The first argument is the name of the application’s module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for __resources__ such as __templates and static files__.

### @app.route("/")

Use the route() __decorator__ to tell Flask what URL should __trigger our function__.

### return

The function returns the message we want to display in the user’s browser. The __default__ content type is __HTML__, so HTML in the string will be rendered by the browser.

### run the script

Save it as `hello.py` or something similar. Make sure to not call your application `flask.py` because this would __conflict__ with Flask itself.

As a shortcut, if the file is named `app.py` or `wsgi.py`, you don’t have to set the `FLASK_APP` environment variable.

To run the application, use the `flask` command or `python -m flask`. Before you can do that you need to tell your terminal the application to work with by exporting the `FLASK_APP` environment variable:

```bash
$ export FLASK_APP=hello
$ flask run
 * Running on http://127.0.0.1:5000/
```

## Debug Mode

The `flask run` command can do more than just start the development server. By enabling __debug mode__, the server will __automatically reload__ if code changes, and will show an interactive debugger in the browser if an error occurs during a request.

The debugger allows executing arbitrary Python code from the browser. It is protected by a pin, but still represents a major security risk. __Do not run the development server or debugger__ in a production environment.

```bash
export FLASK_ENV=development
flask run
```

```cmd
> set FLASK_ENV=development
> flask run
```

## HTML escaping

When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from __injection attacks__. HTML templates rendered with Jinja, introduced later, will do this automatically.

`escape()`, shown here, can be used manually. It is omitted in most examples for brevity, but you should always be aware of how you’re using __untrusted data__.

```python
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

If a user managed to submit the name `<script>alert("bad")</script>`, escaping causes it to be __rendered as text__, rather than running the script in the user’s browser.

`<name>` in the route captures a value from the URL and passes it to the view function. These __variable rules__ are explained below.

## Varible Rules

You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

### Converter types

#### string

(default) accepts any text without a slash

#### int

accepts positive integers

#### float

accepts positive floating point values

#### path

like string but also accepts slashes

#### uuid

accepts UUID strings

## URL Building

To build a URL to a specific function, use the url_for() function. It __accepts__ the name of the __function__ as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

## HTTP Methods

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

## Static Files

Create a folder called static in your package or next to your module and it will be available at /static on the application.

To generate URLs for static files, use the special 'static' endpoint name:

`url_for('static', filename='style.css')`

The file has to be stored on the filesystem as static/style.css.
