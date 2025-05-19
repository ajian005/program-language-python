'''
Python lambda（匿名函数）
Python 使用 lambda 来创建匿名函数。

lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。

匿名函数不需要使用 def 关键字定义完整函数。

lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。

lambda 函数特点：

lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。
lambda 语法格式：

lambda arguments: expression
lambda是 Python 的关键字，用于定义 lambda 函数。
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
expression 是一个表达式，用于计算并返回函数的结果。
'''

# 以下的 lambda 函数没有参数：
f = lambda: "Hello World!"
print(f())  # 输出: Hello World!

# 以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果：
x = lambda a: a + 10
print(x(5))  # 输出: 15

'''
lambda 函数也可以设置多个参数，参数使用逗号 , 隔开：

以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果：
'''
x = lambda a, b: a * b
print(x(5, 6))

# 以下实例使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果：
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # 输出: 13
# 输出: 30

# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

# 使用 lambda 函数与 filter() 一起，筛选偶数：
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6, 8]

# 下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
products = reduce(lambda x, y: x * y, numbers)
print(products)  # 输出: 120