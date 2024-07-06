'''
    使用随机数来设置散点图
'''
import matplotlib.pyplot as plt
import numpy as np

# 随机数生成器的种子
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title("RUNOOB Scatter Test")  # 设置标题
plt.show()  # 显示图像