'''
    imsave() 方法是 Matplotlib 库中用于将图像数据保存到磁盘上的函数。
    通过 imsave() 方法我们可以轻松将生成的图像保存到我们指定的目录中。
    imsave() 方法保存图片支持多种图像格式，例如 PNG、JPEG、BMP 等。
'''
# 一个使用 imsave() 方法保存图像的简单实例：
import matplotlib.pyplot as plt
import numpy as np

# 创建一个二维的图像数据
img_data = np.random.random((100, 100))

# 显示图像
plt.imshow(img_data)

# 保存图像到磁盘上
plt.imsave('matplotlib_test/runoob-test.png', img_data)
