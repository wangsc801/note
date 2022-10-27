# Express Start

## Build

### express-generator

[reference](https://www.npmjs.com/package/express-generator)

create the app

`npm install -g express-generator`

`express --view=hbs /tmp/foo && cd /tmp/foo`

command line options

| options               | description                                             |
| --------------------- | ------------------------------------------------------- |
| --version             | output the version number                               |
| -e, --ejs             | add ejs engine support                                  |
| --pug                 | add pug engine support                                  |
| --hbs                 | add handlebars engine support                           |
| -H, --hogan           | add hogan.js engine support                             |
| -v, --view `<engine>` | add view `<engine>` support (defaults to jade)          |
| --no-view             | use static html instead of view engine                  |
| -c, --css `<engine>`  | add stylesheet `<engine>` support (defaults to plain css)|
| --git                 | add .gitignore                                          |
| -f, --force           | force on non-empty directory                            |
| -h, --help            | output usage information                                |

### install dependencies

`npm install`

### start the app

install nodemon

[reference](https://www.npmjs.com/package/nodemon)

`npm install nodemon`

`nodemon /bin/www`

server listen on 3000 by default.

## Form

/views/test_form.ejs

```html
<!DOCTYPE html>
<html>
  <head>
    <title>test form</title>
    <link rel="stylesheet" href="/stylesheets/style.css" />
  </head>
  <body>
    <form method="post" action="/test_form/do_post">
      <input name="name" type="text" />
      <br />
      <input name="email" type="text" />
      <br />
      <input type="submit" />
      <br />
    </form>
  </body>
</html>
```

/routes/test_form.js

```js
var express = require("express");
var router = express.Router();

var process = (req, res) => {
  console.log("name: " + req.body.name);
  console.log("email: " + req.body.email);
  res.redirect(303, "/test_form");
};

router.post("/do_post", (req, res) => {
  process(req, res);
});

router.get("/", (req, res) => {
  res.render("test_form");
});

module.exports = router;
```

/app.js

```js
var testFormRouter = require("./routes/test_form");

app.use(express.urlencoded({ extended: false }));

app.use("/test_form", testFormRouter);
```
