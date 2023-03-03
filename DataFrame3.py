from pandas import DataFrame
from pandas import Series

df = DataFrame({'age': Series([21, 22, 23]),
'name': Series(['Yubg', 'John', 'Jim'])},
    index=[0, 1, 2])

# 修改列名
df.columns=['age2', 'name2']

# 修改行索引
df.index=range(1, 4)

# 根据行索引删除
df.drop(1, axis=0) #aixs=0表示是行轴

# 根据列名进行删除
df.drop('age2', axis=1) # axis=1表示列轴，不可省略

# 第二种删除列的方式
del df['age2']

# 增加列
df['newColumn'] = [2, 4, 6]

# 增加行，注意，这种方法效率很低
df.loc[len(df)] = [24, 'kenken']

# 增加行的办法可以通过合并（append）两个datafram来解决
df=DataFrame([[1, 2], [3, 4]], columns=list('AB'))
