#!/usr/bin/env python
# encoding: utf-8
from collections import defaultdict

def triangles(n):
    yanghui = [[]] * n
    for row in range(len(yanghui)):
        yanghui[row] = [None] * (row + 1)
        for col in range(len(yanghui[row])):
            if col == 0 or col == row:
                yanghui[row][col] = 1
            else:
                yanghui[row][col] = yanghui[row - 1][col] + yanghui[row - 1][col - 1]
    return yanghui
