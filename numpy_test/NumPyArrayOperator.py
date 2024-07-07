'''
Numpy 数组操作 https://www.runoob.com/numpy/numpy-array-manipulation.html
    Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：
    修改数组形状
    翻转数组
    修改数组维度
    连接数组
    分割数组
    数组元素的添加与删除
'''
import numpy as np
'''
    修改数组形状
'''
# numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下：
a = np.arange(8)
print('原始数组:')
print(a)
print('\n')

b = a.reshape(4,2)
print('修改后的数组:')
print(b)


# numpy.ndarray.flat 是一个数组元素迭代器，实例如下:
a = np.arange(8).reshape(2,4)
print('原始数组:')
for row in a:
     print(row)

#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
     print(element)


# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
# 默认按行
 
print ('展开的数组：')
print (a.flatten())
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))

# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 ravel 函数之后：')
print (a.ravel())
print ('\n')
 
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))

'''
翻转数组
'''
# numpy.transpose 函数用于对换数组的维度，格式如下：
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))

# numpy.ndarray.T 类似 numpy.transpose：
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)


# numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
# 创建了三维的 ndarray
a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('获取数组中一个值：')
print(np.where(a==6))   
print(a[1,1,0])  # 为 6
print ('\n')
 
 
# 将轴 2 滚动到轴 0（宽度到深度）
 
print ('调用 rollaxis 函数：')
b = np.rollaxis(a,2,0)
print (b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b==6))   
print ('\n')
 
# 将轴 2 滚动到轴 1：（宽度到高度）
 
print ('调用 rollaxis 函数：')
c = np.rollaxis(a,2,1)
print (c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c==6))   
print ('\n')

# numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
# 创建了三维的 ndarray
a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
 
print ('调用 swapaxes 函数后的数组：')
print (np.swapaxes(a, 2, 0))

'''
修改数组维度
'''
# numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
# 该函数使用两个数组作为输入参数，如下实例：
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])  
# 对 y 广播 x
b = np.broadcast(x,y)  
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print ('对 y 广播 x：')
r,c = b.iters
 
 # Python3.x 为 next(context) ，Python2.x 为 context.next()
print (next(r), next(c))
print (next(r), next(c))
print ('\n')
# shape 属性返回广播对象的形状
print ('广播对象的形状：')
print (b.shape)
print ('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x,y)
c = np.empty(b.shape)
 
print ('手动使用 broadcast 将 x 与 y 相加：')
print (c.shape)
print ('\n')
c.flat = [u + v for (u,v) in b]
 
print ('调用 flat 函数：')
print (c)
print ('\n')
# 获得了和 NumPy 内建的广播支持相同的结果
 
print ('x 与 y 的和：')
print (x + y)

# numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。 如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。
a = np.arange(4).reshape(1,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 broadcast_to 函数之后：')
print (np.broadcast_to(a,(4,4)))
 
# numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:
x = np.array(([1,2],[3,4]))
 
print ('数组 x：')
print (x)
print ('\n')
y = np.expand_dims(x, axis = 0)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)
print ('\n')
# 在位置 1 插入轴
y = np.expand_dims(x, axis = 1)
 
print ('在位置 1 插入轴之后的数组 y：')
print (y)
print ('\n')
 
print ('x.ndim 和 y.ndim：')
print (x.ndim,y.ndim)
print ('\n')
 
print ('x.shape 和 y.shape：')
print (x.shape, y.shape)

# numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：
x = np.arange(9).reshape(1,3,3)
 
print ('数组 x：')
print (x)
print ('\n')
y = np.squeeze(x)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)

'''
    连接数组
'''
# numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
# 两个数组的维度相同
 
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))

# numpy.stack 函数用于沿新轴连接数组序列，格式如下：
a = np.array([[1,2],[3,4]])
print ('第一个数组：')
print (a)
print ('\n')

b = np.array([[5,6],[7,8]])
print ('第二个数组：')
print (b)
print ('\n')
 
print ('沿轴 0 堆叠两个数组：')
print (np.stack((a,b),0))
print ('\n')
 
print ('沿轴 1 堆叠两个数组：')
print (np.stack((a,b),1))

# numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
a = np.array([[1,2],[3,4]])
print ('第一个数组：')
print (a)
print ('\n')

b = np.array([[5,6],[7,8]])
print ('第二个数组：')
print (b)
print ('\n')
 
print ('水平堆叠：')
c = np.hstack((a,b))
print (c)
print ('\n')

# numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('竖直堆叠：')
c = np.vstack((a,b))
print (c)


'''
    分割数组
'''
# numpy.split 函数沿特定的轴将数组分割为子数组
a = np.arange(9)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('将数组分为三个大小相等的子数组：')
b = np.split(a,3)
print (b)
print ('\n')
 
print ('将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print (b)

# axis 为 0 时在水平方向分割，axis 为 1 时在垂直方向分割：
a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')
print('默认分割（0轴）：')
b = np.split(a,2)
print(b)
print('\n')

print('沿水平方向分割：')
c = np.split(a,2,1)
print(c)
print('\n')

print('沿水平方向分割：')
d= np.hsplit(a,2)
print(d)

# numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
 
print ('拆分后：')
print(np.hsplit(harr, 3))

# numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。
a = np.arange(16).reshape(4,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('竖直分割：')
b = np.vsplit(a,2)
print (b)

'''
数组元素的添加与删除
'''
# numpy.resize 函数返回指定大小的新数组。
# 如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的形状：')
print (a.shape)
print ('\n')
b = np.resize(a, (3,2))
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('第二个数组的形状：')
print (b.shape)
print ('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
 
print ('修改第二个数组的大小：')
b = np.resize(a,(3,3))
print (b)

# numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外，输入数组的维度必须匹配否则将生成ValueError。
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('向数组添加元素：')
print (np.append(a, [7,8,9]))
print ('\n')
 
print ('沿轴 0 添加元素：')
print (np.append(a, [[7,8,9]],axis = 0))
print ('\n')
 
print ('沿轴 1 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))

# numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
# 函数会在指定位置（或位置数组）插入给定的值或数组，然后返回新的数组。
# 被插入的元素可以是标量值，也可以是数组。需要注意的是，插入操作会返回一个新的数组，而不会改变原始数组。
a = np.array([[1,2],[3,4],[5,6]])
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在删除之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
print ('\n')
print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
 
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('\n')
 
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))


# numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
a = np.arange(12).reshape(3,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print (np.delete(a,5))
print ('\n')
 
print ('删除第二列：')
print (np.delete(a,1,axis = 1))
print ('\n')
 
print ('包含从数组中删除的替代值的切片：')
a = np.array([1,2,3,4,5,6,7,8,9,10])
print (np.delete(a, np.s_[::2]))

# numpy.unique 函数用于去除数组中的重复元素。
a = np.array([5,2,6,2,7,5,6,8,2,9])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的去重值：')
u = np.unique(a)
print (u)
print ('\n')
 
print ('去重数组的索引数组：')
u,indices = np.unique(a, return_index = True)
print (indices)
print ('\n')
 
print ('我们可以看到每个和原数组下标对应的数值：')
print (a)
print ('\n')
 
print ('去重数组的下标：')
u,indices = np.unique(a,return_inverse = True)
print (u)
print ('\n')
 
print ('下标为：')
print (indices)
print ('\n')
 
print ('使用下标重构原数组：')
print (u[indices])
print ('\n')
 
print ('返回去重元素的重复数量：')
u,indices = np.unique(a,return_counts = True)
print (u)
print (indices)
