#本次学习为二次巩固基础知识点
#标准数据类型6种：Number（数字）、String（字符串）、
#List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）
#Number（数字），常规的加减乘除，取模，幂运算，取整，取余，还有关键字true和false
#String（字符串），字符串拼接，字符串重复，字符串切片，字符串查找，字符串替换，字符串大小写转换，字符串长度，字符串格式化

#字符串拼接，复制
# a='你好'
# b='世界！'
# print(a+b)
# print(a*2)

#字符串格式化
# print('name=%s,age=%s,sex=%s'%('张三',21,'男'))
# print('name=%s,age=%d,sex=%s'%('张三',21,'男'))
# n='张三'
# m=21
# s='女'
# print(f'name={n},age={m},sex={s}')

#转义字符
# print('let\'s go!')

#索引和切片
# str='0123456789'
# print(str[0:]) #第一个到末尾
# print(str[0:-1]) #第一个到倒数第二个
# print(str[2:]) #第三个到最后
# print(str[0::2]) #取偶数
# print(str[1::2]) #取奇数
# a=[]
# for i in range(1,101):
#     # print(i)
#     a.append(i)
# print(a[0::2]) #打印奇数
# print(a[1::2]) #打印偶数
#
# c=[]
# for j,k in zip(a[0::2],a[1::2]):
#     c.append(j)
#     c.append(k)
# print(c) #还原【1-100】

#判断字符是否存在
# str='horfjowerfoiwjiowjiow4fiojwe'
# a=input("请输入你要查找的字符串：")
# counts=0
# if a in str:
#     counts=str.count(a)
# #下面是三种方式打印某字符出现的次数
# print(f"{a}出现的次数为{counts}")
# print("{}出现的次数为{}".format(a,counts))
# print("%s出现的次数为%s"%(a,counts))

#字符串排序
# strings = ["banana", "apple", "cherry"]
# # 根据每个字符串的第二个字符排序,通过索引进行排序
# strings_sorted = sorted(strings, key=lambda x: x[0])
# print(strings_sorted)


#列表
# list1=[i for i in range(1,101)] #列表推导式
# # print(list1)
# ji=list1[0::2]
# # print(ji)
# ou=list1[1::2]
# # print(ou)
#
# ji_ou=[]
# #zip后面的顺序很重要！！！
# for j,k in zip(ou,ji):
#     ji_ou.append(j)
#     ji_ou.append(k)
# # print(ji_ou)
# sort=sorted(ji_ou)
# print(sort)
# #从大到小排序(反转)
# print(sort[::-1])
# #或者用reverse
# sort.reverse()
# print(sort)

# 函数的使用
#列表反转
def reverse_list(x):
    x=x[::-1]
    return x

list1=[i for i in range(1,101)]
c=reverse_list(list1)
def reverse_list(lst):
    # 初始化一个空列表，用于存储反转后的列表
    reversed_lst = []

    # 遍历原始列表的每个元素
    for item in lst:
        # 将当前元素添加到反转列表的末尾
        reversed_lst.insert(0, item)

    # 返回反转后的列表
    return reversed_lst

# 定义一个列表
list1 = [1, 2, 3, 4, 5]

# 打印反转后的列表
print(reverse_list(list1))
def sort_list(x):
    x=sorted(x)
    return x


x = print(sort_list(c))



