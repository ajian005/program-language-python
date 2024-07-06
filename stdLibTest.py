'''
    Python3 标准库概览
'''
'''
    操作系统接口
'''
import os
# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("当前目录下的文件:", files)

# print("dir(os):", dir(os))

# print("help(os):", help(os))

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil

print("shutil.copyfile():", shutil.copyfile("test.txt", "test_copy.txt"))

'''
文件通配符
glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
'''
import glob
out = glob.glob('*.py')
print("glob.glob('*.py')", out)


'''
错误输出重定向和程序终止
'''
import sys
sys.stderr.write('Warning, log file not found starting a new one\n')

# 字符串正则匹配
import re
out2 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print("out2=", out2)
out3 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print("out3=", out3)


# 数学
import math
print("math.sqrt(100)=", math.sqrt(100))
print("math.log(100)=", math.log(100))
print("math.exp(1)=", math.exp(1))
print("math.pi=", math.pi)
print("math.sin(math.pi/4)=", math.sin(math.pi/4))
print("math.cos(math.pi/4)=", math.cos(math.pi/4))


# random 提供了生成随机数的工具。
import random
out5 = random.choice(['apple', 'pear', 'banana'])
print("out5=", out5)
out6 = random.sample(range(100), 10)   # sampling without replacement
print("out6=", out6)
out7 = random.random()    # random float
print("out7=", out7)
out8 = random.randrange(6)    # random integer chosen from range(6)
print("out8=", out8)


# 访问 互联网
'''


from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)

'''

# 日期和时间
import datetime
#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45

# 导入了 datetime 模块中的 date 类
from datetime import date
now = date.today()    # 当前日期
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# 创建了一个表示生日的日期对象
birthday = date(1964, 7, 31)
age = now - birthday   # 计算两个日期之间的时间差
age.days             # 变量age的days属性，表示时间差的天数
print(age.days)

# 数据压缩
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# 性能度量
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试



# 测试模块
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests

