from pandas import Series

# 可以混合定义一个序列
x = Series(['a', True, 1], index=['first', 'second', 'third'])

# 访问
print(x[1]) # 根据位置访问，不能越界访问
print(x['second']) # 根据index访问
