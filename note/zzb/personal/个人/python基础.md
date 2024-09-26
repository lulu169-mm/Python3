### 1. 对象方法

####  1.字符串对象

#####   1. count

```python
# 调用字符串的count 方法，这里返回2，
# 表示该字符串包含了两个 '我们'
'我们今天不去上学，我们去踢足球'.count('我们')
```

#####   2. find

###### 	1. 从头查找

```python
str1 = '我们今天不去上学，我们去踢足球'

# 返回 0 ， str1字符串中有两个 '我们'
# find返回的是第一个 '我们' 的索引 0
pos1 = str1.find('我们')  
```

###### 	2. 指定查找

```python
str1 = '我们今天不去上学，我们去踢足球'

# 第2个参数 5， 表示从 索引 5 的位置开始往后查找
# 返回的是后面 我们 的索引  9
pos1 = str1.find('我们',5)  
```

##### 3. split、splitlines

###### 	1. split

* 字符串中 **截取**

```python
str1 = '小张：79 | 小李：88 | 小赵：83'
print(str1)
pos1 = str1.split('|')
print(pos1)

#分别返回 
#小张：79 | 小李：88 | 小赵：83
#['小张：79 ', ' 小李：88 ', ' 小赵：83']
```

###### 	2. splitlines

* 把字符串**按换行符**进行切割

```python
salary = '''
小王  10000元
小李  20000元
小徐  15000元
'''
print(salary.splitlines())
#输出结果如下
#['', '小王  10000元', '小李  20000元', '小徐  15000元']
```

#####   4. join

* 将列表中的字符串元素**连接**为一个字符串

```python
'|'.join([
    '小张：79 ',
    ' 小李：88 ',
    ' 小赵：83'
])
#返回的是字符串 
#小张：79 | 小李：88 | 小赵：83 
```



#####   5. strip、lstrip、rstrip

###### 	  1. strip

* 去除字符串前后的空格

###### 	  2. lstrip

* 去除字符串左边的空格

###### 	  3. rstrip

* 去除字符串右边的空格

#####   6. replace

- **替换**字符串里面**所有**指定的 子字符串

```python
str1 = '我们今天不去上学，我们去踢足球'
str1 = str1.replace('我们', '他们') 

#输出结果如下
#'他们今天不去上学，他们踢足球'
```

#####   7. startwith、endwith

###### 	  1. startwith

* 检查字符串是否以参数指定的字符串 **开头**

```python
str1 = '我们今天不去上学，我们去踢足球'
str1.startswith('我们')  # 返回 True
```



###### 	  2. endwith

* 检查字符串是否以指定的字符串 **结尾**

```python
str1 = '我们今天不去上学，我们去踢足球'
str1.endswith('我们')    # 返回 False
```

#####   8. isdigit

* 检查字符串是否全部由数字构成

```python
str1 = input('请输入手机号码:')
if not str1.isdigit(): # 不是全部由数字字符构成
    print('您输入的手机号码不正确，必须全部是数字')
```

#####   9. 字符串的倒序

* 要得到一个字符串的 倒序字符串，只需要使用切片操作 [::-1]

```python
#:: 表示切片字符串的从头到尾，也就是全部内容， 而 步长 为 -1 表示，颠倒过来取元素

str1 = '字符串的倒序'
reverse = str1[::-1]
print(reverse)   #结果为 “序倒的串符字”
```

####   2. 列表对象

##### 	1. append

* 改变列表的内容，在**后面**添加一个元素

```python
a = [1, 2, 3.14, 'hello']  

# append 之后，a就变成了 [1, 2, 3.14, 'hello', '你好']
a.append('你好')
print(a)

# 继续append ，a就变成了 [1, 2, 3.14, 'hello', '你好', [7,8]]
a.append([7,8])
print(a)

print(a.append(3))  #结果为 None
```

* append 方法的**返回值是 None**，而不是新的列表对象。

##### 	2. insert

* 在 **指定位置插入**一个元素

