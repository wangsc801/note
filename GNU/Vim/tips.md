# VIM Tips

## 关闭un~文件

编辑vimrc

追加`set noundofile`

## 字母大小写

g~ 反转大小写

gu 转换为小写

gU 转换为大写

gUU 转换当前行为大写

gUap 把整段文字转换为大写

由daw为删除当前单词推出，gUaw为转换当前单词为大写

## 删除字符

c3w 删除3个单词并进入插入模式

<Ctrl-h> 删除前一个字符

<Ctrl-w> 删除前一个单词

<Ctrl-u> 删除至行首

在bash-shell中也可以使用它们

## 更多删除

dap 删除整个段落

当一个操作符命令被连续执行两次时，它作用于当前行

dd 删除当前行

删除某一行，例如第10行

```text
:10d
或
10G
dd
```

## 跳转

跳转到某一行，例如第三行
```text
3G
或
:3
```

快速跳回原先的位置 `<Ctrl - o>`

:! 在vim中执行shell命令，例如:!ls

:shell 执行多个shell命令，输入exit返回vim

显示行号
`:set number`

## 视图模式

zz 当前行显示在窗口正中

在可视模式选中块中，o可在选中块左右两端切换

## 其他

`>>` 缩进当前行


用次数做简单的算术运算
`#box{ background-position: 0px 0px }`
改成
`#box{ background-position: 30px 0px }`
光标在#上

`30<Ctrl-a>`

`<Ctrl-x>`为减法运算