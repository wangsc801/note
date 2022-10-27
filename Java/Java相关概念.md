# Java相关概念

## Java Bean

[Why Java Beans are called beans - Stack Overflow](https://stackoverflow.com/questions/18609030/why-java-beans-are-called-beans)

actually when they were developing `java`, the developers consumed so much of coffee so they made it as their symbol.

and then so as the `beans` are small parts of the coding they named it as beans corresponding to small coffee beans.

Java语言欠缺属性、事件、多重继承功能。所以，如果要在Java程序中实现一些面向对象编程的常见需求，只能手写大量胶水代码。Java Bean正是编写这套胶水代码的惯用模式或约定。这些约定包括getXxx、setXxx、isXxx、addXxxListener、XxxEvent等。遵守上述约定的类可以用于若干工具或库。

1. 所有属性为private
2. 提供默认构造方法
3. 提供getter和setter
4. 实现serializable接口

[Java bean 是个什么概念？](https://www.zhihu.com/question/19773379/answer/31625054)

传统的java应用中，javabean遵循一些规范，规范如下：

1. 这个类必须具有一个公共的(public)无参构造函数；
2. 所有属性私有化（private）；
3. 私有化的属性必须通过public类型的方法（getter和setter）暴露给其他程序，并且方法的命名也必须遵循一定的命名规范。
4. 这个类应是可序列化的。（比如可以实现Serializable 接口，用于实现bean的持久性）

[javabean和spring中bean对象是一回事吗，它们分别都有什么含义？](https://www.zhihu.com/question/398256955/answer/1254321910)

- dao：英文全称是 Data Access Object，用在和数据直接交互，比如常用的是定义交互数据库的类或接口。
- bean：是存放的实体类，通常是实现了序列化接口，定义私有属性，set,get方法的普通java类。
- service：业务处理，引用了dao层的类（定义一个dao层的类作为对象属性），拥有自己的业务方法，包含处理异常、提交事务等。
- model：就是Action或Controller，作为控制器，与用户使用的页面交互数据。也有包名是controller的。
- util：工具类，通常有StringUtil，SpringUtil，DateUtil等提供一系列静态方法的类。
- view：视图，有人喜欢用它作为controller的包名。
- domain：实体类。

[Java项目开发中代码结构中的包dao、bean、service、model都是什么意思啊？](https://www.zhihu.com/question/292236048/answer/1263800733)

## JPA

JPA全称为Java Persistence API（Java持久层API），它是Sun公司在JavaEE 5中提出的Java持久化规范。它为Java开发人员提供了一种对象/关联映射工具，来管理Java应用中的关系数据，JPA吸取了目前Java持久化技术的优点，旨在规范、简化Java对象的持久化工作。很多ORM框架都是实现了JPA的规范，如：Hibernate、EclipseLink。

需要注意的是JPA统一了Java应用程序访问ORM框架的规范。

JPA为我们提供了以下规范：

1. ORM映射元数据：JPA支持XML和注解两种元数据的形式，元数据描述对象和表之间的映射关系，框架据此将实体对象持久化到数据库表中。
2. JPA 的API：用来操作实体对象，执行CRUD操作，框架在后台替我们完成所有的事情，开发人员不用再写SQL了。
3. JPQL查询语言：通过面向对象而非面向数据库的查询语言查询数据，避免程序的SQL语句紧密耦合。

### Hibernate 和JPA是什么关系呢

上面我们介绍到JPA是Java EE 5规范中提出的Java持久化接口，而Hibernate是一个ORM框架JPA和Hibernate的关系：

- JPA是一个规范，而不是框架
- Hibernate是JPA的一种实现，是一个框架

### Spring Data JPA又是啥

Spring Data JPA是在实现了JPA规范的基础上封装的一套 JPA 应用框架，虽然ORM框架都实现了JPA规范，但是在不同的ORM框架之间切换仍然需要编写不同的代码，而使用Spring Data JPA能够方便大家在不同的ORM框架之间进行切换而不需要更改代码。Spring Data JPA旨在通过将统一ORM框架的访问持久层的操作，来提高开发人的效率。

### Spring Data JPA和Hibernate的关系

Hibernate其实是JPA的一种实现，而Spring Data JPA是一个JPA数据访问抽象。也就是说Spring Data JPA不是一个实现或JPA提供的程序，它只是一个抽象层，主要用于减少为各种持久层存储实现数据访问层所需的样板代码量。但是它还是需要JPA提供实现程序，其实Spring Data JPA底层就是使用的 Hibernate实现。

总结就是

- Hibernate是JPA的一种实现，是一个框架
- Spring Data JPA是一种JPA的抽象层，底层依赖Hibernate

[来说说JPA、Hibernate、Spring Data JPA之间都是什么关系呢 作者：AI课工场](https://zhuanlan.zhihu.com/p/115507328)

按照时间线来说就明白了。

1. 开发 Hibernate 的团队开发了Hibernate;
2. 制订 J2ee 规范的团队邀请 Hibernate 的核心在 Hibernate 基础上制订了 JPA （Java Persistent API）标准。从功能上看，JPA 是 Hibernate 的子集;
3. Spring 的团队使用 Spring 对 JPA 做了封装，就是 Spring Data JPA 了。

总之，JPA 是一个 API 标准，除了 Hibernate 外，还有其它厂商的实现，例如 Eclipse 的 TopLink。Spring Data Jpa 是个对 JPA 的封装，帮助程序员以 Spring 的方式来使用 JPA。

[Hibernate和Spring Data JPA有什么区别？作者：薪概念开发](https://www.zhihu.com/question/335584253/answer/753316281)

## JTA

JTA，即Java Transaction API，JTA允许应用程序执行分布式事务处理——在两个或多个网络计算机资源上访问并且更新数据。JDBC驱动程序的JTA支持极大地增强了数据访问能力。

## JNDI

Java Naming and Directory Interface, Java命名和目录接口。是SUN公司提供的一种标准的Java命名系统接口，JNDI提供统一的客户端API，通过不同的访问提供者接口JNDI服务供应接口(SPI)的实现，由管理者将JNDI API映射为特定的命名服务和目录系统，使得Java应用程序可以和这些命名服务和目录服务之间进行交互。目录服务是命名服务的一种自然扩展。两者之间的关键差别是目录服务中对象不但可以有名称还可以有属性（例如，用户有email地址），而命名服务中对象没有属性。

### 优点

包含了大量的命名和目录服务，使用通用接口来访问不同种类的服务；
可以同时连接到多个命名或目录服务上；
建立起逻辑关联，允许把名称同Java对象或资源关联起来，而不必知道对象或资源的物理ID。
JNDI程序包：

- javax.naming：命名操作；
- javax.naming.directory：目录操作；
- javax.naming.event：在命名目录服务器中请求事件通知；
- javax.naming.ldap：提供LDAP支持；
- javax.naming.spi：允许动态插入不同实现。

利用JNDI的命名与服务功能来满足企业级API对命名与服务的访问，诸如EJB、JMS、JDBC 2.0以及IIOP上的RMI通过JNDI来使用CORBA的命名服务。

## 序列化

[什么是Java序列化，如何实现java序列化](https://blog.csdn.net/m0_58957310/article/details/120212165)

[知乎专栏 - java序列化，看这篇就够了](https://zhuanlan.zhihu.com/p/449460157)

序列化就是一种用来处理对象流的机制，所谓对象流也就是将对象的内容进行流化。可以对流化后的对象进行读写操作，也可将流化后的对象传输于网络之间。

当两个进程在进行远程通信时，彼此可以发送各种类型的数据。无论是何种类型的数据，都会以二进制序列的形式在网络上传送。发送方需要把这个Java对象转换为字节序列，才能在网络上传送；接收方则需要把字节序列再恢复为Java对象。

只能将支持 java.io.Serializable 接口的对象写入流中。每个 serializable 对象的类都被编码，编码内容包括类名和类签名、对象的字段值和数组值，以及从初始对象中引用的其他所有对象的闭包。

### 概念

序列化：把Java对象转换为字节序列的过程。
反序列化：把字节序列恢复为Java对象的过程。

### 用途

1 .把对象的字节序列永久地保存到硬盘上，通常存放在一个文件中；
2. 在网络上传送对象的字节序列。

> 我之前在国内某基础软件提供商工作（开发譬如一些服务器、框架等），接触多了，我发现国内很多人把java web的那块东西当成java ee了。以为学习了servlet/jsp/一堆框架/页面语言就等于是java ee，在我看来，java ee是个无比庞大的体系，我假想我提到的很多东西可能很多人都没接触过，或者只是了解到而已，譬如rmi-iiop，java idl，jta，jpa，jms，javamail，jndi，jpt，jaas，jaxws，jaxrpc，jaxb，ejb，jmx，jca。。。太多了，每一个规范都是几百页的文档，并且还会衍生出许多平台无关的规范例如ws stack中的ws-*，流程中的bpmn2，bpel，xpdl。。。相信我，我这里列出来的只是一角。所以我个人觉得，没有哪个人会精通去学整个javaee，而是要看你所在的领域。如果你想要了解更多javaee的东西，可以去看看oracle的fusion系列，ibm的webshpere系列，他们是领导者，当然你也可以看看国内厂商的，还有很多开源社区也可以考虑，他们的产品都是基于java ee，真正的java企业级应用，而不是一个简单的java web应用
