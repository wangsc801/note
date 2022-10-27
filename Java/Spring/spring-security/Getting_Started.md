# spring-security Getting Started

## Adding Dependency

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.7.4</version>
</parent>

 ...

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
<dependency>
    <groupId>com.guicedee.services</groupId>
    <artifactId>bouncycastle</artifactId>
    <version>1.2.2.1-jre17</version>
</dependency>
```

## Password Encode and Match

```java
public class App {
    public static void main(String[] args) {
        SCryptPasswordEncoder encoder=new SCryptPasswordEncoder ();
        String result=encoder.encode("myPassword.");
        boolean matched=encoder.matches("myPassword.",result);
        System.out.println(matched);
    }
}
```
