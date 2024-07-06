'''
    Matplotlib 绘制多图
'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("plot 1")

# plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.title("plot 2")

# plot 3:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.title("plot 3")

# plot 4:
x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 5, 6])
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.title("plot 4")

plt.suptitle("Matplotlib Subplot")
plt.show()