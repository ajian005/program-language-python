'''
    ndarray.ndim
    ndarray.ndim 用于获取数组的维度数量（即数组的轴数）。
'''
import numpy as np

a = np.arange(24)
print(a.ndim) # a 现只有一个维度

# 现在调整其大小
b = a.reshape(2,3,4) # 现在 b 是三维的

print(b.ndim)

'''
ndarray.shape
ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"。

ndarray.shape 也可以用于调整数组大小。
'''
c = np.array([[1,2,3],[4,5,6]])
print("c.shape=", c.shape)

'''
    调整数组大小。
'''
d = np.array([[1,2,3],[4,5,6]])
d.shape = (3, 2)
print ("d=", d)

'''
    NumPy 也提供了 reshape 函数来调整数组大小。
'''
e = np.array([[1,2,3],[4,5,6]])
f = e.reshape(3,2)
print("f=", f)

'''
   ndarray.itemsize
   ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
   例如，一个元素类型为 float64 的数组 itemsize 属性值为 8(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节），又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）。
'''
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype=np.float64)
print(y.itemsize)

'''
    ndarray.flags
    ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性：
'''
x = np.array([1,2,3,4,5])
print(x.flags)