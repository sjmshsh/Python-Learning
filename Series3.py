from pandas import Series

# 可以混合定义一个序列
x = Series(['a', True, 1], index=['first', 'second', 'third'])

# 根据index删除
x.drop('first')

# 根据位置删除
x.drop(x.index[0])

x[2 != x.values] # 根据值删除，显示不等于2的值的序列，也就是删除2，返回新序列
