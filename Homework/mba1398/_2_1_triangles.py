# -*- coding: utf-8 -*-
"""
author: mba1398
date: 20190517
task: 杨辉三角
"""


def triangles(n):
    # yield生成器，返回杨辉三角
    L = [1]
    S = []
    for i in range(n):
        yield L
        L = [1] + S + [1]
        S = []
        for j in range(len(L)-1):
            S.append(L[j] + L[j+1])


def nr_kc_triangles(n, k):
    # 将杨辉三角转换为list,最后一个元素即为杨辉三角第n行，其k-1个即为k-1列
    # 打印杨辉三角n行k列元素值
    print(list(triangles(n))[-1][k-1])


nr_kc_triangles(4, 2)
