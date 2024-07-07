'''
    NumPy 字符串函数
    以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。 
    它们基于 Python 内置库中的标准字符串函数。
'''
import numpy as np

# numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))

# numpy.char.multiply() 函数执行多重连接。
print (np.char.multiply('Runoob ',3))

# numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))

# numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：
print (np.char.capitalize('runoob'))

# numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写：
print (np.char.title('hello world'))

# numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower。
#操作数组
print (np.char.lower(['RUNOOB','GOOGLE']))
# 操作字符串
print (np.char.lower('RUNOOB'))

# numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper。
#操作数组
print (np.char.upper(['runoob','google']))
# 操作字符串
print (np.char.upper('runoob'))

# numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))

# numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。
# 换行符 \n
print (np.char.splitlines('i\nlike runoob?')) 
print (np.char.splitlines('i\rlike runoob?'))

# numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
# 移除字符串头尾的 a 字符
print (np.char.strip('ashok arunooba','a'))
 
# 移除数组元素头尾的 a 字符
print (np.char.strip(['arunooba','admin','java'],'a'))

# numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
# 操作字符串
print (np.char.join(':','runoob'))
 
# 指定多个分隔符操作数组元素
print (np.char.join([':','-'],['runoob','google']))

# numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
print (np.char.replace ('i like runoob', 'oo', 'cc'))

# numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
a = np.char.encode('runoob', 'cp500') 
print (a)

# numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
a = np.char.encode('runoob', 'cp500') 
print (a)
print (np.char.decode(a,'cp500'))


