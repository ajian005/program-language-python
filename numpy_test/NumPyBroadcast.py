import numpy as np 

'''
NumPy 广播(Broadcast)
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。
如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
'''
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

# 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。
a = np.array([  [0, 0, 0],
                [10,10,10],
                [20,20,20],
                [30,30,30]])
b = np.array([0,1,2])
print(a + b)

# 4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算：
a = np.array([[ 0, 0, 0],
                [10,10,10],
                [20,20,20],
                [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print('bb=',bb)
print(a + bb)
