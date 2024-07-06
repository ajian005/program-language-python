import matplotlib.pyplot as plt
import numpy as np

# print(dir(plt))
# 以下实例我们绘制一个正弦和余弦图，在 plt.plot() 参数中包含两对 x,y 值，第一对是 x,y，这对应于正弦函数，第二对是 x,z，这对应于余弦函数。
xpoints = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
ypoints = np.sin(xpoints)
zpoints = np.cos(xpoints)
plt.plot(xpoints, ypoints, xpoints, zpoints)
plt.show()