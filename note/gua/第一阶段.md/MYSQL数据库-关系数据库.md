# MYSQL数据库-关系数据库

## 概念

​按数据结构来组织、存储和管理的仓库

由于体积小、速度快、总​体拥有成本低，尤其是开放源码，广泛运用于中小型网站中

优点：

* 按一定的数据模型组织、描述和存储
* 可为各种用户共享
* 冗余度较小、节省存储空间
* 易扩展，编写有关数据库的应用程序

## [类型](https://www.runoob.com/mysql/mysql-data-types.html)

### 数值型

* 整型int  
  十进制和十六进制（x不能大写）
* 浮点型float

### 字符串

* 单引号或双引号
* 要使用转义字符才能表示特殊字符  
  ​![image-20240807095426747](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807095426747.png?lastModify=1729598356)​

### 数据类型

* 日期和时间值：时间按年月日顺序
* NULL值：一种无类型的值，表示“空”
* **数值列类型**  
  ​![image-20240807095652651](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807095652651.png?lastModify=1729598356)​
* **字符串列类型**  
  ​![image-20240807100247092](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807100247092.png?lastModify=1729598356)​

  * char类型和varchar类型长度范围都是0~255，char固定长度的非Unicode字符数据，varchar可变长度非Unicode数据
  * 对于可变长的字符串类型，其长度取决于实际存放在列中的值的长度
  * BLOB是二进制对象，若要存储二进制数BLOB是最好的，可用来存储图像  
    ​![image-20240807102627367](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807102627367.png?lastModify=1729598356)​

## 登录命令

**mysql -h host_name -u user_name -p password**

```
-h 主机名、IP地址

-u 用户名

-p 密码
```

​![image-20240807094356821](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807094356821.png?lastModify=1729598356)​

## 常用命令

```
\c               //放弃正在输入的命令
\h               //显示命令清单
\q               //退出程序 
\s               //查看mysql服务器状态信息
```

```
show databases;  //显示所有数据库
use dbname;      //选定默认数据库
show tables;     //显示默认数据库中所有表

CREATE DATABASE 数据库名;  //创建数据库
desc 表名;        //查看表的创建结构


```

```
CREATE TABLE 表名(
列名 列类型 [<列的完整约束性>]，
列名 列类型 [<列的完整约束性>]，
。。。
);               //建表
```

​![image-20240807103001443](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807103001443.png?lastModify=1729598356)​

```
drop table 表名    //删除表
```

​![image-20240807104727364](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807104727364.png?lastModify=1729598356)​

```
drop table database 数据库名  //删除数据库
//删除是永久性的，如果出现if exists子句 ，则删除不存在的数据库不会出错 
```

```
alter table 表名 action      //更改表结构操作
```

​![image-20240807105031241](file:///C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20240807105031241.png?lastModify=1729598356)​

### 

‍

### 总结

```bash
mysql -h localhost -uroot -proot   //登录数据库
create database you; //创建数据库
show databases; //查看mysql中存在的所有数据库
use yxzc;   //指定某个数据库
create table person(id int, name char(8), age int);  //创建数据表
show tables;  //查看表
show columns from person; //查看表中字段
insert [into] 表名[(列名1, 列名2, 列名3, ...)] values (值1, 值2, 值3, ...);  //插入数据
insert into person values(99,‘stem', 100)  
向dashuaibi数据表中写入数据，dashuaibi数据表一共创建了三个列，id列、name列、age列，99对应id、you对应name、
100对应age。
select * from person;   //查看所写的数据
select id,name from person;   //只查询某几列
update person set name='xiaoming' where id=99; //修改写入的数据
delete from person where id=99 and/or age=100;  //删除写入的数据
drop table person;   //删除数据表
```

‍

‍
