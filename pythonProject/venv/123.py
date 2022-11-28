import numpy as np #矩阵加法
a = np.array([1,1,1,1])
b = np.array([[1],[1],[1],[1]])# 这叫python的广播机制

c = np.array([[1,1,1,1]])
print(c+b)