#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Guan
@Github: https://github.com/youguanxinqing
@Date: 2019-04-27 21:22:01
@LastEditTime: 2019-04-29 01:39:46
'''

def get_geometrically(n):
    a, q = 2, 3

    if n == 1:
        return a

    return a*q**(n-1) + get_geometrically(n-1)


if __name__ == "__main__":
    print(get_geometrically(4))