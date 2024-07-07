'''
NumPy 排序、条件筛选函数
NumPy 提供了多种排序的方法。 这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。 
'''
import numpy as np

# numpy.sort()
# numpy.sort() 函数返回输入数组的排序副本
a = np.array([[3,7],[9,1]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 sort() 函数：')
print (np.sort(a))
print ('\n')
print ('按列排序：')
print (np.sort(a, axis =  0))
print ('\n')
# 在 sort 函数中排序字段 
dt = np.dtype([('name',  'S10'),('age',  int)]) 
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
print ('我们的数组是：')
print (a)
print ('\n')
print ('按 name 排序：')
print (np.sort(a, order =  'name'))

# numpy.argsort()
# numpy.argsort() 函数返回的是数组值从小到大的索引值。
x = np.array([3,  1,  2])  
print ('我们的数组是：')
print (x)
print ('\n')
print ('对 x 调用 argsort() 函数：')
y = np.argsort(x)  
print (y)
print ('\n')
print ('以排序后的顺序重构原数组：')
print (x[y])
print ('\n')
print ('使用循环重构原数组：')
for i in y:  
    print (x[i], end=" ")

# numpy.lexsort()
# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
nm =  ('raju','anil','ravi','amar') 
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.') 
ind = np.lexsort((dv,nm))  
print ('调用 lexsort() 函数：') 
print (ind) 
print ('\n') 
print ('使用这个索引来获取排序后的数据：') 
print ([nm[i]  +  ", "  + dv[i]  for i in ind])

# numpy.ndarray.byteswap() 函数将 ndarray 中每个元素中的字节进行大小端转换。
a = np.array([1,  256,  8755], dtype = np.int16)  
print ('我们的数组是：')
print (a)
print ('以十六进制表示内存中的数据：')
print (map(hex,a))
# byteswap() 函数通过传入 true 来原地交换 
print ('调用 byteswap() 函数：')
print (a.byteswap(True))
print ('十六进制形式：')
print (map(hex,a))
# 我们可以看到字节已经交换了

