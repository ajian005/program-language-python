import numpy as np
a = np.arange(12).reshape(3, 4)

print('原数组: ')
print(a)
print('\n')

print (np.matlib.empty((2, 2)))

print( np.matlib.zeros((2, 2)))

print( np.matlib.ones((2, 2)))

print( np.matlib.eye(n=3, M=4, k=0, dtype=float) )

#  大小为 5，类型位浮点型
print( "====================================================================" )
print( np.matlib.identity(5, dtype=float) )

print( np.matlib.rand(3, 3) )

print( np.matlib.rand(3, 3) )

j = np.asarray(1)
print(j)
