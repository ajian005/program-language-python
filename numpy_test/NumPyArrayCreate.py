'''
    NumPy 创建数组
    ndarray 数组除了可以使用底层 ndarray 构造器来创建外，也可以通过以下几种方式来创建。
'''

'''
    numpy.empty
    numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
'''
import numpy as np

'''
    下面是一个创建空数组的实例：
'''
x = np.empty([3,2], dtype=int)
print('x=', x)

'''
    numpy.zeros
    创建指定大小的数组，数组元素以 0 来填充
'''

# 默认为浮点数
y = np.zeros(5)
print('y=', y)

# 设置类型为整数
y2 = np.zeros((5,), dtype=int)
print('y2=', y2)

# 自定义类型
z = np.zeros((2,2), dtype=[('x', 'i4'), ('y', 'i4')])
print('z=', z)

'''
    numpy.ones
    创建指定形状的数组，数组元素以 1 来填充：
'''
# 默认为浮点数
xx = np.ones(5)
print(xx)

# 自定义类型
x = np.ones([2,2], dtype=int)
print('x=',x)

'''
    numpy.zeros_like
    numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充。
    numpy.zeros 和 numpy.zeros_like 都是用于创建一个指定形状的数组，其中所有元素都是 0。
    它们之间的区别在于：numpy.zeros 可以直接指定要创建的数组的形状，而 numpy.zeros_like 则是创建一个与给定数组具有相同形状的数组。
'''

# 创建一个 3x3 的二维数组
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print('zeros_arr=',zeros_arr)

'''
    numpy.ones_like
    numpy.ones_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充。
    numpy.ones 和 numpy.ones_like 都是用于创建一个指定形状的数组，其中所有元素都是 1。
    它们之间的区别在于：numpy.ones 可以直接指定要创建的数组的形状，而 numpy.ones_like 则是创建一个与给定数组具有相同形状的数组。
'''
# 创建一个 3x3 的二维数组
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 创建一个与arr形状相同的，所有元素都为1的数组
ones_arr = np.ones_like(arr)
print(ones_arr)