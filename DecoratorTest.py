'''
装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
装饰器的语法使用 @decorator_name 来应用在函数或方法上。
Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

装饰器的应用场景：
日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
性能分析: 可以使用装饰器来测量函数的执行时间。
权限控制: 装饰器可用于限制对某些函数的访问权限。
缓存: 装饰器可用于实现函数结果的缓存，以提高性能。
'''

'''
带参数的装饰器
装饰器函数也可以接受参数，例如：
'''
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


'''
类装饰器
除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参
'''
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        print("Before function called")
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        print("Function called")
        return result
    

@DecoratorClass
def my_function():
    print("Hello, world!")


my_function()