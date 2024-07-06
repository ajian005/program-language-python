import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 系统的字体：
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)

# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf", size=18)
plt.rcParams['font.family']=['Hiragino Sans GB']


plt.title("中文Title: Sports Watch Data")
plt.xlabel("中文Average Pulse")
plt.ylabel("中文Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()

