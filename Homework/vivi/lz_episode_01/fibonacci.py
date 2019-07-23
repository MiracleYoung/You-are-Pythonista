#!/usr/bin/env python
# encoding: utf-8


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return (fib(n - 2) + fib(n - 1))


def fib_seq(n):
    L = []
    i = 1
    while i <= n:
        L.append(fib(i))
        i += 1
    return L

