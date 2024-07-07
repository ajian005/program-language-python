'''
    列表Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
    以下是 Python 中列表的方法：
'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, 999)
a.insert(2, -1)
a.append(333)
print(a)
a.index(333)
a.remove(333)
print(a)
a.reverse()
a.sort()

print(a)
