# Lambda

## Introduction

### Example: Runnable

Before Java 1.8

```java
public class RunnableDemo {
    public static void main(String... args) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("anonymous inner class.");
            }
        }).start();
    }
}
```

Lambda style

```java
public class RunnableDemo {
    public static void main(String... args) {
        new Thread(() -> System.out.println("Lambda")).start();
    }
}
```

Lambda expression to variable

```java
public class RunnableDemo {
    public static void main(String... args) {
        Runnable r = () -> System.out.println("lambda expression implementing the run method.");
        new Thread(r).start();
    }
}
```

### Example: FilenameFilter

Before Java 1.8

```java
import java.io.File;
import java.io.FilenameFilter;

public class Demo {
    public static void main(String... args) {
        File directory =new File("D:\\library\\Documents\\EBOOK\\O'Reilly");
        String[] names=directory.list(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                return name.endsWith(".pdf");
            }
        });
        for(var name:names){
            System.out.println(name);
        }
    }
}
```

Lambda style

```java
import java.io.File;

public class Demo {
    public static void main(String... args) {
        File directory =new File("D:\\library\\Documents\\EBOOK\\O'Reilly");
        String[] names=directory.list((File dir, String name)-> {
                return name.endsWith(".epub");
            });
        for(var name:names){
            System.out.println(name);
        }
    }
}
```
