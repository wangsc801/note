# Error Log - Spring-boot

## Upload

### Maximum upload size exceeded

```text
MaxUploadSizeExceededException: Maximum upload size exceeded
org.apache.tomcat.util.http.fileupload.impl.

FileSizeLimitExceededException: The field files exceeds its maximum permitted size of 1048576 bytes.]
```

solution

```yml
spring:
  servlet:
    multipart:
      max-file-size: 2MB
```
