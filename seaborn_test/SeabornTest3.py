'''
2. 折线图 - sns.lineplot()
用于绘制变量随着另一个变量变化的趋势线图。
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 绘制散点图
sns.lineplot(x='X', y='Y', data=df)

# 显示图形
plt.show()