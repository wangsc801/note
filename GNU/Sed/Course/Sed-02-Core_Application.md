# 二、核心应用

## （一） 查找：p

| 查找格式           | 意义                                   |
|--------------------|----------------------------------------|
| '2p'               | 指定行号进行查找                       |
| '1,5p'             | 指定行号范围进行查找                   |
| '/colou?r/p'       | 类似于 grep 过滤，//里可以写正则表达式 |
| '/10:00/,/11:00/p' | 范围的过滤                             |

例子：输出 name.txt 从第 4 行到最后一行的内容

`sed -n '4,$p' name.txt`

### 1、输出包含“is”的行

`sed -n '/is/p' name.txt`

output

```console
102 Chris
103 Dannis
104 Elise
```

### 2、输出包含“4”和“5”的行

`sed -n '/[45]/p' name.txt`

output

```console
104 Elise
105 Frankenstein
```

### 3、输出包含数字“2”至“4”的行

`sed -n '/[2-4]/p' name.txt`

output

```console
102 Chris
103 Dannis
104 Elise
```

### 4、拓展正则

sed 加上-nr（拓展正则）选项后才支持“+”等正则表达式。例如`sed -nr '/[0-9]+/p' name.txt`。

### 5、范围过滤，输出包含 102 至 105 的行

`sed -n '/102/,/105/p' name.txt`

output

```console
102 Chris
103 Dannis
104 Elise
105 Frankenstein
```

## （二） 删除：d

| 删除格式           | 意义                                   |
|--------------------|----------------------------------------|
| '2d'               | 指定行号进行删除                       |
| '1,5d'             | 指定行号范围进行删除                   |
| '/colou?r/d'       | 类似于 grep 过滤，//里可以写正则表达式 |
| '/10:00/,/11:00/d' | 删除的范围                             |

不要带-n 选项 `sed '3d' name.txt`

ouput

```console
100 Alice
101 Ben
103 Dannis
104 Elise
105 Frankenstein
```

`sed '3d' name.txt`只是输出时不显示第 3 行，原文件仍包含`102 Chris`。

`cat name.txt`

output

```console
100 Alice
101 Ben
102 Chris
103 Dannis
104 Elise
105 Frankenstein
```

### 案例：删除空行和包含#的行

```console
egrep -v '^$|#' /etc/ssh/sshd_config
sed -r '/^$|#/d' /etc/ssh/sshd_config
```

或者运用取反“!”

`sed -nr '/^$|#/!p' /etc/ssh/sshd_config`

## （三） 插入：cai

| 命令 | 选项                   |
|------|------------------------|
| c    | replace 替换这行的内容 |
| a    | append 追加到行尾      |
| i    | insert 插入到行首      |

### 1、在第二行后增加一行“---”

`sed '2a---' name.txt`

output

```console
100 Alice
101 Ben
---
102 Chris
103 Dannis
104 Elise
105 Frankenstein
```

### 2、把第一行换成“100 Anna”

`sed '1c100 Anna' name.txt`

output

```console
100 Anna
101 Ben
102 Chris
103 Dannis
104 Elise
105 Frankenstein
```

### 3、在文本文件末尾添加文字

方法一：cat

```console
cat >>name.txt<<'EOF'
> 106 Grace
> 107 Hellen
> 108 Isabel
> EOF
```

方法二：sed

-i: edit files in place

`sed -i '$a106 Grace\n107 Hellen\n108 Isabel' name.txt`

## （四） 替换：s

格式

`s###g`或`s@@@g`或`s///g`

### 1、删除所有数字

`sed 's#[0-9]##g' name.txt`

output

```console
 Alice
 Ben
 Chris
 Dannis
 Elise
 Frankenstein
 Grace
 Hellen
 Isabel
```

不加 g 只会匹配每一行第一个数字

`sed 's#[0-9]##' name.txt`

output

```console
00 Alice
01 Ben
02 Chris
03 Dannis
04 Elise
05 Frankenstein
06 Grace
07 Hellen
08 Isabel
```
