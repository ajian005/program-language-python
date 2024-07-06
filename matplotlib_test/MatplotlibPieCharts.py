'''
Matplotlib 饼图
饼图（Pie Chart）是一种常用的数据可视化图形，用来展示各类别在总体中所占的比例。
使用 pyplot 中的 pie() 方法来绘制饼图。
'''

# 简单实用 pie() 来创建一个饼图:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
# 设置饼图各个扇形的标签与颜色：
labels1=['A','B','C','D'] # 设置饼图标签
colors1=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"] # 设置饼图颜色
plt.pie(y, labels=labels1, colors=colors1) # 绘制饼图
plt.title("Pie chart") # 设置标题
plt.show()