"""
Python3 数据结构

本章节我们主要结合前面所学的知识点来介绍Python数据结构。

列表
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

以下是 Python 中列表的方法：

方法	描述
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。
下面示例演示了列表的大部分方法：
"""
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)


"""
将列表当做栈使用
    在 Python 中，可以使用列表（list）来实现栈的功能。栈是一种后进先出（LIFO, Last-In-First-Out）数据结构，意味着最后添加的元素最先被移除。列表提供了一些方法，使其非常适合用于栈操作，特别是 append() 和 pop() 方法。

    用 append() 方法可以把一个元素添加到栈顶，用不指定索引的 pop() 方法可以把一个元素从栈顶释放出来。

    栈操作
    压入（Push）: 将一个元素添加到栈的顶端。
    弹出（Pop）: 移除并返回栈顶元素。
    查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
    检查是否为空（IsEmpty）: 检查栈是否为空。
    获取栈的大小（Size）: 获取栈中元素的数量。
"""

'''
    以下是如何在 Python 中使用列表实现这些操作的详细说明：

    1、创建一个空栈
    实例
    stack = []

    2、压入（Push）操作
    使用 append() 方法将元素添加到栈的顶端：

    实例
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack)  # 输出: [1, 2, 3]

    3、弹出（Pop）操作
    使用 pop() 方法移除并返回栈顶元素：

    实例
    top_element = stack.pop()
    print(top_element)  # 输出: 3
    print(stack)        # 输出: [1, 2]

    4、查看栈顶元素（Peek/Top）
    直接访问列表的最后一个元素（不移除）：

    实例
    top_element = stack[-1]
    print(top_element)  # 输出: 2

    5、检查是否为空（IsEmpty）
    检查列表是否为空：

    实例
    is_empty = len(stack) == 0
    print(is_empty)  # 输出: False

    6、获取栈的大小（Size）
    使用 len() 函数获取栈中元素的数量：

    实例
    size = len(stack)
    print(size)  # 输出: 2
'''

"""
实例
    以下是一个完整的实例，展示了如何使用上述操作来实现一个简单的栈：
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3

print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2


"""
将列表当作队列使用
    在 Python 中，列表（list）可以用作队列（queue），但由于列表的特点，直接使用列表来实现队列并不是最优的选择。

    队列是一种先进先出（FIFO, First-In-First-Out）的数据结构，意味着最早添加的元素最先被移除。

    使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)。为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素。

    使用 collections.deque 实现队列
    collections.deque 是 Python 标准库的一部分，非常适合用于实现队列。

    以下是使用 deque 实现队列的示例：
"""
from collections import deque

# 创建一个空队列
queue = deque()

# 向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')

print("队列状态:", queue)  # 输出: 队列状态: deque(['a', 'b', 'c'])

# 从队首移除元素
first_element = queue.popleft()
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)            # 输出: 队列状态: deque(['b', 'c'])

# 查看队首元素（不移除）
front_element = queue[0]
print("队首元素:", front_element)    # 输出: 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)     # 输出: 队列是否为空: False

# 获取队列大小
size = len(queue)
print("队列大小:", size)            # 输出: 队列大小: 2

'''
使用列表实现队列

    虽然 deque更高效，但如果坚持使用列表来实现队列，也可以这么做。以下是如何使用列表实现队列的示例：

    1. 创建队列

    实例
    queue = []
    2. 向队尾添加元素

    使用 append() 方法将元素添加到队尾：

    实例
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print("队列状态:", queue)  # 输出: 队列状态: ['a', 'b', 'c']
    3. 从队首移除元素

    使用 pop(0) 方法从队首移除元素：

    实例
    first_element = queue.pop(0)
    print("移除的元素:", first_element)  # 输出: 移除的元素: a
    print("队列状态:", queue)            # 输出: 队列状态: ['b', 'c']
    4. 查看队首元素（不移除）

    直接访问列表的第一个元素：

    实例
    front_element = queue[0]
    print("队首元素:", front_element)    # 输出: 队首元素: b
    5. 检查队列是否为空

    检查列表是否为空：

    实例
    is_empty = len(queue) == 0
    print("队列是否为空:", is_empty)     # 输出: 队列是否为空: False
    6. 获取队列大小

    使用 len() 函数获取队列的大小：

    实例
    size = len(queue)
    print("队列大小:", size)            # 输出: 队列大小: 2
    实例（使用列表实现队列）
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:   
            raise IndexError("dequeue from empty queue")
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
# 使用示例
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("队首元素:", queue.peek())    # 输出: 队首元素: a
print("队列大小:", queue.size())    # 输出: 队列大小: 3

print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False
print("队列大小:", queue.size())    # 输出: 队列大小: 2

"""
虽然可以使用列表来实现队列，但使用 collections.deque 会更高效和简洁。它提供了 O(1) 时间复杂度的添加和删除操作，非常适合队列这种数据结构。
"""

'''
列表推导式
    列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
    每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
    
'''
# 这里我们将列表中每个数值乘三，获得一个新的列表：
vec = [2, 4, 6]
print([3*x for x in vec])  # 输出: [6, 12, 18]

# 这里我们将列表中每个数值乘三，获得一个新的列表：
print([[x, x**2] for x in vec])

# 这里我们对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# 我们可以用 if 子句作为过滤器：
print(3*x for x in vec if x > 2)
print(3*x for x in vec if x > 3)

# 以下是一些关于循环和其它技巧的演示：
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

# 列表推导式可以使用复杂表达式或嵌套函数：
print([str(round(355/113, i)) for i in range(1, 6)])

"""
嵌套列表解析
    Python的列表还可以嵌套。

    以下实例展示了3X4的矩阵列表：
"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
# 以下实例将3X4的矩阵列表转换为4X3列表：
print([[row[i] for row in matrix] for i in range(4)])

"""
del 语句
   使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
   例如
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)  # 输出: [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)  # 输出: [1, 66.25, 1234.5]
del a[:]
print(a)

"""
元组和序列
    元组由若干逗号分隔的值组成，例如：
"""
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1,2,3,4,5)
print(u)
"""
如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
"""

"""
集合
    集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
    可以用大括号({})创建集合。
    注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
    以下是一个简单的演示：
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 的差集

# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

"""
字典
    另一个非常有用的 Python 内建数据类型是字典。

    序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。

    理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。

    一对大括号创建一个空的字典：{}。

    这是一个字典运用的简单例子：
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
list(tel.keys())
sorted(tel.keys())
print('guido' in tel)
print('jack' not in tel)

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# 此外，字典推导可以用来创建任意键和值的表达式词典：
print({x: x**2 for x in (2, 4, 6)})

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
print(dict(sape=4139, guido=4127, jack=4098))

"""
遍历技巧
    在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
