'''
    Matplotlib 柱形图
    我们可以使用 pyplot 中的 bar() 方法来绘制柱形图。
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "Runoob-4"])
y = np.array([12, 22, 6, 18])
# plt.bar(x, y)
# 垂直方向的柱形图可以使用 barh() 方法来设置：
plt.barh(x, y)
plt.show()