# Basic JavaFX

## Build With Gradle

### initialize project

`gradle init`

### edit build.gradle

```groovy
plugins {
    // Apply the application plugin to add support for building a CLI application in Java.
    id 'application'
    id 'org.openjfx.javafxplugin' version '0.0.9'
}

javafx {
    version = "17.0.1"
    modules = [ 'javafx.controls', 'javafx.fxml' ]
}
```

## Build With Maven

### pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>indi.wangsc</groupId>
    <artifactId>hotline</artifactId>
    <version>0.0.1</version>
    <packaging>jar</packaging>

    <name>hotline</name>
    <!-- <url>http://maven.apache.org</url> -->

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <java.version>17</java.version>
        <javafx.version>17.0.1</javafx.version>
        <javafx.maven.plugin.version>0.0.8</javafx.maven.plugin.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.openjfx</groupId>
            <artifactId>javafx-controls</artifactId>
            <version>${javafx.version}</version>
        </dependency>

        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.openjfx</groupId>
                <artifactId>javafx-maven-plugin</artifactId>
                <version>${javafx.maven.plugin.version}</version>
                <configuration>
                    <mainClass>indi.wangsc.hotline.App</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

then

`mvn clean javafx:run`

## Launch Window

### Core Codes

```java
package priv.demo.launch;

import javafx.application.Application;
import javafx.stage.Stage;

public class Launch extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        stage.show();
    }
}
```

```java
package priv.demo.launch;

import javafx.application.Application;

public class Main {
    public static void main(String[] args) {
        Application.launch(Launch.class);
    }
}
```

## Title, Icon, Size of Window

```java
import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class HelloStage extends Application {
    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        primaryStage.setTitle("JavaFx Application");
        primaryStage.getIcons().add(new Image("asset/icon/icons8-app-24.png"));
        
        // set width and height of window, and its limit
        primaryStage.setWidth(400);
        primaryStage.setHeight(300);
        primaryStage.setMaxWidth(600);
        primaryStage.setMaxHeight(500);
        
        // listening the change of window-size, then print current window-size to console
        primaryStage.heightProperty().addListener(new ChangeListener<Number>() {
            @Override
            public void changed(ObservableValue<? extends Number> observable, Number oldValue, Number newValue) {
                System.out.println("new height: "+newValue.doubleValue());
            }
        });
        primaryStage.widthProperty().addListener(new ChangeListener<Number>() {
            @Override
            public void changed(ObservableValue<? extends Number> observable, Number oldValue, Number newValue) {
                System.out.println("new weight: "+newValue.doubleValue());
            }
        });
        // primaryStage.setFullScreen(true);
        // primaryStage.setScene(new Scene(new Group()));
        
        primaryStage.show();
    }
}
```

## Modality

### Core Code

```java
import javafx.application.Application;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class Stages extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        // stage1
        Stage stage1 = new Stage();
        stage1.setTitle("stage1");
        stage1.setHeight(360);
        stage1.setWidth(240);
        // initial position
        stage1.setX(100);
        stage1.setY(100);
        stage.initStyle(StageStyle.UNDECORATED);
        stage1.show();

        // stage2
        Stage stage2 = new Stage();
        stage2.setTitle("stage2");
        stage2.setHeight(420);stage2.setWidth(480);
        stage2.initStyle(StageStyle.DECORATED);
        stage2.show();

        // stage3
        Stage stage3 = new Stage();
        stage3.setTitle("stage3");
        stage3.setHeight(320);stage3.setWidth(200);
        stage3.initStyle(StageStyle.UTILITY);
        stage3.initOwner(stage2);
        stage3.initModality(Modality.WINDOW_MODAL);
        stage3.show();
    }
}
```

### Notice

`Platform.exit()` closing all windows.

### Style

```text
A stage has one of the following styles:

StageStyle.DECORATED - a stage with a solid white background and platform decorations.

StageStyle.UNDECORATED - a stage with a solid white background and no decorations.

StageStyle.TRANSPARENT - a stage with a transparent background and no decorations.

StageStyle.UTILITY - a stage with a solid white background and minimal platform decorations.
```
