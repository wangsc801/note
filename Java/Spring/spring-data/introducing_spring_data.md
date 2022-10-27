# Introducing Spring Data

## JPA

### 1. 创建数据库

```sql
drop database if exists `jpa` DEFAULT CHARACTER SET utf8;

create database `jpa`;
```

用于测试的数据

```SQL
create table if not exists `jpa`.`media_file`(
    `id` int unsigned auto_increment primary key,
    `filename` varchar(20),
    `owner_id` int unsigned
);

insert into `jpa`.`media_file` (`filename`,`owner_id`) values ("textbook.txt",1);
insert into `jpa`.`media_file` (`filename`,`owner_id`) values ("flower.jpg",1);
insert into `jpa`.`media_file` (`filename`,`owner_id`) values ("In the Mood for Love.mkv",2);
insert into `jpa`.`media_file` (`filename`,`owner_id`) values ("She's Gone.mp3",2); 
```

### 2. 创建项目

依赖

* spring-boot-starter-data-jpa
* spring-boot-starter-web
* druid
* mysql-connector-java

### 3. 数据库配置

```yml
spring:
  datasource: 
    type: com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql:///jpa
    username: root
    password: root
  jpa: 
    show-sql: true
    database: mysql
    hibernate: 
      ddl-auto: update
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL5InnoDBDialect
```

dialect为`org.hibernate.dialect.MySQLDialect`时，MySQL引擎为`MyISAM`。

dialect为`org.hibernate.dialect.MySQL5InnoDBDialect`时，MySQL引擎为`InnoDB`。

### 4. 创建实体类

```java
import javax.persistence.Id;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Transient;

@Entity(name="media_file")
public class MediaFile {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Integer id;
    @Column(name="filename",nullable=false)
    private String filename;
    @Column(name="owner_id",nullable=false)
    private Integer ownerId;
    @DateTimeFormat(pattern = "yyyy-MM-dd HH-mm-ss")
    private Date created;
    @Transient
    private String remark;

    // omit getter and setter
}
```

* @Entity注解表示该类是一个实体类，在项目启动时会根据该类自动生成一张表，表的名称即@Entity注解中name的值，如果不配置name，默认表名为类名。
* @Entity(name="user")和@Entity @Table(name="user")等效。
* 所有的实体类都要有主键，@Id注解表示该属性是一个主键，@GeneratedValue注解表示主键自动生成，strategy则表示主键的生成策略。
* 默认情况下，生成的表中字段的名称就是实体类中属性的名称，通过@Column注解可以定制生成的字段的属性，name表示该属性对应的数据表中字段的名称，nullable表示该字段非空。
* @DateTimeFormat注解中pattern格式中含有"."会出错，例如"yyyy-MM-dd HH.mm.ss"
* @Transient注解表示在生成数据库中的表时，该属性被忽略，即不生成对应的字段。

在Spring Data

```java
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import demo.spring.jpa.entity.MediaFile;

public interface MediaFileDao extends JpaRepository<MediaFile, Integer>{
    List<MediaFile> findAll();
    @Query(value="select * from media_file where id=(select max(id) from media_file)",nativeQuery=true)
    List<MediaFile> getMaxIdMediaFile();
    @Query("select f from media_file f where f.id=:id")
    MediaFile getMediaFileById(@Param("id")Integer id);
}
```

JPA中，只要方法的定义符合既定规范，Spring Data就能分析出开发者的意图，从而避免开发者定义SQL。所谓的既定规范，就是一定的方法命名规则。支持的命名规则如表所示。

| KeyWords           | method examples         | respective SQL            |
| ------------------ | ----------------------- | ------------------------- |
| And                | findByNameAndAge        | where name=? and age=?    |
| Or                 | findByNameOrAge         | where name=? or age=?     |
| Equals             | findByAgeIs             | where age=?               |
| Between            | findByAgeBetween        | where age between ? and ? |
| LessThan           | findByAgeLessThan       | where age < ?             |
| LessThanEquals     | findByAgeLessThanEquals | where age <= ?            |
| GreaterThan        | findByAgeGreaterThan    | where age > ?             |
| After              | findByAgeAfter          | where age > ?             |
| Before             | findByAgeBefore         | where age < ?             |
| IsNull             | findByNameIsNull        | where name is null        |
| IsNotNull, NotNull | findByNameNotNull       | where name is not null    |
| Not                | findByGenderNot         | where gender <> ?         |
| In                 | findByAgeIn             | where age in (?)          |
| NotIn              | findByAgeNotIn          | where age not in (?)      |

Failed to initialize JPA EntityManagerFactory: No identifier specified

去掉SpringBootApplication里的 disable DataSource

```java
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import demo.spring.jpa.dao.MediaFileDao;
import demo.spring.jpa.entity.MediaFile;

@Service
public class MediaFileService {
    @Autowired(required=true)
    MediaFileDao mediaFileDao;

    public List<MediaFile> findAll(){
        return mediaFileDao.findAll();
    }

    public void add(MediaFile mf) {
        mediaFileDao.save(mf);
    }

    public List<MediaFile> getMaxIdMediaFile(){
        return mediaFileDao.getMaxIdMediaFile();
    }

    public MediaFile getMediaFileById(Integer id) {
        return mediaFileDao.getMediaFileById(id);
    }
}
```

```java
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import demo.spring.jpa.entity.MediaFile;
import demo.spring.jpa.service.MediaFileService;

@RestController
public class MediaFileController {
    @Autowired
    MediaFileService mfService;

    @GetMapping("/findAll")
    public String findAll() {
        List<MediaFile> list=mfService.findAll();
        return list.toString();
    }

    @GetMapping("/find/{id}")
    public String find(@PathVariable("id")Integer id) {
        MediaFile mf=mfService.getMediaFileById(id);
        return mf.getFilename();
    }
}
```
