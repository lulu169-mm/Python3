# Java安全

IDEA 

Maven 

Java Web 

反射

ASM/Javassist 

JNDI：8u191低版本和高版本怎么打(反序列化/本地工厂)，以及如何审计 

RMI是什么 

Java Agent：启动原理和RASP的实现原理 

JMX/JDWP 

反序列化基础：gadget链、JEP290是什么 

FastJson反序列化 

WebLogic：二次反序列化、XML Decoder、IIOP/T3 

Xstream反序列化 

Hessian反序列化：dubbo 

SnakeYAML反序列化 

Shiro：Shiro经典漏洞、Padding Oracle漏洞形成原理、如何通过Shiro注入内存马 

Struts2 

Spring：Spring4Shell、Spring EL、SpringBoot Actuator利用 

Tomcat：Tomcat AJP RCE 

内存马原理：原理是什么、有哪些内存马 

内存马如何查杀 

Log4J 

其他组件漏洞：Apache Solr、Flink 

进阶：tabby、codeql等静态分析 



## Maven



## 反射

**三种方式获取类的Class对象**



**通过类名获取**

```java
类名.class
```



**通过该类的实例化对象获取**

```java
对象.getClass()
```



**通过全类名获取**

```java
Class.forName("全类名")
```



```java
class Person{
}
public class Students extends Person {
    public static void main(String[] args) throws Exception {
        //1.直接通过类名称.class
       Class c1 = Students.class;
       //2.通过Students类的任意一个实例化对象，调用getClass 方法
       Class c2 = new Students().getClass();
       //通过Class的forName方法
       Class c3 = Class.forName("article2.Students");
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
    }
}
```

```java
//输出：
class article2.Students
class article2.Students
class article2.Students
```

