# Tip

## Push to Github With Accecss Token

for example, the `access token` is "ghp_Z5BfUmzENpT1QvSt0SnOeAdQ8SfIt50Y1RUk",

execute `git remote set-url origin https://ghp_Z5BfUmzENpT1QvSt0SnOeAdQ8SfIt50Y1RUk@github.com/username/repository_name.git`

## Don't Ignore Case

`git config core.ignorecase false`

## Generate SSH Key

[reference](https://blog.csdn.net/u013778905/article/details/83501204)

```bash
ssh-keygen -t rsa -C "yourname@example.com"
cat ~/.ssh/id_rsa.pub
```

copy ssh {code}.

visit `github`->`Settings`->`SSH and GPG keys`->`New SSH key`.

paste the {code}.
