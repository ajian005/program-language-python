'''
    imshow() 函数是 Matplotlib 库中的一个函数，用于显示图像。
    imshow() 函数常用于绘制二维的灰度图像或彩色图像。
    imshow() 函数可用于绘制矩阵、热力图、地图等。
'''
import matplotlib.pyplot as plt
import numpy as np

# 生成一个随机的彩色图像
img = np.random.rand(10, 10)

# 绘制彩色图像
# plt.imshow(img)

# 显示热力图
plt.imshow(img, cmap='hot')

# 显示图像
plt.colorbar()
# 显示图像
plt.show()