'''
    显示矩阵
'''
import matplotlib.pyplot as plt
import numpy as np
# from PIL import Image

# 生成一个随机矩阵
data = np.random.rand(10, 10)

# 绘制矩阵
plt.imshow(data)

# 显示图像
plt.show()