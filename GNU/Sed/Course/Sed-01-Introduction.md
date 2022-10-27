# 一、概述

## （一） 格式

示例

| 命令 | 选项 | 命令功能      | 参数     |
|------|------|---------------|----------|
| sed  | -r   | 's#old#new#g' | file.txt |

核心功能

| 命令 | 选项                      |
|------|---------------------------|
| s    | 替换 substitute           |
| p    | 显示 print                |
| d    | 删除（以行为单位） delete |
| cai  | 增加 （c/a/i）            |

## （二） 过程

- 找谁（文件参数）
- 干啥（命令功能）

例如
`sed -n "3p" name.txt`

(name.txt)

```console
100 Alice
101 Ben
102 Chris
103 Dannis
104 Elise
105 Frankenstein
```

`sed -n "3p" name.txt`打印 name.txt 的第 3 行 Chris，有了`-n`只打印 Chris，不打印其他的行。
