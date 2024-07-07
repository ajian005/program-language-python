# 创建空字典
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:", len(emptyDict))
 
# 查看类型
print(type(emptyDict))

# 访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
# 如果用字典里没有的键访问数据，会输出错误如
# print ("tinydict['Alice']: ", tinydict['Alice'])

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

# 删除字典元素
'''
能删单一的元素也能清空字典，清空只需一项操作。
显式删除一个字典用del命令，如下实例：
'''
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
# print ("tinydict['Age']: ", tinydict['Age'])
# print ("tinydict['School']: ", tinydict['School'])