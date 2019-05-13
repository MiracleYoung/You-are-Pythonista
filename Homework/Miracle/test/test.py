#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/9 9:29 PM

__author__ = 'Miracle'


list1 = [1,2,3,4,5,6]

def sum1(list1, sm=0):
    lst = list1[:]
    if len(lst):
        sm += lst.pop()
        return sum1(lst, sm)
    else:
        return sm


print(sum1(list1))