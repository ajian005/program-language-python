#!/usr/bin/python3
'''
    Python3 迭代器与生成器
'''
# 字符串，列表或元组对象都可用于创建迭代器：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))
print (next(it))
print (next(it))
# print (next(it))

# 迭代器对象可以使用常规for语句进行遍历：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

# 也可以使用 next() 函数：
import  sys  # 引入 sys 模块

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象

print("-----------------")

'''
while True:
    try:
        print (next(it))
    except StopIteration:
        # sys.exit()
        print("迭代器已完成")
'''


'''
    创建一个迭代器
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print (next(myiter))
print (next(myiter))
print (next(myiter))
print (next(myiter))
print (next(myiter))


'''
StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

在 20 次迭代后停止执行：
'''
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for x in myiter2:
    print (x)



'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
调用一个生成器函数，返回的是一个迭代器对象。
'''
def countdown(n):
    print("开始倒计时")
    while n > 0:
        yield n
        n -= 1
    print("倒计时结束")

# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value) # 输出: 2, 1


# 以下实例使用 yield 实现斐波那契数列：
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()  # 退出程序