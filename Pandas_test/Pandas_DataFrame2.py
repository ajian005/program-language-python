import pandas as pd

#  创建一个简单的 DataFrame
data = {'Name':['Google', 'Runoob', 'Tabao'], 'Age':[25, 30, 35]}
df = pd.DataFrame(data)

# 查看 DataFrame
print(df)

# 创建两个Series对象
series_apples = pd.Series([1, 3, 7, 4])
series_bananas = pd.Series([2, 6, 3, 5])

# 将两个Series对象相加，得到DataFrame，并指定列名
df = pd.DataFrame({'Apples': series_apples, 'Bananas': series_bananas})

# 显示DataFrame
print(df)