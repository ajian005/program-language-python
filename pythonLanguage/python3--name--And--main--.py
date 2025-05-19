'''
    Python __name__ 与 __main__
    平时我们经常会看到这样的 Python 代码：

    if __name__ == "__main__":
        main() 
    在 Python 中，__name__ 和 __main__ 是两个与模块和脚本执行相关的特殊变量。

    __name__ 和 __main__ 通常用于控制代码的执行方式，尤其是在模块既可以作为独立脚本运行，也可以被其他模块导入时。

    1. __name__ 变量
    __name__ 是一个内置变量，用于表示当前模块的名称。

    __name__ 的值取决于模块是如何被使用的：

    当模块作为主程序运行时：__name__ 的值被设置为 "__main__"。

    当模块被导入时：__name__ 的值被设置为模块的文件名（不包括 .py 扩展名）。

    假设有一个 module.py 文件：

    print(f"模块的 __name__ 值: {__name__}")
    输出会是：
    模块的 __name__ 值: __main__
    2. __main__ 的含义
    __main__ 是一个特殊的字符串，用于表示当前模块是作为主程序运行的。

    __main__ 通常与 __name__ 变量一起使用，以确定模块是被导入还是作为独立脚本运行。

    3. 使用 if __name__ == "__main__": 的常见模式
    在 Python 中，常见的做法是在模块的末尾添加以下代码块：

    实例
    if __name__ == "__main__":
        # 这里的代码只有在模块作为主程序运行时才会执行
        main()
    这种模式允许模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。
'''


def main2():
    print("Hello, World!")
# This code is executed when the script is run directly


if __name__ == "__main__":
    print(__name__)

    # main()
    print("This script is being run directly")