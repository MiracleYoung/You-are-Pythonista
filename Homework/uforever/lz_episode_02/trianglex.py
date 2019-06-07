#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/25 20:08

__author__ = 'Uforever I'


n = 12
k = 8

def Ta(num = 10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j==0 else LL[i-1][j-1])+ (0 if j==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL

for x in Ta(n):
    print(x)

print(x[k-1])