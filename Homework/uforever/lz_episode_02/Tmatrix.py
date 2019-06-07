#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/25 19:54

__author__ = 'Uforever I'


lst = [(1, 4, 7, 0, 3), (2, 5, 8, 1, 4), (3, 6, 9, 2, 5), (4, 7, 0, 3, 1)]  # 源矩阵

lst_nT = []  # 转置矩阵初始化
# 转置
for n in range(0, len(lst[0])):
    lst_T = []
    for t in range(0, len(lst)):
        lst_T.append(lst[t][n])
    lst_nT.append((lst_T))

# 打印转置矩阵
for i in range(len(lst_nT)):
    for x in lst_nT[i]:
        print(x, end="  ")
    print()

# 打印分隔线
print("=" * (len(lst[0]) + 2 * (len(lst[0]) - 1)))

# 打印源矩阵
for i in range(len(lst)):
    for x in lst[i]:
        print(x, end="  ")
    print()