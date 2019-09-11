#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/8/13 下午10:20
# @Author  : MiracleYoung
# @File    : lover7c.py

import seaborn as sns
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# Define Data
data = np.zeros([62, 65], dtype="float")

# Begin to Draw
POS_VALUE = 1
NEG_VALUE = -1

# 绘制第一个 "M"
data[1:31, 1] = POS_VALUE

for i in range(1, 11):
    data[i, i] = POS_VALUE
for i in range(11, 21):
    data[21 - i, i] = POS_VALUE

data[1:31, 20] = POS_VALUE
data[2, 31:34] = POS_VALUE

# 绘制 "O"
for i in range(0, 7):
    data[i + 2, 31 - i] = POS_VALUE

data[8:25, 25] = POS_VALUE
for i in range(25, 32):
    data[i, i] = POS_VALUE

data[31, 31:34] = POS_VALUE
for i in range(34, 41):
    data[65 - i, i] = POS_VALUE

data[8:25, 40] = POS_VALUE
for i in range(0, 7):
    data[i + 2, i + 34] = POS_VALUE

# 绘制第二个 “M”
data[1:31, 44] = POS_VALUE
for i in range(1, 11):
    data[i, 43 + i] = POS_VALUE
for i in range(11, 21):
    data[21 - i, 43 + i] = POS_VALUE
data[1:31, 63] = POS_VALUE

# 绘制 “心”
for i in range(37, 44):
    data[i, i - 11] = NEG_VALUE
for i in range(37, 44):
    data[i, 64 - i] = NEG_VALUE
for i in range(44, 57):
    data[i, i - 23] = NEG_VALUE
    data[i, i - 22] = NEG_VALUE
    data[i - 1, i - 22] = NEG_VALUE
    data[i - 1, i - 21] = NEG_VALUE
    data[i - 2, i - 21] = NEG_VALUE
    data[i - 2, i - 20] = NEG_VALUE
    data[i - 3, i - 20] = NEG_VALUE
    data[i - 3, i - 19] = NEG_VALUE
    data[i - 4, i - 19] = NEG_VALUE
    data[i - 4, i - 18] = NEG_VALUE
    data[i - 5, i - 18] = NEG_VALUE
    data[i - 5, i - 17] = NEG_VALUE

for i in range(44, 57):
    data[i, 89 - i] = NEG_VALUE
    data[i, 88 - i] = NEG_VALUE
    data[i - 1, 88 - i] = NEG_VALUE
    data[i - 1, 87 - i] = NEG_VALUE
    data[i - 2, 87 - i] = NEG_VALUE
    data[i - 2, 86 - i] = NEG_VALUE
    data[i - 3, 86 - i] = NEG_VALUE
    data[i - 3, 85 - i] = NEG_VALUE
    data[i - 4, 85 - i] = NEG_VALUE
    data[i - 4, 84 - i] = NEG_VALUE
    data[i - 5, 84 - i] = NEG_VALUE
    data[i - 5, 83 - i] = NEG_VALUE
    data[i - 6, 83 - i] = NEG_VALUE

for i in range(37, 44):
    data[i, i + 2] = NEG_VALUE
for i in range(37, 45):
    data[i, 77 - i] = NEG_VALUE

# 绘制 “I”
data[33:59, 11] = NEG_VALUE
data[33, 9:14] = NEG_VALUE
data[59, 9:14] = NEG_VALUE

# 绘制 “U”
data[33:53, 47] = NEG_VALUE
for i in range(53, 60):
    data[i, i - 6] = NEG_VALUE

data[59, 53:56] = NEG_VALUE

for i in range(0, 6):
    data[59 - i, i + 55] = NEG_VALUE

data[33:54, 61] = NEG_VALUE

# SHOW THE MAP
plt.figure(figsize=(15, 10))
sns.heatmap(-data, xticklabels=False, yticklabels=False)
show()