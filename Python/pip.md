# PIP

## Modify pip Mirror

create file `pip.ini` in `C:\Users\{username}\pip`.

pip.ini:

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

for checking: `pip config list`.

## Encountered error while trying to install package

```text
× Encountered error while trying to install package.
╰─> mysqlclient
```

[solution](https://www.pudn.com/news/62e0aeed55398e076be335cb.html)

visit `https://www.lfd.uci.edu/~gohlke/pythonlibs/`.

Ctrl+F for search the package.

Then download the package you want and install: `pip install {filename}.whl`
