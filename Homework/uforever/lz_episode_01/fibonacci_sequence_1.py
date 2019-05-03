#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/5/3 下午3:20

__author__ = 'Uforever I'


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def get_fib_list(n):
    return [fib(i) for i in range(1, n + 1)]

print('Please input n:')
m = int(input())
l = fib(m)
s = get_fib_list(m)
print("The last num:%d" % l)
print("The num list:",end='')
print(s)

if __name__ == "__main__":
    print('For example: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55，...')
#    print(get_fib_list(10))
#如果get_fib_list()出错，那么就可能导致一些列的问题。
#所以应该默认输出一串（10个）数（dict字典）作为标准Fibonacci sequence进行参照和便于校对。