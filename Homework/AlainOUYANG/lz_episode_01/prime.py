#!/usr/bin/env pipenv-shebang
# -*- coding: utf-8 -*-

'''
@Author: AlainOUYANG
@Date: 2019-10-16 16:45:49
@LastEditors: AlainOUYANG
@LastEditTime: 2019-10-17 20:01:29
@Description: get_prime
'''
from math import sqrt


def get_prime(n):
    return filter(lambda x: not [x%i for i in range(2, int(sqrt(x)+1)) if x%i == 0], range(2, n+1))


def main():
    for each in get_prime(20):
        print(each)

if __name__ == "__main__":
    main()
