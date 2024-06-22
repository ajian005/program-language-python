
s = 'Hello, Runoob'
str(s)
repr(s)
str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为: ' + repr(x) + ', y 的值为: ' + repr(y) + '...'
print(s)

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))

# 这里有两种方式输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))

print('{1} 和 {0}'.format('Google', 'Runoob'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
#将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 ** 来实现相同的功能：
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
import math
print("常量 PI 的值近似为: %5.3f。" % math.pi)


# 读取键盘输入
str = input("请输入：")
print("你输入的内容是:", str)

# 读和写文件

# 打开一个文件
f = open("foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

# f.read()
# 打开一个文件
f = open("foo.txt", "r")
str = f.read()
print(str)

# 关闭打开的文件
f.close()

'''
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
'''
# 打开一个文件
f = open("foo.txt", "r")
str = f.readline()
print(str)
# 关闭打开的文件
f.close()

'''
f.readlines()
f.readlines() 将返回该文件中包含的所有行。

如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
'''
# # 打开一个文件
f = open("foo.txt", "r")
str = f.readlines()
print(str)

# 关闭打开的文件
f.close()


'''
另一种方式是迭代一个文件对象然后读取每行:
'''
print("=======================")
# 打开一个文件
f = open("foo.txt", "r")
for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

'''
 f.write()
 f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
'''
f = open("foo.txt", "w")
num = f.write( "Python 是一个非常好的语言w。\n是的，的确非常好!!\n" )
print("写入 %d 个字节" % num)

# 关闭打开的文件
f.close()


# 打开一个文件
f = open("foo.txt", "w")
values = "('www.runoob.com', 14)"
#s = ''.join(str(values))
f.write(values)

# 关闭打开的文件
f.close()

# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# file: 类文件对象，有read()和readline()接口。
import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None  }

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


import pprint, pickle
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()