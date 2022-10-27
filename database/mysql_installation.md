# MySQL Installation

## Option File

[reference: Creating an Option File](https://dev.mysql.com/doc/refman/8.0/en/windows-create-option-file.html)

[reference: Using Option Files](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)

create configuration file `{MYSQL_HOME}\my.cnf`

{MYSQL_HOME}\my.cnf

```ini
[mysqld]
port=3306
# set basedir to your installation path
basedir=E:\\mysql
# set datadir to the location of your data directory
datadir=E:\\mydata\\data
```

|File Name|Purpose|
|---|---|
|  %WINDIR%\my.ini, %WINDIR%\my.cnf  |  Global options  |
|  C:\my.ini, C:\my.cnf              |  Global options  |
|BASEDIR\my.ini, BASEDIR\my.cnf      |  Global options  |
|defaults-extra-file                 |The file specified with --defaults-extra-file, if any|

`/` may be used in Windows path names and is treated as `\`.

## Initialize

 `{MYSQL_HOME}\bin\mysqld.exe --initialize --console`

console shows

```text
[Server] A temporary password is generated for root@localhost: 0tfn(fKbL*sl
```

## Starting MySQL from the Windows Command Line

`{MYSQL_HOME}\bin\mysqld.exe`

## Alter Password

`{MYSQL_HOME}\bin\mysql.exe -uroot -p`

Then input the temporary password.

For example, if you want to change the password to 'root', execute the following command:

`ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';`

## Install Service

`{MYSQL_HOME}\bin\mysqld.exe --install mysql`

## Remove Service

`{MYSQL_HOME}\bin\mysqld.exe --remove`
