counter = 100       # 整型变量
miles   = 1000.0    # 浮点型变量
name    = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

a, b,c,d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d));
a = 111
print(isinstance(a, int))

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))

print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(issubclass(bool, int))
print(True == 1)
print(False == 0)
print(True + 1)
print(False + 1)
print(1 is True)
print(0 is False)


# 数值运算
print("5 + 4 =", 5 + 4)  # 加法  9
print("4.3 - 2 =", 4.3 - 2)  # 减法  2.3
print("2 * 4 =", 2 * 4)  # 乘法  8
print("16 / 4 =", 16 / 4)   # 除法  4.0
print("16.0 / 4 =", 16.0 / 4)   # 除法  4.0
print("16 // 4 =", 16 // 4)   # 除法  4
print("16 % 3 =", 16 % 3)   # 取模  1
print("-16 // 4 =", -16 // 4)  # 除法  -4
print("2 ** 5 =", 2 ** 5 )   # 乘方

# String（字符串）
str = 'Runoob'  # 定义一个字符串变量

print(str)   # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（包含第五个字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起

# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')       # 输出 Ru\noob
print(r'Ru\noob')      # 输出 Ru\noob

word = 'Python'
print(word[0],  word[5])
print(word[-1], word[-6])

# List（列表） List（列表） 是 Python 中使用最频繁的数据类型。
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 创建一个列表
tinylist = [123, 'runoob']   # 创建另一个列表

print (list)             # 输出完整列表
print (list[0])          # 输出列表第一个元素
print (list[1:3])        # 输出第二个至第三个元素
print (list[2:])         # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)     # 输出列表两次
print (list + tinylist)  # 打印组合的列表



def reverseWords(s):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = s.split(" ")
    # 翻转字符串
    inputWords = inputWords[-1: :-1]
    # 将单词拼接成字符串
    output = " ".join(inputWords)
    return output

if __name__ == '__main__':
    input = "I like runoob Python"
    rw = reverseWords(input)
    print(rw)

# Tuple（元组）
tuple = ( 'abcd', 786, 2.23, 'runoob', 70.2 )
tinytuple = (123, 'runoob')

print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)      # 输出元组两次
print(tuple + tinytuple) # 打印组合的元组



# Set（集合）
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print("Runoob 在集合中")
else :
    print("Runoob 不在集合中")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)  # a 和 b 的差集
print(a|b)  # a 和 b 的并集
print(a&b)  # a 和 b 的交集
print(a^b)  # a 和 b 中不同时存在的元素


# Dictionary（字典）
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code':6734, 'site': 'www.runoob.com'}
print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict.keys())   # 输出所有的键
print(tinydict.values()) # 输出所有的值
print(tinydict)          # 输出完整的字典
