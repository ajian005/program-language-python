'''
    显示地图
'''
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 加载地图图像, 下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = Image.open('matplotlib_test/map.jpeg')

# 转换为数组
data = np.array(img)

# 绘制地图
plt.imshow(data)

# 隐藏坐标轴
plt.axis('off')

# 显示图像
plt.show()