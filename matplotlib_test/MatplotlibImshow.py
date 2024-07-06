'''
    imshow() 函数是 Matplotlib 库中的一个函数，用于显示图像。
    imshow() 函数常用于绘制二维的灰度图像或彩色图像。
    imshow() 函数可用于绘制矩阵、热力图、地图等。
'''
import matplotlib.pyplot as plt
import numpy as np

# 生成一个二维随机数组
img = np.random.rand(10, 10)

# 绘制灰度图像
plt.imshow(img, cmap='gray')

# 显示图像
plt.show()