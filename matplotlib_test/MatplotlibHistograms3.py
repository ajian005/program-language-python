'''
    Matplotlib 直方图
    pyplot 中的 hist() 方法来绘制直方图
    hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数。
    结合 Pandas 来绘制直方图
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)

# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)

# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()