```python
a = [1, 2, 3.14, 'byhy.net']  

# 插入到索引0的位置，也是插到第1个元素的位置上
# a列表内容就变成了 ['你好', 1, 2, 3.14, 'byhy.net']
a.insert(0, '你好')
print(a)

# 插入到索引2的位置，也是插到第3个元素的位置上
# a列表内容就变成了 ['你好', 1, 'Laffrex',  2, 3.14, 'byhy.net']
b = a.insert(2, 'Laffrex')
print(a)

print(b)  #结果为 None
```

* insert方法的返回值也是 None

##### 3. pop

* 从列表 **取出并删除** 一个元素

```python
a = [1, 2, 3.14, 'byhy.net']  

# 取出索引为3 的元素，也就是第4个元素
poped = a.pop(3)

# 取出后，a列表对象内容就变成了 [ 1, 2, 3.14]
print(a)

# 而取出的元素赋值给变量poped， poped的内容就是 'byhy.net'  
print(poped)

```

##### 	4. remove

* 删除指定列表元素第一次出现的值

```python
var1 = ['a','b','c','a']
b = var1.remove('a')
print(var1)    # ['b', 'c', 'a']
print(b)    # None
```

* remove 方法的返回值也是 None

##### 	5.  reverse

* 将列表元素倒过来

```python
var1 = [1,2,3,4,5,6,7]
b = var1.reverse()
print(var1)		# [7, 6, 5, 4, 3, 2, 1]
print(b)		# None
```

* reverse 方法的返回值也是 None

##### 	6. index

* 返回 参数对象的索引

```python
var1 = [1,2,3,4,5,6,7]
print(len(var1))	# 长度为7
idx = var1.index(5)
print(idx)			# 索引为4
```

##### 	7. sort

* 对列表进行排序

```python
students = ['Alex','Tom','Jerry','Michale','Alex']
students.sort()
print(f'after sort: {students}')

numbers = [7,3,8,2,9]
numbers.sort()
print(f'after sort: {numbers}')

#输出结果如下
#after sort: ['Alex', 'Alex', 'Jerry', 'Michale', 'Tom']
#after sort: [2, 3, 7, 8, 9]

number2 = numbers.sort()
print(number2)  	# None
```

* sort方法的返回值是None



###  2. 格式化字符串

####   1. printf风格

* 同C语言printf函数一样用法

1. 多个值

   ```python
   salary = input('请输入薪资：')
   # 计算出缴税额，存入变量tax
   tax = int(salary) *25/100  
   # 计算出税后工资，存入变量aftertax
   aftertax = int(salary) *75/100 
   print('税前薪资：%s元，缴税：%s元，税后薪资：%s元' %(salary,tax,aftertax))
   ```

2. 一个值

   ```python
   '税前薪资：%s 元' % (salary,)
   # or 
   '税前薪资：%s 元' % salary
   ```

3. 指定宽度和对齐

```python
'税前薪资：%10s 元' % 100000
'税前薪资：%10s 元' % 10000
'税前薪资：%10s 元' % 1000
```

| 占位符  | 含义                                         |
| ------- | -------------------------------------------- |
| %s      | 格式化对象为字符串                           |
| %10s    | 右对齐，总位数10位，不足用空格补齐           |
| %-10s   | 左对齐，总位数10位，不足用空格补齐           |
| %d      | 格式化对象为整数                             |
| %010d   | 右对齐，总位数10位，不足用0补齐              |
| %f      | 格式化对象为小数                             |
| %010.2f | 右对齐，总位数10位，保留2位小数，不足用0补齐 |

####   2. f-string格式化

##### 	1. 含义

* f-string 格式化 就是在字符串模板前面加上f，然后占位符使用{} ,里面直接放入对应的数据对象

```python
salary = input('请输入薪资：')

# 计算出缴税额，存入变量tax
tax = int(salary) *25/100  

# 计算出税后工资，存入变量aftertax
aftertax = int(salary) *75/100 

print(f'税前薪资是：{salary}元， 缴税：{tax}元， 税后薪资是：{aftertax}元')
```

