

import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
img_array = plt.imread('matplotlib_test/tiger.jpeg')
tiger = img_array/255
print(tiger)

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()