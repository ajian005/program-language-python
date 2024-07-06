import matplotlib.pyplot as plt
import numpy as np

print(dir(plt))

xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.plot(xpoints, ypoints, 'bo--')
plt.show()