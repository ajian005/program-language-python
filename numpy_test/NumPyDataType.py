'''
NumPy 数据类型
'''

import numpy as np

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

 # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i8')
print(dt)

# # 字节顺序标注
dt = np.dtype('<i4')
print(dt)

# 首先创建结构化数据类型
dt = np.dtype([('age', np.int8)])
print(dt)

# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
print(a['age'])
# print(a[np.int8])

# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)

a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
print(a['name'])
print(a['age'])
print(a['marks'])
