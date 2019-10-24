#!/usr/bin/env pipenv-shebang
# -*- coding: utf-8 -*-

'''
@Author: AlainOUYANG
@Date: 2019-10-16 16:52:17
@LastEditors: AlainOUYANG
@LastEditTime: 2019-10-17 20:25:34
@Description: fibonacci
'''

def fibonacci_item(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_item(n - 1) + fibonacci_item(n - 2)


def fibonacci_list(n):
    lst = []
    for i in range(1, n+1):
        lst.append(fibonacci_item(i))
    return lst


def main():
    print(fibonacci_list(20))


if __name__ == "__main__":
    main()