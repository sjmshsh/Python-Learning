from pandas import DataFrame
from pandas import Series

df = DataFrame({'age': Series([21, 22, 23]),
'name': Series(['Yubg', 'John', 'Jim'])},
    index=[0, 1, 2])

print(df)
