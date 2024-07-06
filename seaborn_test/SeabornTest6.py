'''
5. 热图 - sns.heatmap()
用于绘制矩阵数据的热图，通常用于展示相关性矩阵。


'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 创建一个相关性矩阵
correlation_matrix = df.corr()

# 使用热图可视化相关性矩阵
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# 显示图形
plt.show()