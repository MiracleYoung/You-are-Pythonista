#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/25 20:13

__author__ = 'Uforever I'

# 参考了mona的作业
# 通过字典实现0~9的字符映射
d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# 实现字符串型的int转换
# 输入字符串型整数
s1 = '20190525'

# 整型初始化
sInt = 0

for x in range(len(s1)):
    sInt += d[s1[len(s1)-x-1]] * (10**x)
print(sInt)

# 实现字符串型的float转换
# 输入字符串型浮点数
s2 = '2019.0525'

# 浮点型初始化
sFlt = 0.0

f1, f2 = s2.split('.')

for x in range(len(f1)):
    sFlt += d[f1[len(f1)-x-1]] * (10**x)

for x in range(len(f2)):
    sFlt += d[f2[x]] * (10 ** (-x-1))

print(sFlt)