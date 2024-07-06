'''
    ndarray 数组除了可以使用底层 ndarray 构造器来创建
'''
import numpy as np 

# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
x = np.empty([3,2], dtype = int) 
print (x)

# 创建指定大小的数组，数组元素以 0 来填充
# 默认为浮点数
x = np.zeros(5) 
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype = int) 
print(y)

# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)

# 创建指定形状的数组，数组元素以 1 来填充：
# 默认为浮点数
x = np.ones(5) 
print(x)

# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)


# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)

import numpy as np
 
# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)

# NumPy 从已有的数组创建数组
x =  [1,2,3] 
a = np.asarray(x)  
print (a)

# 将元组转换为 ndarray:
x =  (1,2,3) 
a = np.asarray(x)  
print (a)

# 将元组列表转换为 ndarray:
# y =  [(1,2,3),(4,5)]
# b = np.asarray(y)  
# print (b)

# 设置了 dtype 参数
x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)


# numpy.frombuffer 用于实现动态数组。
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)

# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)

'''
# NumPy 从数值范围创建数组
'''

# 生成 0 到 4 长度为 5 的数组:
x = np.arange(5)  
print (x)

# 设置返回类型位 float
# 设置了 dtype
x = np.arange(5, dtype =  float)  
print (x)

# 设置了起始值、终止值及步长
x = np.arange(10,20,2)  
print (x)

# 以下实例用到三个参数，设置起始点为 1 ，终止点为 10，数列个数为 10
a = np.linspace(1,10,10)
print(a)

# 设置元素全部是1的等差数列
a = np.linspace(1,1,10)
print(a)

# 将 endpoint 设为 false，不包含终止值
a = np.linspace(10, 20,  5, endpoint =  False)  
print(a)

# 如果将 endpoint 设为 true，则会包含 20
a =np.linspace(1,10,10,retstep= True)
print(a)

# 拓展例子
b =np.linspace(1,10,10).reshape([10,1])
print(b)

'''
numpy.logspace 函数用于创建一个于等比数列
'''
# 默认底数是 10
a = np.logspace(1.0,  2.0, num =  10)  
print (a)

# 将对数的底数设置为 2
a = np.logspace(0,9,10,base=2)
print (a)