##### 	2. 指定宽度

* 在括号里面的变量后面加上 `:宽度值`

```python
# 员工 1
salary = 8000
tax = int(salary) *25/100  
aftertax = int(salary) *75/100 
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')


# 员工 2
salary = 15000
tax = int(salary) *25/100  
aftertax = int(salary) *75/100 
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')


# 员工 3
salary = 100000
tax = int(salary) *25/100  
aftertax = int(salary) *75/100 
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')

#税前薪资是：    8000元， 缴税：  2000.0元， 税后薪资是：  6000.0元
#税前薪资是：   15000元， 缴税：  3750.0元， 税后薪资是： 11250.0元
#税前薪资是：  100000元， 缴税： 25000.0元， 税后薪资是： 75000.0元
```

##### 	2. 左右对齐

* 在括号里使用 `<` `>` 符号，< 就是左对齐，> 就是右对齐

```python
def calcTax(salary):
    tax = int(salary) *25/100  
    aftertax = int(salary) *75/100 
    print(f'税前薪资是：{salary:<8}元， 缴税：{tax:<8}元， 税后薪资是：{aftertax:<8}元')
    
calcTax(8320)
calcTax(15023)
calcTax(100030)

#税前薪资是：8320    元， 缴税：2080.0  元， 税后薪资是：6240.0  元
#税前薪资是：15023   元， 缴税：3755.75 元， 税后薪资是：11267.25元
#税前薪资是：100030  元， 缴税：25007.5 元， 税后薪资是：75022.5 元
```

##### 	3. 小数点后位数

* `.2f`就表示小数点后面保留2位

```python
def calcTax(salary):
    tax = int(salary) *25/100  
    aftertax = int(salary) *75/100 
    print(f'税前薪资是：{salary:8.1f}元， 缴税：{tax:8.1f}元， 税后薪资是：{aftertax:8.1f}元')

calcTax(8320)
calcTax(15023)
calcTax(100030)

#税前薪资是：  8320.0元， 缴税：  2080.0元， 税后薪资是：  6240.0元
#税前薪资是： 15023.0元， 缴税：  3755.8元， 税后薪资是： 11267.2元
#税前薪资是：100030.0元， 缴税： 25007.5元， 税后薪资是： 75022.5元
```

##### 	4. 不足补零

###### 	  1. 数字

* 在确定的位数前加0

```python
def calcTax(salary):
    tax = int(salary) *25/100  
    aftertax = int(salary) *75/100 
    print(f'税前薪资是：{salary:08}元， 缴税：{tax:08.1f}元， 税后薪资是：{aftertax:08.1f}元')


calcTax(8320)
calcTax(15023)
calcTax(100030)

#税前薪资是：00008320元， 缴税：002080.0元， 税后薪资是：006240.0元
#税前薪资是：00015023元， 缴税：003755.8元， 税后薪资是：011267.2元
#税前薪资是：00100030元， 缴税：025007.5元， 税后薪资是：075022.5元
```

###### 	  2. 字符串

* 使用符号 `<` 或者 `>` 同时指定左右对齐方式

```python
var = '34324'
f'{var:<08}'	# '34324000'
f'{var:>08}'	# '00034324'
```

##### 	5. 16进制

```python
# 用 x 表示格式化为16进制，并采用小写格式
f'数字65535的16进制表示为：{65535:x}'  

# 用 X 表示格式化为16进制，并采用大写格式
f'数字65535的16进制表示为：{65535:X}'
```

##### 	6. 字符串有花括号

* 要 双写进行转义，否则会被当成是格式化占位符

```python
times1 = 1000
times2 = 2000

print(f'文章中 {{ 符号 出现了 {times1} 次')
print(f'文章中 }} 符号 出现了 {times2} 次')
```

###  3. 循环

####   1. range

```python
range(101)		#n值从0到100，循环100次
range(50,101)	#n值从50到100，步长为1
range(50,101,5)	#n值从50到100，步长为5
```

