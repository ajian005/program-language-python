import matplotlib.pyplot as plt
import numpy as np

print(dir(plt))

xpoints = np.array([0,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints, 'bo--')
plt.show()