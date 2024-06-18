# 以下的 lambda 函数没有参数
f = lambda:  "Hello, world!"
print(f())  # 输出 "Hello, world!"

# 以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果：
x = lambda a : {a + 10}
print(x(5))  # 输出 15

'''
    lambda 函数也可以设置多个参数，参数使用逗号 , 隔开：
    以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果：
'''
x = lambda a, b : {a * b}
print(x(5, 6))  # 输出 30

x = lambda a, b : a * b
print(x(5, 6))  # 输出 30

'''
    以下实例使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果：
'''
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # 输出 13

'''
    lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。
'''
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x**2, numbers))
print(squared)  # 输出 [1, 4, 9, 16, 25]

'''
    使用 lambda 函数与 filter() 一起，筛选偶数：
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)  # 输出 [2, 4, 6, 8]

'''
下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y : x * y, numbers)
print(product)  # 输出 120