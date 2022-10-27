# Java APIs

## 字符串

### replace和replaceAll的用法

[java中replace和replaceAll的用法](https://blog.csdn.net/quietbxj/article/details/108292819)

replace：使用字符串进行替换。

replaceAll：优先使用正则匹配，不匹配再使用字符串进行替换。

```java
String s1="hello.hello.hello";
//replace使用字符串进行替换
System.out.println(s1.replace(".","#"));
//replaceAll转为正则表达式进行替换，"."匹配任何单个字符
System.out.println(s1.replaceAll(".","#"));

// 输出结果
// hello#hello#hello
// #################
```

### 反转字符串

```java
String str=String.format("%s@%s", new StringBuffer("user").reverse()," here");
```

## 文件系统

### mkdir()与mkdirs()

mkdir()只能创建单层目录文件夹

mkdirs()可以创建多层目录文件夹
