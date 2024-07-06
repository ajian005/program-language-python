'''
3. 柱状图 - sns.barplot()
用于绘制变量的均值或其他聚合函数的柱状图。
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'B', 'C'], 'Value': [3, 7, 5]}
df = pd.DataFrame(data)

# 绘制柱状图
sns.barplot(x='Category', y='Value', data=df)

# 显示图形
plt.show()