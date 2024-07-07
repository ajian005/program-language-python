'''
    位运算是一种在二进制数字的位级别上进行操作的一类运算，它们直接操作二进制数字的各个位，而不考虑数字的整体值。
    位运算在计算机科学中广泛应用于优化和处理底层数据。
    NumPy "bitwise_" 开头的函数是位运算函数。
'''
import numpy as np

arr1 = np.array([True, False, True], dtype=bool)
arr2 = np.array([False, True, False], dtype=bool)

result_and = np.bitwise_and(arr1, arr2)
result_or = np.bitwise_or(arr1, arr2)
result_xor = np.bitwise_xor(arr1, arr2)
result_not = np.invert(arr1)

print("AND:", result_and)  # [False, False, False]
print("OR:", result_or)    # [True, True, True]
print("XOR:", result_xor)  # [True, True, True]
print("NOT:", result_not)  # [False, True, False]

# 按位取反
arr_invert = np.invert(np.array([1, 2], dtype=np.int8))
print("Invert:", arr_invert)  # [-2, -3]

# 左移位运算
arr_left_shift = np.left_shift(5, 2)
print("Left Shift:", arr_left_shift)  # 20

# 右移位运算
arr_right_shift = np.right_shift(10, 1)
print("Right Shift:", arr_right_shift)  # 5


# bitwise_and() 函数对数组中整数的二进制形式执行位与运算。
print ('13 和 17 的二进制形式：')
a,b = 13,17
print (bin(a), bin(b))
print ('\n')
 
print ('13 和 17 的位与：')
print (np.bitwise_and(13, 17))

# bitwise_or()函数对数组中整数的二进制形式执行位或运算。
a,b = 13,17 
print ('13 和 17 的二进制形式：')
print (bin(a), bin(b))
 
print ('13 和 17 的位或：')
print (np.bitwise_or(13, 17))

# invert() 函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0。
# 对于有符号整数，取该二进制数的补码，然后 +1。二进制数，最高位为0表示正数，最高位为 1 表示负数。
print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print (np.invert(np.array([13], dtype = np.uint8)))
print ('\n')
# 比较 13 和 242 的二进制表示，我们发现了位的反转
 
print ('13 的二进制表示：')
print (np.binary_repr(13, width = 8))
print ('\n')
 
print ('242 的二进制表示：')
print (np.binary_repr(242, width = 8))

# left_shift() 函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的 0。
print ('将 10 左移两位：')
print (np.left_shift(10,2))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
#  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。

# right_shift() 函数将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的 0。
print ('将 40 右移两位：')
print (np.right_shift(40,2))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
#  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。