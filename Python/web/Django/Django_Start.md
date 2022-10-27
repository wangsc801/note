# Django Start

[official tutorial reference](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

## Create a project

`$ django-admin startproject mysite`

### project structure

```text
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Run development server

`$ python manage.py runserver 8000`

then visit `http://localhost:8000`

## Create the Polls app

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

Your apps can live anywhere on your [Python path](https://docs.python.org/3/tutorial/modules.html#tut-searchpath). In this tutorial, we’ll create our poll app in the same directory as your `manage.py` file so that it can be imported as its own top-level module, rather than a submodule of `mysite`.

To create your app, make sure you’re in the same directory as `manage.py` and type this command:

`$ python manage.py startapp polls`

### polls structure

```text
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## First view

Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

```text
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

In the `polls/urls.py` file include the following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The [path()](https://docs.djangoproject.com/en/4.1/ref/urls/#django.urls.path) function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. At this point, it’s worth reviewing what these arguments are for.

`arguement: route` is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.

`arguement: view` When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.

`arguement: kwargs` Arbitrary keyword arguments can be passed in a dictionary to the target view.

`arguement: name` Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

The next step is to point the root URLconf at the `polls.urls` module. In `mysite/urls.py`, add an import for `django.urls.include` and insert an [include()](https://docs.djangoproject.com/en/4.1/ref/urls/#django.urls.include) in the `urlpatterns` list, so you have:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

then visit `http://localhost:8000/polls`