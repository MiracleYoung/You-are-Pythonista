#!/usr/bin/env python
# encoding: utf-8
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def prime_list(n):
    L = []
    for i in range(1, n):
        if is_prime(i):
            L.append(i)
    return L
