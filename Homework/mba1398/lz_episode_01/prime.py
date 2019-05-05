#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:mba1398
@time:20190504
@task: find prime numbers
"""
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    return list(filter(is_prime, range(2, n+1)))

if __name__ == "__main__":
    prime_list = find_prime(1000000)
    print(prime_list)
