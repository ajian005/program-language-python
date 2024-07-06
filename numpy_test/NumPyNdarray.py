'''
    NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
    ndarray 对象是用于存放同类型元素的多维数组。
    ndarray 中的每个元素在内存中都有相同存储大小的区域。
'''
import numpy as np

# 一维数组
a = np.array([1, 2, 3])
print(a)

# 多于一个维度  
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# # 最小维度  
c = np.array([1, 2, 3, 4, 5], ndmin =  64) 
print(c)

# # dtype 参数  
d = np.array([1, 2, 3], dtype = complex)
print(d)

