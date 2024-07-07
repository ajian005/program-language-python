
class MyClass:
    """一个简单的类实例"""
    def __init__(self):
        self.data = []
        print("MyClass 类被实例化")
    i = 12345
    def f(self):
        return 'hello world'
    
# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为: ", x.i)
print("MyClass 类的方法 f 输出为: ", x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5

'''
self 代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
'''
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

'''
self 不是关键字，可以用任意变量名，但是最好还是用 self 习惯一些。
'''
class Test2:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t = Test2()
t.prt()

'''
    在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。

当你定义一个类，并在类中定义方法时，第一个参数通常被命名为 self，尽管你可以使用其他名称，但强烈建议使用 self，以保持代码的一致性和可读性。
'''
class MyClass2:
    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data)

# 创建一个类的实例
obj = MyClass2(10)

# 调用实例的方法
obj.display()  # 输出：10

'''
    类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    #定义一般方法
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
        
# 实例化类
p = people('张三',20,30)
p.speak()

'''
    继承
'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁，体重 %d 斤。"%(self.name,self.age,self.__weight))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('ken', 10, 60, 3)
s.speak()

'''
    多继承
    Python同样有限的支持多继承形式。多继承的类定义形如下例:
'''
#另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t

    def speak(self):  
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" %(self.name,self.topic))

#多继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim", 25, 80, 4, "Python")
test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法

'''
    方法重写
    如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
'''
class Parent:         # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent): # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()          # 子类实例 
c.myMethod()        # 子类调用重写方法
super(Child,c).myMethod() # 用子类对象调用父类已被覆盖的方法