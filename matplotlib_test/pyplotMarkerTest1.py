import matplotlib.pyplot as plt
import numpy as np

# 绘图过程如果我们想要给坐标自定义一些不一样的标记，就可以使用 plot() 方法的 marker 参数来定义。
ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])
# fmt = '[marker][line][color]'
plt.plot(ypoints, 'o:r')
plt.show()
