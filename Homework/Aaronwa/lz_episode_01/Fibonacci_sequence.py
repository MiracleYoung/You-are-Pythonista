#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/5/816:42

__author__ = 'aaronwa'

list=[]
for i in range(10):
    if i==0 or i==1: #第一和第二项均为1
        list.append(1)
    else:
        list.append(list[i-2]+list[i-1]) # 从第三项开始每项值是前两项的和
print(list)
