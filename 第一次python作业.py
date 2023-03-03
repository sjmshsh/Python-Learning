# 构造一个由4个数值大小为0~100范围内的随机数生成的 series R；
from pandas import Series
import random

R = Series([random.randint(0, 100) for i in range(4)])
print(R)
