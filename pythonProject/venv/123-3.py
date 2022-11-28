import numpy as np
matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
p1 = np.delete(matrix, 1, 0) # 第0维度(行)第1行被删除(初始行为0行)
print('>>>>p1>>>>\n',p1)
p2 = np.delete(matrix, 1, 1) # 第1维度(列)第1行被删除
print('>>>>p2>>>>\n',p2)
p3 = np.delete(matrix, 1) # 拉平后删除第1个元素(初始为第0个)
print('>>>>p3>>>>\n',p3)
p4 = np.delete(matrix, [0,1], 1) # 第1维度(列)第0、1行被删除
print('>>>>p4>>>>\n',p4)
