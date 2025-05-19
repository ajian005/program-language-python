'''
    假设我们有一个名为 example.py 的模块：
'''
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("example.py 模块作为主程序运行")
    greet()
else:
    print("example.py 模块被导入")
    print("模块的 __name__ 值:", __name__)