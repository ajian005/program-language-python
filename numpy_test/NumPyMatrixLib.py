'''
NumPy 矩阵库(Matrix)
    NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。
'''
import numpy as np

# 转置矩阵
# NumPy 中除了可以使用 numpy.transpose 函数来对换数组的维度，还可以使用 T 属性。。
# 例如有个 m 行 n 列的矩阵，使用 t() 函数就能转换为 n 行 m 列的矩阵。
a = np.arange(12).reshape(3,4)
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)

# matlib.empty() 函数返回一个新的矩阵
import numpy.matlib 
import numpy as np
print (np.matlib.empty((2,2)))
# 填充为随机数据

# numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
print (np.matlib.zeros((2,2)))

# numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
print (np.matlib.ones((2,2)))

# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))

# numpy.matlib.identity() 函数返回给定大小的单位矩阵。
# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))

# numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
print (np.matlib.rand(3,3))

