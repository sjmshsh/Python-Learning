from pandas import DataFrame
from pandas import Series

df = DataFrame({'age': Series([21, 22, 23]),
'name': Series(['Yubg', 'John', 'Jim'])},
    index=[0, 1, 2])

print(df)
print()
A=df['age']
print(A)
print()

B=df[1:2]
print(B)

# 获取第0行到第1行（不含）与第0列到2列（不含）交叉值
C=df.iloc[0:1, 0:2]
D=df.at(0, 'name') # 获取第0行与name列的交叉值

print(C)
