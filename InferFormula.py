# 列表推导式 
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)

# 计算 30 以内可以被 3 整除的整数:
multiples = [x for x in range(30) if x%3 == 0]
print(multiples)


# 字典推导式
# 使用字符串及其长度创建字典：
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = { x: x**2 for x in (2, 4, 6) }
print(dic)
print(type(dic))


# 集合推导式
'''
    计算数字 1,2,3 的平方数：
'''
setnew = {i**2 for i in (1,2,3)}
print(setnew)

'''
    判断不是 abc 的字母并输出：
'''
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(type(a))


# 元组推导式（生成器表达式）
a = (x for x in range(1,10))
print(a)
print(type(a))
print(tuple(a))