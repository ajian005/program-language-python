'''
    以下实例添加一个简单的网格线，参数使用默认值：
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([1,4,9,16])

plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)
# plt.grid()
# plt.grid(axis='x') # 设置 y 就在轴方向显示网格线
# plt.grid(axis='y') # 设置 x 就在轴方向显示网格线
plt.grid(color = 'b', linestyle = '--', linewidth = 0.5)


plt.show()