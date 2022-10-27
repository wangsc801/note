# Tiny spring-boot-web Application

[spring-boot Getting Started Reference](https://docs.spring.io/spring-boot/docs/current/reference/html/getting-started.html#getting-started)

## Create a `spring-boot-web` Project By Maven

### Archetype

org.apache.maven.archetypes:maven-archetype-quickstart

### pom.xml

#### Creating the POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>myproject</artifactId>
    <version>0.0.1-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.4</version>
    </parent>

    <!-- Additional lines to be added here... -->

</project>
```

#### Adding Classpath Dependencies

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

### project structure

```text
├─ main
│   ├─ java
│   │   └─ indi
│   │       └─ example
│   │           ├─ App.java
│   │           └─ controller
│   │               └─ DefaultController.java
│   └─ resources
│       └─ application.yml
└─ test
    └─ java
        └─ indi
            └─ example
                └─ AppTest.java
```

## Running Code

### App.java

```java
package indi.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@EnableAutoConfiguration
@ComponentScan("indi.example.controller")
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
```

### DefaultController.java

```java
package indi.example.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DefaultController {

    @RequestMapping("/test")
    public String test(){
        return "test";
    }
}
```

### application.yml

```yml
server:
  port: 8080
```

### Visit

`localhost:8080/test` or `127.0.0.1:8080/test`
