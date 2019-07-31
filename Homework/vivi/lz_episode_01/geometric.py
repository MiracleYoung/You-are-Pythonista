#!/usr/bin/env python
# encoding: utf-8


def geometric_series(a, b, n):
    if b == 1:
        series = a * n
    else:
        series = a * (b ** n - 1) / (b - 1)
    return series