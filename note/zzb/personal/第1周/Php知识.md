## 一. 基本语法

### 1.变量

#### (1).可变变量

```php
$shu = "biao";
$biao = "鼠标";
echo $$shu;
```

#### (2).外部变量

```php
//对于一个表格
<html>
  <head>
  </head>
  <body>
<!-- 这一行method 对应的值改为post --->
<form action="req.php" method="post">
<input type="text" name="username"/>
<input type="password" name="pwd"/>
<input type="submit" name="提交"/>
</form>
  </body>
</html>
```

在php代码中调用上述变量

```php
<?php
$u = $_POST['username'];
echo $u.'<br />';
$passwd = $_POST['pwd'];
echo $passwd.'<br />';
?>
```

#### (3).环境变量

### 2.常量

定义方式：define(常量名，常量值)

```php
<?php
define('MY_NAME','PHP中文网');
echo MY_NAME;
//下面是错误的调用方式
echo '我的名字是MY_NAME';
//下面是正确的调用方式
echo '我的名字是'.MY_NAME;
?>
```

### 3.注释

#### (1).单行注释

```php
//表示单行注释
#表示单行注释
```

#### (2).多行注释

```php
/*
作者：PHP中文网
时间：2020.01.01
功能：这是一个多行注释例子
*/
```

### 4.数据类型

| 数据类型             | 含义                     |
| -------------------- | ------------------------ |
| boolean(布尔型)      | 值只有 真or假            |
| string(字符串型)     | 连续的字符               |
| integer(整型)        | 只能包含整数             |
| float/double(浮点型) | 存储含小数位数的数字     |
| array(数组型)        | 一组相同类型的集合       |
| object(对象类)       | 一个对象，用new创建      |
| **resource(资源型)** | 保存在外部资源的一个应用 |
| null(空白)           | 表示值为空               |

