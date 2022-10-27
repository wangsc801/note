# Introducing Bash

[各种bash手册格式](http://www.gnu.org/software/bash/manual/)

[bash手册网页版](http://www.gnu.org/software/bash/manual/html_node/index.html)

[GNU Manuals Online](http://www.gnu.org/manual/)

## 管道符(pipeline)

A pipeline is a sequence of one or more commands separated by one of the control operators ‘|’ or ‘|&’.

*example:*

```console
$ seq 15 | grep 1
1
10
11
12
13
14
15
$ seq 15 | grep 1 | wc -l
7
```

The output of each command in the pipeline is connected via a pipe to the input of the next command. That is, each command reads the **previous** command’s **output**. This connection is performed before any redirections specified by the command.

## 重定向(Redirections)

Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell. Redirection allows commands’ **file** handles to be duplicated, opened, closed, made to refer to different **files**, and can change the **files** the command reads from and **writes** to.

### Redirecting Input

Redirection of input causes the file whose name results from the expansion of word to be opened for reading on file descriptor n, or the standard input (file descriptor 0) if n is not specified.

The general format for redirecting input is:

`[n]<word`

*example:*

```bash
$ cat calculations
10+5
10*5
10%5
$ bc < calculations
15
50
0
```

### Redirecting Output

Redirection of output causes the file whose name results from the expansion of word to be opened for writing on file descriptor n, or the standard output (file descriptor 1) if n is not specified. If the file does not exist it is created; if it does exist it is truncated to zero size.

The general format for redirecting output is:

`[n]>[|]word`

*example:*

```bash
$ uname -a > sys_version.txt
$ cat sys_version.txt
Linux primary 5.4.0-94-generic #106-Ubuntu SMP Thu Jan 6 23:58:14 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

### Appending Redirected Output

Redirection of output in this fashion causes the file whose name results from the expansion of word to be opened for appending on file descriptor n, or the standard output (file descriptor 1) if n is not specified. If the file does not exist it is created.

The general format for appending output is:

`[n]>>word`

*example:*

```bash
$ lsb_release -a >> sys_version.txt
No LSB modules are available.
$ cat sys_version.txt
Linux primary 5.4.0-94-generic #106-Ubuntu SMP Thu Jan 6 23:58:14 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal
ubuntu@primary:~$
```
