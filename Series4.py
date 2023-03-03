from pandas import Series

# 可以混合定义一个序列
x = Series(['a', True, 1], index=['first', 'second', 'third'])

# 可将字典转化为Series
s=Series({'a': 1, 'b': 2, 'c': 3})

# 重排序
# 默认为升序（True）
x.sort_index(ascending=False)
print(x)