####   2. enumerate函数

* 除了获取每个元素，还能得到每个元素的索引

```python
#打印年龄大于17岁的成员的索引

studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
# enumerate (studentAges) 每次迭代返回 一个元组
# 里面有两个元素，依次是 元素的索引和元素本身 
for idx, student in enumerate(studentAges):
    if int(student.split(':')[-1]) > 17:
        print(idx)
```

####   3. break

* 跳出当前循环

##### 	1. 对while

```python
while True:
    command = input("请输入命令:")
    if command == 'exit':
        break
    print(f'输入的命令是{command}')

print('程序结束')
```

##### 	2. 对for

```python
for i in range(100):
    command = input("请输入命令:")
    if command == 'exit':
        break
    print(f'输入的命令是{command}')

print('程序结束')
```

####   4. continue

* **只结束当前这一轮循环**

```python
while True:
    command = input("请输入命令:")
    if command == 'exit':
        break
    if command == 'cont':
        continue
    print(f'输入的命令是{command}')
    
print('程序结束')
```

####   5. 列表推导式

* 把一个列表里面的每个元素， **经过相同的处理**，生成另一个列表

```python
#传统写法：
list1 = [1,2,3,4,5,6]
list2 = []
for num in list1:
    list2.append(num*num)
    
#列表推导式：
list1 = [1,2,3,4,5,6]
list2 = [num**2 for num in list1]
```

###  4. 文件读写

####   1. 文本模式

##### 	1. open函数

###### 	  1. 总参数

```python
open(
    file, 
    mode='r', 
    buffering=-1, 
    encoding=None, 
    errors=None, 
    newline=None, 
    closefd=True, 
    opener=None
    ) 
```

###### 	  2. 常用参数

1. file

   * 指定文件打开的路径

   * 使用**相对路径**或**绝对路径**

2. mode

   * 指定文件打开的模式

   * | 参数  | 含义                         |
     | ----- | ---------------------------- |
     | **r** | **只读模式，文件必须存在**   |
     | **w** | **只写模式**                 |
     | **a** | **追加模式**                 |
     | rb    | 二进制只读模式，文件必须存在 |
     | wb    | 二进制只写模式               |
     | ab    | 二进制追加模式               |
     | r+    | 读写模式，文件必须存在       |
     | rb+   | 二进制读写模式，文件必须存在 |
     | w+    | 读写模式                     |
     | wb+   | 二进制读写模式               |
     | a+    | 追加模式                     |
     | ab+   | 二进制追加模式               |

3. encoding

   * 指定读写文件时使用的**字符编解码**方式

   * ```python
     后面调用write写入字符串到文件中，open函数会使用指定encoding编码为字节串；
     
     后面调用read从文件中读取内容，open函数会使用指定encoding解码为字符串对象
     
     如果调用的时候没有传入encoding参数值，open函数会使用系统缺省字符编码方式。 比如在中文的Windows系统上，就是使用cp936（就是gbk编码）。
     ```

##### 	2. 写文件

```python
# 指定编码方式为 utf8
f = open('tmp.txt','w',encoding='utf8')

# write方法会将字符串编码为utf8字节串写入文件
f.write('白月黑羽：祝大家好运气')

# 文件操作完毕后， 使用close 方法关闭该文件对象
f.close()
```

##### 	3. 读文件

```python
# 指定编码方式为 gbk，gbk编码兼容gb2312
f = open('tmp.txt','r',encoding='gbk')

# read 方法会在读取文件中的原始字节串后， 根据上面指定的gbk解码为字符串对象返回
content = f.read()

# 文件操作完毕后， 使用close 方法关闭该文件对象
f.close()

# 通过字符串的split方法获取其中用户名部分
name = content.split('：')[0]

print(name)
```

##### 	4. 注意点

###### 	  1. read函数

* 有参数size，用来指定读取多少个字符

