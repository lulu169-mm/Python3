### 1.Webshell概念

```
是一种通过web漏洞或后门获取web服务器控制权限的脚本程序
or
以asp、php、jsp或cgi等网页形式存在的一种命令执行环境，也叫网页后门
```

### 2. 绕过WAF方法

```
1. 绕过正则
2. 同义替换
3. 拆分参数
4. 更换数据源
```

### 3. 步骤

```
1. 入侵网站
2. 将asp或php等后门文件混入正常网页文件
3. 通过网页访问后门文件
4. 得到命令执行环境
5. 控制网站服务器
```

### 4. 相关函数

#### (1).php环境

```
1. eval()、assert()
2. preg_replace()
3. create_function()
4. array_map、array_filter()
5. call_user_func()、call_user_func_array()
```

#### (2).命令环境

```
1. system()、exec()、shell_exec()
2. popen()、passthru()
```

### 5. 变形

```
1. 字符替换法
	str_replace()
2. 编码替换法
	a. base64_decode()
	b. str_rot13()
3. 点字符操作
4. 更换数据源
5. 标签替换法
6. 字符串连接
7. 自定义
	a. 自定义函数
	b. 自定义类
	c. 魔术方法
		__construct()
		__destruct()
		__toString()
		__wakeup()
	d. 匿名函数
8. 异或运算


```

