'''
    Matplotlib 散点图
    我们可以使用 pyplot 中的 scatter() 方法来绘制散点图。
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
# 设置图标大小
sizes = np.array([20, 50, 100, 200, 500, 1000, 2000, 5000])
# 设置颜色
colors = np.array(["red", "green", "blue", "yellow", "black", "cyan", "magenta", "purple"])
plt.scatter(x, y, s = sizes, c = colors)
# plt.scatter(x, y, s = 100)
# plt.scatter(x, y)
plt.show()