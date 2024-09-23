import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图表
fig = plt.figure()

# 子图 1
ax1 = fig.add_subplot(121)
t = np.arange(0.0, 5, 0.01)
s = np.sin(2 * np.pi * t)
ax1.plot(t, s, lw=2)

# 用箭头注释一个点
bbox = dict(boxstyle='round', facecolor='white')
plt.annotate('局部最大值', xy=(2.3, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', edgecolor='red', headwidth=7, width=2), bbox=bbox)

# 设置标签和文本
ax1.set_ylabel('Y轴', fontsize=12)
ax1.set_xlabel('X轴', fontsize=12)
ax1.set_ylim(-2, 2)
ax1.text(1, 1.2, '最大值', fontsize=18)
ax1.text(1.2, -1.8, '$y = \\sin(2 \\pi t)$', bbox=bbox, rotation=10, alpha=0.8)

# 子图 2
ax2 = fig.add_subplot(122)
x = np.linspace(0, 10, 200)
y = np.sin(x)
ax2.plot(x, y, linestyle='-.', color='purple')

# 用箭头和边框注释一个点
ax2.annotate(text='我在这里', xy=(4.8, np.sin(4.8)), xytext=(3.7, -0.2), weight='bold', color='k',
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='red'),
              bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', ec='k', lw=1, alpha=0.8))

# 设置坐标轴范围、标签和文本
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlim(0, 10)
ax2.text(6, -1.9, '$y = \\sin(x)$', bbox=dict(boxstyle='square', facecolor='white', ec='black'))
ax2.grid(ls=":", color='gray', alpha=0.5)

# 添加带有边框的水印
ax2.text(4.5, 1, 'NWNU', fontsize=15, alpha=0.3, color='gray',
         bbox=dict(facecolor='white', boxstyle='round', edgecolor='gray', alpha=0.3))

# 显示图表
plt.show()