* ```python
  # 因为是读取文本文件的模式， 可以无须指定 mode参数
  # 因为都是 英文字符，基本上所以的编码方式都兼容ASCII，可以无须指定encoding参数
  f = open('tmp.txt')
  
  tmp = f.read(3)  # read 方法读取3个字符
  print(tmp)       # 返回3个字符的字符串 'hel' 
  
  tmp = f.read(3)  # 继续使用 read 方法读取3个字符
  print(tmp)       # 返回3个字符的字符串 'lo\n'  换行符也是一个字符
  
  tmp = f.read()  # 不加参数，读取剩余的所有字符
  print(tmp)       # 返回剩余字符的字符串 'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==' 
  
  # 文件操作完毕后， 使用close 方法关闭该文件对象
  f.close()  
  ```

###### 	  2. readlines方法

* 返回一个列表

* ```python
  #这种方法,列表的每个元素对应的字符串 最后有一个换行符。
  f = open('tmp.txt')
  linelist = f.readlines() 
  f.close()  
  for line in linelist:
      print(line)
      
  #不想要换行符，可以使用字符串对象的splitlines方法
  f = open('tmp.txt')
  content = f.read()   # 读取全部文件内容
  f.close()  
  # 将文件内容字符串按换行符切割到列表中，每个元素依次对应一行
  linelist = content.splitlines()
  for line in linelist:
      print(line)
  ```

####   2. 字节(二进制)模式

* 字节实现一个简单的文件拷贝功能

```python
def fileCopy(srcPath,destPath):
    srcF = open(srcPath,'rb')
    content = srcF.read()
    srcF.close()

    destF = open(destPath,'wb')
    destF.write(content)
    destF.close()

fileCopy('1.png','1copy.png')
```



####   3. with语句

* with 语句 打开文件，不需要手动调用close方法关闭。 

```python
# open返回的对象 赋值为 变量 f
with open('tmp.txt') as f:
    linelist = f.readlines() 
    for line in linelist:
        print(line)
```

####   4. 写入缓冲

* 如果有sleep()等延时操作，文件不会被立即写入存储空间，而是先被写入内存缓冲区，等待对象关闭或缓冲区溢出才存入存储空间

```python
f = open('tmp.txt','w',encoding='utf8')

f.write('白月黑羽：祝大家好运气')
f.flush()	# 立即把内容写到文件里面

# 等待 30秒，再close文件
import time
time.sleep(30)

f.close()
```

###  5. 文件和目录操作

####   1. 创建目录

```python
import os
os.makedirs('tmp/python/fileop',exist_ok=True)

#会在当前工作目录下面创建 tmp目录，在tmp目录下面再创建 python目录，在Python目录下面再创建fileop目录,exist_ok=True 指定了，如果某个要创建的目录已经存在，也不报错
```

####   2. 删除文件或目录

##### 	1. 文件

```python
import os
os.remove('sdf.py')
```

##### 	2. 目录

```python
import shutil
shutil.rmtree('tmp', ignore_errors=True)
#参数 ignore_errors 值设置为 True ，表示忽略删除过程中的错误，不会抛出异常。
```

####   3. 拷贝文件

```python
from shutil import copyfile

# 拷贝 d:/tools/first.py 到 e:/first.py
#如果拷贝前，e:/first.py 已经存在，则会被拷贝覆盖
copyfile('d:/tools/first.py', 'e:/first.py')
```

####   4. 拷贝目录

```python
from shutil import copytree

# 拷贝 d:/tools/aaa 目录中所有的内容 到 e:/bbb 中
#拷贝前， 目标目录必须 不存在 ，否则会报错
copytree('d:/tools/aaa', 'e:/new/bbb')
```

####   5. 修改文件、目录名

```python
import os

# 修改目录名 d:/tools/aaa 为 d:/tools/bbb
os.rename('d:/tools/aaa','d:/tools/bbb')

# 修改文件名 d:/tools/first.py 为 d:/tools/second.py
os.rename('d:/tools/first.py','d:/tools/second.py')
```

####   6. 判断存在

