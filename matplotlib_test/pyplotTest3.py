import matplotlib.pyplot as plt
import numpy as np

# print(dir(plt))
# 如果我们不指定 x 轴上的点，则 x 会根据 y 的值来设置为 0, 1, 2, 3..N-1。
ypoints = np.array([3,8,1,10])

plt.plot(ypoints, 'bo--')
plt.show()