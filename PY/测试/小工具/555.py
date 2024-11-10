# 列表
list1 = [i for i in range(1, 10)]  # 列表推导式
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 添加元素
list1.append(44)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 44]
print(list1)

# 删除元素
list1.remove(9)
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 44]
del list1[3]
print(list1)  # [1, 2, 3, 6, 7, 8, 44]

# 列表切片
print(list1[1:5])  # [2, 3, 6, 7],左闭右开

# 列表相加
list2 = [i for i in range(10, 20)]
print(list1 + list2)  # [1, 2, 3, 6, 7, 8, 44, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 修改列表
list1[1] = 99
print(list1)  # [1, 99, 3, 6, 7, 8, 44]

# 遍历列表
for i in list1:
    print(i)

# 字典推导式
dict1 = {i: i * 100 for i in range(1, 10)}
print(dict1)

# 访问字典
print(dict1[3])  # 300

# 删除
del dict1[4]
print(dict1)

# 添加
dict1[11] = 400
print(dict1)

# 修改
dict1[11] = 500
print(dict1)

# 遍历字典
for key in dict1:
    print(key, dict1[key])

# 元组推导式
tuple1 = tuple(i for i in range(90, 100))
print(tuple1)

# 遍历元组
for i in tuple1:
    print(i)

# 删除元组
# del tuple1

# 集合推导式
set1 = {i for i in range(200, 211)}
print(set1)

# 添加元素
set1.add(222)
print(set1)

# 删除元素
set1.remove(200)
print(set1)


def remove_set():
    set1.remove(201)
    set1.add(202)
    set1.add(211)
    print(set1)


if __name__ == '__main__':
    remove_set()
    set1.add(999)
    print(set1)


# import re

# print(re.search(r'[^a].*', 'aaahello world'))
# print(re.findall(r'[^a].*', 'aaahello world'))