```python
1. 判断指定路径的文件或目录是否存在：
import os
os.path.exists('d:/systems/cmd.exe')
os.path.exists('d:/systems')
#exists方法返回值为True表示 存在，否则表示不存在。

2.判断指定路径是否是文件：
import os
os.path.isfile('d:/systems/cmd.exe')	#返回值为True 表示是文件

3.判断指定路径是否是目录：
import os
os.path.isdir('d:/systems')	#返回值为True 表示是目录
```

####   7. 当前工作目录

```python
1.确认当前工作目录:
import os
cwd = os.getcwd()

2.改变当前工作目录到另外的路径:
import os
os.chdir(path)
#参数就是 新的当前工作目录 路径地址。
```

####   8. 递归遍历目录所有文件

```python
1.得到某个目录下的所有子目录和所有文件
import os
targetDir = r'd:\tmp\util\dist\check'	# 目标目录
files = []
dirs  = []
# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
    dirs += dirnames
print(files)
print(dirs)

2.得到某个目录下所有文件的全路径
import os
targetDir = r'd:\tmp\util\dist\check'	# 目标目录
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        # 把 dirpath 和 每个文件名拼接起来 就是全路径
        fpath = os.path.join(dirpath, fn)
```

####   9. 得到目录所有文件、子目录名

```python
1获取文件及子目录：
import os
targetDir = r'd:\tmp\util\dist\check'	# 目标目录
files =  os.listdir(targetDir)
print(files)

2.只获取目录中所有的文件，或者子目录:
import os
from os.path import isfile, join,isdir
targetDir = r'd:\tmp\util\dist\check'	#目标目录
print([f for f in os.listdir(targetDir) if isfile(join(targetDir, f))])	#所有的文件
print([f for f in os.listdir(targetDir) if isdir(join(targetDir, f))])  #所有的目录
```

####   10. 得到目录指定扩展名的文件、子目录

```python
import glob
exes = glob.glob(r'd:\tmp\*.txt')
print(exes)
```

###  6. 多线程和多进程

####   1. 创建线程

* python3 将 系统调用**创建线程** 的功能封装在 **标准库 threading** 中

```python
print('主线程执行代码') 
# 从 threading 库中导入Thread类
from threading import Thread
from time import sleep

# 定义一个函数，作为新线程执行的入口函数
def threadFunc(arg1,arg2):
    print('子线程 开始')
    print(f'线程函数参数是：{arg1}, {arg2}')
    sleep(5)
    print('子线程 结束')

thread = Thread(	# 创建 Thread 类的实例对象
    # target 参数 指定 新线程要执行的函数
    # 注意，指定函数对象后面不能加括号，加括号是在当前线程调用执行
    target=threadFunc, 
    args=('参数1', '参数2')	#新线程函数的参数是元组，在 args里面填入参数
)

# 执行start 方法，就会创建新线程并执行入口函数，
# 这时候 这个进程 有两个线程了。
thread.start()

# 主线程的代码执行 子线程对象的join方法，
# 就会等待子线程结束，才继续执行下面的代码
thread.join()
print('主线程结束')
```

####   2. 共享数据(锁)

* 避免数据的访问**互相冲突**影响

```python
from threading import Thread,Lock
from time import sleep

bank = {
    'money' : 0
}

bankLock = Lock()

# 定义一个函数，作为新线程执行的入口函数
def deposit(theadidx,amount):
    bankLock.acquire()	# 操作共享数据前，申请获取锁
    balance =  bank['money']
    sleep(0.1)		    # 执行一些任务，耗费了0.1秒
    bank['money']  = balance + amount
    print(f'子线程 {theadidx} 结束')
    bankLock.release()	    # 操作完共享数据后，申请释放锁

theadlist = []
for idx in range(10):
    thread = Thread(
        target = deposit,
        args = (idx,1)
    )
    thread.start()
    theadlist.append(thread)	    # 把线程对象都存储到 threadlist中

for thread in theadlist:
    thread.join()
print('主线程结束')
print(f'最后我们的账号余额为 {bank["money"]}')
```

