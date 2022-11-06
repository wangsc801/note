# Deploy

## firewall

ufw commands example.

```bash
apt-get install ufw
ufw enable
ufw allow 5000
ufw status
ufw reload
ufw delete allow 5000
```

## run app by gunicorn

`gunicorn -w 2 -b :5000 "run:app"`

`run` means `./run.py`, `app` is a variable.

### run.py

```python
from app import create_app

app = create_app()
```

### _app.py

```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '__this_is_a_secret_key__'
    return app
```
