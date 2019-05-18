#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/5/814:42

__author__ = 'aaronwa'

def geometricprogression(a, q, n):
    if q == 1:
        sn = a * n
    else:
        sn = int(a*(q**n-1)/(q-1))
    print (sn)
geometricprogression(2, 3, 4)