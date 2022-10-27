# 第一部分 模式

## .命令

### 缩进

光标在第二行行首

```
line one
line two
line three
line four
缩进为
line one
    line two
        line three
            line four
```

解

```
>G
j.
j.
```

### 为多行代码末尾添加分号

```
A;
[ESC]
j.
j.
(重复"j."直到为所有需要末尾添加分号的行都添加上)
```

### 为+号前后添加一个空格

光标在+号前方

```
String sql = "select * from "+table+" where "+arg+">0";
```

解

```
f+
s(空格)+(空格)
[ESC]
;.
;.
;.
```

### 选择性替换文本

光标在第一行的 days 上

```
3 days
one days
2 days
a days
another days
改成
3 days
one day
2 days
a day
another day
```

解

```
*
cw
day
[ESC]
n
n
.
n
.
```

### 反向删除

光标在字母 x 上

```
This is Marx
```

解 1

```
db
x
```

解 2

```
b
dw
```

解 3

```
daw
```

其中解 3 最佳，因为其可用“.”重复反向删除，且粒度妥当。

---

## 插入模式

### 在插入模式中更正错误

<Ctrl-h> 删除前一个字符
<Ctrl-w> 删除前一个单词
<Ctrl-u> 删除至行首
在 bash-shell 中也可以使用它们

### 不离开插入模式，粘贴寄存器中的文本

光标在开头

```
Practice Vim, by Drew Neil
Read Drew Neil's
改成
Practice Vim, by Drew Neil
Read Drew Neil's Practice Vim.
```

解

```
yt,
jA(space)
<Ctrl-r>0
.<ESC>
```

### 随时随地做运算

光标在开头

```
6 chairs, each costing $35, total $
```

解

```
A
<Ctrl-r>=
6*35<Enter>
```

### 用字符编码插入非常用字符

在插入模式下，<Ctrl-v>065 会输入“A”。
要输入 Unicode 字符，例如“だ”，则先要知道其 Unicode 码为 a4c0。
执行<Ctrl-v>ua4c0 后即可输入“だ”。

### 用替换模式替换已有文本

光标在开头

```
Typing in Insert mode extends the line. But in Replace mode the line length doesn't change.
改成
Typing in Insert mode extends the line, but in Replace mode the line length doesn't change.
```

解

```
f.
R,(space)b
<ESC>
```

## 可视模式

### 重复执行面向行的可视命令

光标在 print a, 行行首。将 while 下面的两行缩进两次

```python
def fib(n):
    a, b = 0, 1
    while a < n:
print a,
a, b = b, a+b
fib(32)
```

解

```
Vj
>.
```

### 只要可能，最好用操作符命令，而不是可视命令

将标签内文本改为大写

```html
<a href="#">one</a>
<a href="#">two</a>
<a href="#">three</a>
```

解

```
vit
U
j.
j.
会使three变成THRee
最佳做法是
gUit
j.
j.
```

如果想使用点命令能够重复某些有用的工作，那么最好要远离可视模式，选用操作符命令。

### 在长短不一的高亮块后添加文本

在每一行后添加分号

```
var foo = 1
var bar = 'a'
var foobar = foo + bar
```

解

```
<Ctrl-v>
jj$
A;
<ESC>
```

## 命令行模式

### 用‘t’命令复制行

把第 5 行的内容复制到第 1 行下面，光标在第一行

```
1 #a{
2 padding: 2px;
3 }
4 #b{
5 margin: 0 auto;
6 padding: 2px;
7 }
```

解

```
:2t.
```

把第 4 行到第 7 行的内容复制到文本末尾
解

```
:4,7t$
或
:4,$t$
```

:t.相当于 yyp，yyp 会使用寄存器，:t.则不会

### 为每一行末尾添加分号

```php
$a = 1
$b = 2
$c = 3
$d = 4
$e = 5
```

解

```
A;<ESC>
jVG
:'<,'>normal .
```

### 为某些行添加注释

还以上一例为例
解

```
:1,$%normal i//m
```

### 把当前单词插入命令行

将 margin 替换为 nigram. 光标在#a 的 margin 上

```css
#a {
  margin: 0 auto;
}
#b {
  margin: 0 auto;
}
#c {
  margin: 0 auto;
}
```

解

```
*
cw
nigram<ESC>
:%s//<Ctrl-r><Ctrl-w>/g
```

### 运行 Shell 命令

#### 执行 Shell 中的程序

```
:!
在vim中执行shell命令，例如:!ls

:shell
执行多个shell命令，输入exit返回vim
```

#### 把缓冲区内容作为标准输入或输出

```
var=10
echo "I have $var apples."
echo "I am $var years old."
```

**运行此 shell**

```
:write !sh
```

运行结果
I have 10 apples.
I am 10 years old.

**将此脚本写入到名为 script 的文件里**

```
:write! script
```

\*\*将 shell 中的命令以标准输出插入到光标下方，例如将磁盘利用信息插入到文本末尾

```
G
:read !df -h
```
