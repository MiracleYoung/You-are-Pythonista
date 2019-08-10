# 矩阵转置

# 定义一个m x n的矩阵，m行n列
lst = [[1, 2, 3], [4, 5 ,6]]
print('矩阵转置前：' + str(lst) + '\n')

# 转置
# 定义一个新列表存储转置后的矩阵
ret = []
# 获取行数m
m = len(lst)
# 获取列数n
n = len(lst[0])
# 将 m x n 变为 n x m
for _ in range(n):
    ret.append([])

# 填入相应的元素
for x in range(m):
    for j  in range(n):
        ret[j].append(lst[x][j])

print('矩阵转置后：' + str(ret))