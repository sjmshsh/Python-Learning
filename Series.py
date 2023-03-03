from pandas import Series
A = Series([1, 2, 3]) #定义系列的时候，数据类型不限
print(A)

B = Series([1, 2, 3], index=[1, 2, 3]) # 可以自定义索引，如：123
print(B)

C = Series([1, 2, 3], index=['A', 'B', 'C'])
print(C)
