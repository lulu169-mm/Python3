import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 导入前待处理数据并显示前五行
fdata = pd.read_excel('')

# 修改列名为汉字，并显示前5行
fdata.rename(columns={'total_bill': '消费总额', 'tip': '小费', 'sex': '性别',
                      'smoker': '是否吸烟', 'day': '星期', 'time': '聚餐时间段', 'size': '人数'}, inplace=True)

# 每行数据至少有四个非空值才能存活
fdata.dropna(thresh=4, axis=0)

# 人均消费
fdata['人均消费'] = round(fdata['消费总额'] / fdata['人数'])

# 查询吸烟男性中人均消费大于15的数据
# fdata.query('是否吸烟=="Yes"&性别=="Male"&人均消费>15')

# 分析消费金额与消费总额的关系
fdata.plot(kind='scatter', x='消费总额', y='小费')

# 分析男性顾客和女性顾客谁更慷慨
# fdata.groupby('性别')['小费'].mean()

# 分析星期和小费的关系
r = fdata.groupby('星期')['小费'].mean()
fig = r.plot(kind='bar', x='星期', y='小费', fontsize=12, rot=30)
fig.axes.title.set_size(16)

# 性别+吸烟组合对慷慨度的影响
r = fdata.groupby(['性别', '是否吸烟'])['小费'].mean()
fig = r.plot(kind='bar', x=['性别', '是否吸烟'], y='小费', fontsize=12, rot=30)
fig.axes.title.set_size(16)

# 分析聚餐时间段与小费的关系
r = fdata.groupby(['聚餐时间段'])['小费'].mean()
fig = r.plot(kind='bar', x='聚餐时间段', y='小费', fontsize=12, rot=30)
fig.axes.title.set_size(16)

plt.show()
