"""
Python3 错误和异常
    作为 Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
    Python 有两种错误很容易辨认：语法错误和异常。
    Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
"""

'''
以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。
'''
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("Oops! 不是一个有效的数字。")
        break