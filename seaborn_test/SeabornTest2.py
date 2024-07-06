'''
  1. 散点图 - sns.scatterplot()
     用于绘制两个变量之间的散点图，可选择添加趋势线。
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 绘制散点图
sns.scatterplot(x='A', y='B', data=df)

# 显示图形
plt.show()