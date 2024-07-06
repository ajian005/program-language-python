'''
6. 小提琴图 - sns.violinplot()
用于显示分布的形状和密度估计，结合了箱线图和核密度估计。


'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

# 绘制小提琴图
sns.violinplot(x='Category', y='Value', data=df)

# 显示图形
plt.show()