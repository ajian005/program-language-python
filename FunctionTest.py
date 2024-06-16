#!/usr/bin/python3

def hello() :
    print("Hello, World!")

hello()

'''
    比较两个数，并返回较大的数:
'''
def max(a, b):
    if a > b:
        return a
    else:
        return b
a = 4
b = 5
print(max(a, b))

# 计算面积函数:
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome, " + name + "!")

print_welcome("RuningNoob")
w = 4
h = 5
print("width =", w, "height =", h, "area =", area(w, h))

'''
    函数调用
'''
# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数!")

# 参数传递
# python 传不可变对象实例
def change(a):
    print(id(a))  # # 指向的是同一个对象
    a=10
    print(id(a))  # # 指向的是不同的对象

a = 1
print(id(a)) 
change(a)

# 传可变对象实例
# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print("函数外取值: ", mylist)

