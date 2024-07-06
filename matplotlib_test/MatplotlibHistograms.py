'''
    Matplotlib 直方图
    pyplot 中的 hist() 方法来绘制直方图
    hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数。
    简单实用 hist() 来创建一个直方图
'''
import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据
data = np.random.randn(1000)

# 绘制直方图
plt.hist(data, bins=30, color='steelblue', edgecolor='black')

# 设置图表属性
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()