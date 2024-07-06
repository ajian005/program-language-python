'''
NumPy 数组属性
NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。

'''
import numpy as np

# ndarray.ndim 用于返回数组的维数，等于秩。
a = np.arange(24)
print(a.ndim)  # 1
print(a)
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)
print(b)

# ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"。
a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape)  # 返回 (2, 3)，表示 2 行 3 列

# 调整数组大小。
a.shape = (3,2)  # 返回一个 3 行 4 列的数组
print (a)  

# NumPy 也提供了 reshape 函数来调整数组大小。
b = a.reshape(3,2)
print (b)

# ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)  # 返回 1


# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)

# ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性
x = np.array([1,2,3,4,5])  
print (x.flags)