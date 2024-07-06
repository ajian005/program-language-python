'''
imread() 方法是 Matplotlib 库中的一个函数，用于从图像文件中读取图像数据。
'''

# 以下实例演示了如何使用 imread 函数从一张图像文件中读取图像数据，并将其显示出来：
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = plt.imread('matplotlib_test/map.jpeg')
# 显示图像
plt.imshow(img)
plt.show()