####   3. daemon线程

* daemon线程也被称为用户线程，不能独立存在，必须依附于主线程(非Daemon线程)
* 非Deamon线程存在，程序不会结束
* python的thread生成的线程**默认为非Deamon线程**
* 可以使用**daemon = true** 属性来设置为deamon线程

```python
thread = Thread(target=threadFunc,
                daemon=True # 设置新线程为daemon线程
                )
```

####   4. 多进程

* 如果需要利用电脑**多个CPU核心的运算能力**，可以使用Python的**多进程库**

##### 	1. 使用多进程库

* 多进程库multiprocessing的**Process方法**

```python
from multiprocessing import Process

def f():
    while True:
        b = 53*53
        
if __name__ == '__main__':
    plist = []
    for i in range(2):
        p = Process(target=f)
        p.start()
        plist.append(p)
    for p in plist:
        p.join()
```

##### 	2. 主进程获取子进程

* 使用多进程库 multiprocessing 里面的 **Manage 对象**

```python
from multiprocessing import Process,Manager
from time import sleep

def f(taskno,return_dict):
    sleep(2)
    return_dict[taskno] = taskno	    # 存放计算结果到共享对象中

if __name__ == '__main__':
    manager = Manager()
    return_dict = manager.dict()	    # 创建 类似字典的 跨进程 共享对象
    plist = []
    for i in range(10):
        p = Process(target=f, args=(i,return_dict))
        p.start()
        plist.append(p)

    for p in plist:
        p.join()
    print('get result...')
    for k,v in return_dict.items():		   #从共享对象中取出其他进程的计算结果
        print (k,v)
```

###  7. 正则表达式

####   1. 常见语法

```python
import re
pattern = re.compile("匹配规则")
```

##### 	1. 点号.

* 匹配除了**换行符之外**的任何**单个**字符

###### 	  1. 一次性使用

```python
content = '''苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的'''

import re
for one in  re.findall('.色', content):
    print(one)
```

###### 	  2， 多次使用

* re.compile` 函数返回的是 `正则表达式对象，它对应的匹配规则在参数中进行定义

```python
import re
p = re.compile('.色')
for one in  p.findall(content):
    print(one)
```

##### 	2.星号*

* "*"  表示匹配前面的子表达式**任意次**，包括0次
* ".*" 表示重复匹配任意数量的任意字符（除了换行符），包括零个字符
* "." 表示**重复**匹配行为

```python
content = '''苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，'''

import re
p = re.compile(r'，.*')		
#，：匹配中文逗号;
#r : 表示是原始字符串，该原始字符串中的反斜杠"\"不会被解释为转义字符
for one in  p.findall(content):
    print(one)
```

##### 	3. 加号+

* 表示匹配前面的子表达式**一次或多次**，不包括0次

##### 	4. 问号？

* 匹配前面的子表达式**0次或1次**

##### 	5. 花括号{}

* 表示匹配前面的字表达式**指定的次数**

```python
content = '''
	红彤彤，绿油油，黑乎乎，绿油油油油
'''
p = re.compile(r'油{3}')		#匹配连续的油3次
p = re.compile(r'油{3，4}')	#匹配连续的油至少3次，至多4次
```

#####  	6. 方括号[]

* 表示要匹配指定的几个字符之一 

* **元字符** 在方括号内和**普通字符一样，“^”除外**

* ```python
  [abc] 可以匹配a,b,或者c里面的任意一个字符。等价于[a-c]
  [a-c] 中间的 - 表示一个范围从a 到 c
  ```

```python
content = 'a1b2c3d4e5'

import re
p = re.compile(r'[^\d]' )
for one in  p.findall(content):
    print(one)
```

##### 	7. ^、&

###### 	  1. 开头位置^

* 表示匹配文本的开头位置

###### 	  2. 结尾位置&

* 表示匹配文本的结尾位置

##### 	8. 单行、多行模式

* 默认为单行模式
* 多行模式使用compile函数的re.MULTILINE参数进行切换

