'''
    NumPy IO
    Numpy 可以读写磁盘上的文本数据或二进制数据。
    NumPy 为 ndarray 对象引入了一个简单的文件格式：npy。
'''
# numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中。
import numpy as np 
 
a = np.array([1,2,3,4,5]) 
 
# 保存到 outfile.npy 文件上
np.save('numpy_test/outfile.npy',a) 
 
# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('numpy_test/outfile2',a)

# 我们可以使用 load() 函数来读取数据就可以正常显示了：
import numpy as np 
 
b = np.load('numpy_test/outfile.npy')  
print (b)

# numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中。
import numpy as np 
 
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
np.savez("runoob.npz", a, b, sin_array = c)
r = np.load("runoob.npz")  
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组 a
print(r["arr_1"]) # 数组 b
print(r["sin_array"]) # 数组 c

# savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。
import numpy as np 
a = np.array([1,2,3,4,5]) 
np.savetxt('numpy_test/out.txt',a) 
b = np.loadtxt('numpy_test/out.txt')  
print(b)

# 使用 delimiter 参数：
import numpy as np 
 
a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("numpy_test/out2.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b = np.loadtxt("numpy_test/out2.txt",delimiter=",") # load 时也要指定为逗号分隔
print(b)