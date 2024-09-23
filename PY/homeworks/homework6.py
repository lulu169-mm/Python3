import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os

# 设置环境变量以防止 Unicode 解码错误
os.environ['PYTHONIOENCODING'] = 'utf-8'

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False

# 载入泰坦尼克号数据集
titanic = sns.load_dataset('titanic')

# 用年龄的均值填充缺失值
mean_age = titanic['age'].mean()
titanic['age'] = titanic['age'].fillna(mean_age)

# 对登船地点进行缺失值填充（填充为S）
titanic['embarked'] = titanic['embarked'].fillna("S")

# 删除deck字段（缺失值太多）
del titanic['deck']

# 基于性别，绘制乘客年龄箱线图
sns.boxplot(x='sex', y='age', data=titanic)
plt.show()

# 对船舱等级进行计数
sns.countplot(x='class', data=titanic)
plt.show()

# 结合船舱等级，绘制乘客年龄分布的小提琴图
sns.violinplot(y='age', x='class', data=titanic)
plt.show()

# 对年龄进行分级，分开老人和小孩的数据
def age_level(age):
    if age <= 16:
        return 'child'
    elif age >= 60:
        return 'old'
    else:
        return 'middle'

titanic['age_level'] = titanic['age'].map(age_level)

# 对分级后的年龄进行可视化
sns.countplot(x='age_level', data=titanic)
plt.show()

# 分析乘客年龄与生还乘客之间的关系
sns.countplot(x='age_level', hue='survived', data=titanic)
plt.legend(loc="best", fontsize='15')
plt.show()
