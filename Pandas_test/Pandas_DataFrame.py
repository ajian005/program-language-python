'''
Pandas 数据结构 - DataFrame
    DataFrame 是 Pandas 中的另一个核心数据结构，用于表示二维表格型数据。
    DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
    DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
    DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。
'''
import pandas as pd

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)