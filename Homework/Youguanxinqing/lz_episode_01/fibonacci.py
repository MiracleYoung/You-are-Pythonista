#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Guan
@Github: https://github.com/youguanxinqing
@Date: 2019-04-27 21:22:49
@LastEditTime: 2019-04-27 21:42:37
'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def get_fib_squence(n):
    return [fib(i) for i in range(1, n+1)]
    

if __name__ == "__main__":
    print(get_fib_squence(10))