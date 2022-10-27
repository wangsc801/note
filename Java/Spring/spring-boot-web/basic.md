# Basic

Spring Boot version: 2.6.0

## Profile

开发者在项目发布之前，一般需要频繁地在开发环境、测试环境以及生产环境之间进行切换，这个时候大量的配置需要频繁更改，例如数据库配置、redis配置、mongodb配置、jms配置等。频繁修改带来了巨大的工作量，Spring对此提供了解决方案（@Profile注解），Spring Boot则更进一步提供了更加简洁的解决方案，Spring Boot中约定的不同环境下配置文件名称规则为application-{profile}.properties，profile占位符表示当前环境的名称，具体配置步骤如下：

### 1. 创建配置文件

首先在resources目录下创建两个配置文件：application-dev.properties和application-prod.properties，分别表示开发环境中的配置和生产环境中的配置。其中，application-dev.properties文件的内容如下：
`server.port=8080`

application-prod.properties文件内容如下
`server.port=80`

### 2. 配置application.properties

application.properties文件内容如下
`spring.profiles.active=dev`

这个表示使用application-dev.properties配置文件启动项目，若将dev改为prod，则表示使用application-prod.properties启动项目。项目启动成功后，就可以通过相应的端口进行访问了。

### 3. 在代码中配置

对于第二步在application.properties中添加的配置，我们也可以在代码中添加配置来完成，在启动类的main方法上添加如下代码，可以替换第二步的配置：

    SpringApplicationBuilder builder=new SpringApplicationBuilder(Chapter013Application.class);
    builder.application().setAdditionalProfiles("prod");
    builder.run(args);

### 4. 项目启动时配置

对于第2步和第3步提到的两种配置方式，也可以在将项目打成jar包后启动时，在命令行动态指定当前环境，示例命令如下：

`java -jar chapter01-3-0.0.1-SNAPSHOT.jar --spring.profiles.active=prod`

## Controller - GetMapping

    ```java
    package com.example;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;

    @SpringBootApplication
    public class DemoApplication {
        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }
    }
    ```

    ```java
    package com.example.controller;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class Hello {

        @GetMapping("/hello")
        public String hello(@RequestParam(value="name",defaultValue="World") String name) {
            return String.format("Hello %s", name);
        }
    }
    ```

visit localhost:8080/hello?name=Alice

*Browser shows:* Hello Alice

## Upload File

### application.yml

    ```yaml
    server: 
        port: 8080
    spring: 
        servlet:
        multipart:
            enabled: true
            max-file-size: 256MB
            max-request-size: 1024MB
        freemarker: 
        template-loader-path: classpath:/templates
        suffix: .html
        content-type: text/html
        charset: UTF-8
        cache: false
    file:
        upload:
        path: ./upload/
    ```

### UploadFile.java

    ```java
    import java.io.File;
    import java.io.IOException;
    import java.io.InputStream;
    import java.nio.file.Files;
    import java.time.LocalDateTime;
    import java.time.format.DateTimeFormatter;
    import java.util.UUID;

    import org.apache.tika.Tika;
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RequestPart;
    import org.springframework.web.multipart.MultipartFile;

    @Controller
    public class UploadFile {
        @Value("${file.upload.path}")
        String path;

        @GetMapping("/upload")
        public String uploadPage() {
            return "upload";
        }

        private String datePath() {
            LocalDateTime now = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd/");
            File directory = new File(path + now.format(formatter));
            // if the directory didn't created,
            // exception "java.nio.file.NoSuchFileException" comes.
            if (!directory.exists()) {
                directory.mkdirs();
            }
            return now.format(formatter);
        }

        // use Tika.detect(InputStream) but not MultipartFile.getContentType()
        // because MultipartFile.getContentType() effected by file's extension.
        private String getMIME(InputStream inputStream) throws IOException {
            Tika tika = new Tika();
            /*
                * some common MIME types --- 
                * image/png .png 
                * image/gif .gif 
                * image/jpeg .jpeg,.jpg
                * video/mpeg .mpg,.mpeg 
                * video/x-msvideo .avi 
                * audio/basic .au
                * audio/midi,audio/x-midi mid,.midi 
                * audio/x-pn-realaudio .ra, .ram
                */
            String mimeInfo = tika.detect(inputStream);

            return mimeInfo;
        }

        private boolean isMimeTypeAllowed(String checkingType) {
            String[] allowedMimeTypes= {"image","audio","video"};
            for(String type : allowedMimeTypes) {
                if(checkingType.equals(type)) {
                    return true;
                }
            }
            return false;
        }

        private String getExtension(String filename) {
            int lastIndexOfDot=filename.lastIndexOf(".");
            if(lastIndexOfDot==-1) {
                return "";
            }
            return filename.substring(lastIndexOfDot);
        }

        @PostMapping("/upload")
        // the variable "files" in "@RequestPart MultipartFile[] files"
        // should be consistent with the value of name-property in
        // "<input type='file' name='files'>"
        public String upload(@RequestPart MultipartFile[] files) throws IOException {
            
            for (MultipartFile file : files) {
                // for example, if getMIME(file.getInputStream()) exerts "audio/mpeg",
                // then mimeInfo[0] equals "audio", and mimeInfo[1] equals "mpeg".
                String[] mimeInfo = getMIME(file.getInputStream()).split("/");
                if(!isMimeTypeAllowed(mimeInfo[0])) {
                    throw new IOException("-> Exception: not allowed MIME type.");
                }
                String extension = getExtension(file.getOriginalFilename());
                // random UUID filename in server
                String filename = UUID.randomUUID().toString();
                String filePath = path + datePath() + filename;
                File dest = new File(filePath);
                Files.copy(file.getInputStream(), dest.toPath());
            }
            return "upload";
        }
    }
    ```

### classpath: /templates/upload.html

注意form标签中要包含enctype="multipart/form-data"

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>upload</title>
    </head>
    <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="files"/><br>
        <input type="file" name="files"/><br>
        <input type="file" name="files"/><br>
        <input type="submit"/>
        </form>
    </body>
    </html>
    ```

出现无法找到"file.upload.path"的情况，需要用Maven重新清理并编译项目
