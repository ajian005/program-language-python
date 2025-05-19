'''
Python 装饰器

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

# 以下是一个简单的装饰器示例，它会在函数执行前后打印日志：
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()


'''
带参数的装饰器
如果原函数需要参数，可以在装饰器的 wrapper 函数中传递参数：
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        result = func(*args, **kwargs)
        print("在原函数之后执行")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 输出: 在原函数之前执行 Hello, Alice! 在原函数之后执行

#装饰器本身也可以接受参数，此时需要额外定义一个外层函数：
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 输出: Hello, Alice! Hello, Alice! Hello, Alice!


"""
类装饰器
除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数。
"""
def my_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def display(self):
            print("在原函数之前执行")
            self.wrapped.display()
            print("在原函数之后执行")
    return Wrapper

@my_decorator
class MyClass:
    def display(self):
        print("Hello, World!")

obj = MyClass()
obj.display()  # 输出: 在原函数之前执行 Hello, World! 在原函数之后执行

'''
内置装饰器
Python 提供了一些内置的装饰器，例如：

@staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。

@classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）。

@property: 将方法转换为属性，使其可以像属性一样访问。

'''
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)

'''
多个装饰器的堆叠
你可以将多个装饰器堆叠在一起，它们会按照从下到上的顺序依次应用。
'''
def decorator1(func):
    def wrapper():
        print("Decorator 1 before")
        func()
        print("Decorator 1 after")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 before")
        func()
        print("Decorator 2 after")
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, World!")

say_hello()  # 输出: Decorator 1 before Decorator 2 before Hello, World! Decorator 2 after Decorator 1 after