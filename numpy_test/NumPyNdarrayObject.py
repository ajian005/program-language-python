import numpy as np

# 一个维度  
a = np.array([1,2,3])
print(a)

# 多于一个维度
b = np.array([[1,2,3], [4,5,6]])
print("b=", b)

# 最小维度  
c = np.array([1, 2, 3], ndmin=2)
print("c=", c)

# dtype 参数  
d = np.array([1, 2, 3], dtype=complex)
print("d=", d)
