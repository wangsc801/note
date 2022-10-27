# Introducing React

[尚硅谷React教程](https://www.bilibili.com/video/BV1wy4y1D7JT)

[中文文档](https://react.docschina.org/)

## 相关js库

1. react.js

   react核心库。

2. react-dom.js

   提供操作DOM的React扩展库。

3. babel.min.js

   解析JSX语法代码转为JS代码的库。

## 渲染虚拟DOM

示例：Hello React

```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Hello React</title>
</head>
<body>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <!-- show "Hello React!" -->
    <div id="hello"></div>
    <script type="text/babel">
        const VDOM=(<h1>
                <i>Hello React!</i>
            </h1>)
        ReactDOM.render(VDOM,document.getElementById("hello"))
    </script>
</body>
</html>
```

## JSX

### JSX语法规则

- 定义虚拟DOM时， 不要写引号。
- 标签中混入JS表达式时要用{}。
- 样式的类名指定不要用class， 要用className。
- 内联样式， 要用style={{key：value}}的形式去写。
- 只有一个根标签
- 标签必须闭合
- 标签首字母

1. 若小写字母开头， 则将改标签转为html中同名元素， 若html中无该标签对应的同名元素，则报错。
2. 若大写字母开头， React就去渲染对应的组件， 若组件没有定义， 则报错。

示例：遍历显示数组

```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>List</title>
</head>
<body>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <h1>Frameworks</h1>
    <div id="list"></div>
    <script type="text/babel">
        const frameworkList=['Angular','React','Vue'];
        const VDOM=(<ul>
                {
                    frameworkList.map((item,index)=>{
                        return <li key={index}>{item}</li>
                    })
                }
            </ul>)
        ReactDOM.render(VDOM,document.getElementById("list"))
    </script>
</body>
</html>
```

输出：

```text
Frameworks

Angular

React

Vue
```

## 模块与组件

### 模块

理解：向外提供特定功能的js程序，一般就是一个js文件
为什么要拆成模块：随着业务逻辑增加，代码越来越多且复杂。
作用：复用j5,简化js的编写，提高js运行效率

### 组件

理解：用来实现局部功能效果的代码和资源的集合(html/css/js/image等等)
为什么：一个界面的功能更复杂
作用：复用编码，简化项目编码，提高运行效率

### 模块化

当应用的js都以模块来编写的，这个应用就是一个模块化的应用

### 组件化

当应用是以多组件的方式实现，这个应用就是一个组件化的应用

### 函数式组件

```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>List</title>
</head>
<body>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <div id="demo"></div>
    <script type="text/babel">
        function Demo(){
            return <h1>Testing funtional component.</h1>
        }
        ReactDOM.render(<Demo/>,document.getElementById("demo"))
    </script>
</body>
</html>
```

输出：

```text
Testing funtional component.
```

## 面向对象

### 示例

```js
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    introduce() {
        return `My name is ${this.name}, ${this.age} years old.`;
    }
}
const guy = new Person("Alex", 20);
console.log(guy.introduce());
```

控制台输出：

```text
My name is Alex, 20 years old.
```

### 继承

```js
class Student extends Person {
    constructor(name, age, grade) {
        super(name, age);
        this.grade = grade;
    }

    introduce(){
        return `My name is ${this.name}, ${this.age} years old. ${this.grade} grade student.`;
    }

    study(){
        return `studying`;
    }
}

const student=new Student("Alice",18,1);
console.log(student.introduce());
console.log(student.study());
```

## 类式组件

```js
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Class-Component</title>
</head>
<body>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <div id="demo"></div>
    <script type="text/babel">
        class MyComponent extends React.Component {
            render(){
                // render放在哪里的？——MyComponent的原型对象上，供实例使用
                // render中的this是谁？ ——MyComponent的实例对象。
                return <h3>This is class-component</h3>
            }
        }
        ReactDOM.render(<MyComponent/>,document.getElementById("demo"))
        /*
        执行了ReactDOM.render(<MyComponent/>,...)之后，发生了什么？
        1. React解析组件标签，找到了MyComponent组件；
        2. 发现组件是使用类定义的，随后new出来该类的实例，并通过该实例调用到原型上的render方法；
        3. 将render返回的虚拟DOM转为真实DOM，随后呈现在页面中。
        */
    </script>
</body>
</html>
```