```python
#提取所有的水果价格
content = '''001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''

import re
p = re.compile(r'\d+$', re.MULTILINE)
for one in  p.findall(content):
    print(one)
```

##### 	8. 竖线 | 

* 表示匹配其中之一

```python
content = '''苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
'''

import re
p = re.compile(r'绿|橙|黄')
for one in  p.findall(content):
    print(one)
```

##### 	9. 括号()

* 括号称之为 正则表达式的 组选择。
* 就是把 正则表达式 匹配的内容 里面 **其中的某些部分** 标记为某个组

```python
#提取水果的名字
content = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的'''

import re
p = re.compile(r'^(.*)，', re.MULTILINE)
for one in  p.findall(content):
    print(one)
```

* 可以在一个正则表达式中使用多个分组

```python
#从下面的文本中，提取出每个人的 名字 和对应的 手机号
content = '''张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901'''

import re
p = re.compile(r'^(.+)，.+(\d{11})', re.MULTILINE)
for one in  p.findall(content):
    print(one)
```

##### 	10. 让点匹配换行

* 使用参数DOTALL

```python
#找出下面文字中所有的职位名称
content = '''
<div class="el">
        <p class="t1">           
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
        </p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
'''

import re
p = re.compile(r'class=\"t1\">.*?<a>(.*?)</a>', re.DOTALL)
for one in  p.findall(content):
    print(one)
```



####  2. 贪婪与非贪婪模式

##### 	1. 贪婪模式

* 默认模式，它会尽可能多地匹配字符，直到达到整个正则表达式可以匹配的最大范围

* | 常见量词 | 功能                   |
  | -------- | ---------------------- |
  | *        | 匹配零个或多个字符     |
  | +        | 匹配一个或多个字符     |
  | {m,n}    | 匹配 `m` 到 `n` 个字符 |

```python
import re

text = "abc123def456ghi"
pattern = r'\d+'	#匹配所有连续的数字，但由于 + 是贪婪的，它会尽可能多地匹配所有数字
match = re.search(pattern, text)
print(match.group())  # 输出: '123456'

```

##### 	2. 非贪婪模式

* 会尽可能少地匹配字符，只到足够的字符能够使整个正则表达式匹配成功为止

* 要使正则表达式进入非贪婪模式，可以在量词后面添加一个问号 `?`

* | 常见量词 | 功能                               |
  | -------- | ---------------------------------- |
  | *?       | 匹配零个或多个字符（尽可能少)      |
  | +?       | 匹配一个或多个字符（尽可能少）     |
  | {m,n}?   | 匹配 `m` 到 `n` 个字符（尽可能少） |

```python
import re

text = "abc123def456ghi"
pattern = r'\d+?'
matches = re.findall(pattern, text)
print(matches)  # 输出: ['123', '456']

```

####   3. 元字符转义

* 要搜索的内容本身就包含元字符，就可以使用 反斜杠进行转义

```python
content = '''苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的'''

import re
p = re.compile(r'.*\.')		#匹配以"."结尾的所有字符串
for one in  p.findall(content):
    print(one)
```

####   4. 匹配类型

| 字符 | 功能                                                         |
| ---- | ------------------------------------------------------------ |
| \d   | 匹配0-9之间任意一个数字字符,等价于表达式[0-9]                |
| \D   | 匹配任意一个非0-9数字的字符，等价于[.^0-9]                   |
| \s   | 匹配任意一个空白字符，包括 空格、tab、换行符等，等价于表达式 [\t\n\r\f\v] |
| \S   | 匹配任意一个非空白字符，等价于表达式 [.^ \t\n\r\f\v]         |
| \w   | 匹配任意一个文字字符，包括大小写字母、数字、下划线，等价于表达式 [a-zA-Z0-9_] |
| \W   | 匹配任意一个非文字字符，等价于表达式[.^a-zA-Z0-9_]           |

* 反斜杠也可以用在方括号里面，比如 [\s,.] 表示匹配 ： 任何空白字符， 或者逗号，或者点
