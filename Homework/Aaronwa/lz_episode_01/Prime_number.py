#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/5/722:01

__author__ = 'aaronwa'

list=[]
i=2
for i in range(2,1000000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        list.append(i)
print(list)
