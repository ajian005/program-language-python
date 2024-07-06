'''
    设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "Runoob-4"])
y = np.array([12, 22, 6, 18])
# plt.bar(x, y, color="#4CAF50")
# 自定义各个柱形的颜色：
# plt.bar(x, y, width=0.1, color = ["#4CAF50","red","hotpink","#556B2F"])
plt.barh(x, y, height = 0.1)
plt.show()