# Web Development With Node and Express - 2nd edition (Note)

## npm包

**如果你需要对项目依赖的某个包做修改，正确的做法是创建自己的分支版本库（fork）。**如果你的确这样做了，并且觉得所做的改进对其他人也会有用，祝贺你：你参与了一个开源项目！如果变更符合项目标准，你就可以提交了，这些变更会被包含进官方的包。为一个现有的包做贡献并创建定制构建超出了本书的范畴，不过如果想做贡献，活跃的开发者社区随时都可以帮助你。

**package.json文件的两大用途是描述项目和列出项目依赖。**包版本号前的脱字符（^）表示从这个指定版本号开始到下一个大版本号的版本之前都可以。比如，这个 package.json文件表示任何从 4.0.0 开始的 Express 版本都可以。因此，4.0.1 和 4.9.9 都没问题，3.4.7 则不行，5.0.0 也不行。**package.json文件的另一个用途是存储项目元数据，比如项目名、作者、许可信息，等等。**

## Node模块

**require 是用于导入模块的一个 Node 函数。**默认情况下，Node 会在 node_modules 目录下查找模块（毫无疑问，node_modules 下面会有一个 express 目录）。不过，Node 也提供了创建你自己的模块的机制（绝对不要把你自己的模块创建到 node_modules 目录下）。

### 示例：写一个“幸运饼干”的功能

首先创建一个用于存储模块的目录。你把它叫什么都可以，但叫 lib（library 的缩写）最常见。在这个目录下，创建一个名为 fortune.js 的文件。

```js
const fortuneCookies = [
    "Conquer your fears or they will conquer you.",
    "Rivers need springs.",
    "Do not fear what you don't know.",
    "You will have a pleasant surprise.",
    "Whenever possible, keep it simple.",
]
exports.getFortune = () => {
    const idx = Math.floor(Math.random()*fortuneCookies.length)
    return fortuneCookies[idx]
}
```

这里最需要注意的是全局变量`exports`的使用。如果想让什么东西在这个模块以外可见，就必须把它加到`exports`里。在这个例子中，函数`getFortune`是模块外可以用的，**但数组 fortuneCookies 是完全隐藏的。**

在app.js或路由文件的顶部导入模块。

```js
const fortune = require('./lib/fortune')
```

注意，我们在模块名前面加上了 ./ 前缀。这是在告诉 Node 不要在 node_modules 目录下查找这个模块。如果遗漏了这个前缀，就会出错。
现在，在“关于”页的路由里，可以利用模块的 getFortune 方法了：

```js
app.get('/about', (req, res) => {
res.render('about', { fortune: fortune.getFortune() } )
})
```

示例结束。

**Node 模块有时被称作 CommonJS（CJS）模块。**这是向一个更旧一些的规范致敬，Node 是从它那里得到的启发。JavaScript 语言采纳了一个正式的包机制，叫 `ECMAScript` 模块（`ESM`）。如果你一直在使用 React 或别的新潮前端语言，可能已经很熟悉`ESM`了：它使用的是`import`和`export`（而不是`exports`、`module.exports`和`require`）。更多信息请查看 Axel Rauschmayer 博士的博文“ECMAScript 6 modules: the final syntax”。
