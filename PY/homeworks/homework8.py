import pandas as pd
import numpy as np

# 读取Excel文件
fdata = pd.read_excel('')

# 显示数据的前几行
print("数据前五行：")
print(fdata.head())

# 查看数据形状
print("\n数据形状：")
print(fdata.shape)

# 查看数据描述信息
print("\n数据描述信息：")
print(fdata.describe())

# 显示聚餐时间段time的不重复值
print("\n聚餐时间段不重复值：")
print(fdata['time'].unique())

# 监测数据中的缺失值
print("\n数据中的缺失值：")
print(fdata.isnull().sum())

# 删除一行内有两个缺失值的数据
fdata.dropna(thresh=4, inplace=True)
print("\n删除一行内有两个缺失值的数据后：")
print(fdata.isnull().sum())

# 删除sex或time为空的行
fdata.dropna(subset=['sex', 'time'], inplace=True)
print("\n删除sex或time为空的行后：")
print(fdata.isnull().sum())

# 对有空缺值的数据用平均值替换
fdata.fillna(method='ffill', inplace=True)
print("\n用平均值替换空缺值后：")
print(fdata.isnull().sum())
