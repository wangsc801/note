# Error Log - Maven

## Dependency

### 未解析的依赖项: 'PaperWork:indi.wangsc.paperwork:jar:unknown'

```xml
<dependency>
    <groupId>PaperWork</groupId>
    <artifactId>indi.wangsc.paperwork</artifactId>
    <systemPath>${project.basedir}/src/main/resources/lib/PaperWork.jar</systemPath>
</dependency>
```

solution

```xml
<dependency>
    <groupId>PaperWork</groupId>
    <artifactId>indi.wangsc.paperwork</artifactId>
    <scope>system</scope>
    <systemPath>${project.basedir}/src/main/resources/lib/indi/wangsc/paperwork/PaperWork.jar</systemPath>
</dependency>
```

### Jar File Within The Project Directory

```text
Some problems were encountered while building the effective model for indi.wangsc:MayorHotline:jar:1.0-SNAPSHOT

'dependencies.dependency.systemPath' for PaperWork:indi.wangsc.paperwork:jar should not point at files within the project directory, ${project.basedir}/lib/indi/wangsc/
paperwork/PaperWork.jar will be unresolvable by dependent projects @ line 33, column 25

It is highly recommended to fix these problems because they threaten the stability of your build.

For this reason, future Maven versions might no longer support building such malformed projects.
```

solution

set the `<systemPath>` to `${settings.localRepository}` but not `${project.basedir}`

```xml
<dependency>
    <groupId>PaperWork</groupId>
    <artifactId>indi.wangsc.paperwork</artifactId>
    <version>1.0-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${settings.localRepository}/indi/wangsc/paperwork/PaperWork.jar</systemPath>
</dependency>
```

add `requires indi.wangsc.paperwork;` to module-info.java

```java
module indi.wangsc.mayorhotline {
    requires javafx.controls;
    requires javafx.fxml;
    requires indi.wangsc.paperwork;

    opens indi.wangsc.mayorhotline to javafx.fxml;
    exports indi.wangsc.mayorhotline;
}
```

**But, the best way to solve the problem is**: use `${java.home}`

```xml
<dependency>
    <groupId>indi.wangsc.paperwork</groupId>
    <artifactId>PaperWork</artifactId>
    <version>0.1</version>
    <scope>system</scope>
    <systemPath>${java.home}/lib/PaperWork.jar</systemPath>
</dependency>
```
