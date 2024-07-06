'''
4. 箱线图 - sns.boxplot()
用于绘制变量的分布情况，包括中位数、四分位数等。
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

# 绘制箱线图
sns.boxplot(x='Category', y='Value', data=df)

# 显示图形
plt.show()