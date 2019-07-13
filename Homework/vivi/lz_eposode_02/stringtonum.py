#!/usr/bin/env python
# encoding: utf-8


def string_to_int(strs):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9}
    new_str = 0
    for bit, number in enumerate(strs, start=1):
        lenth = len(strs)
        new_str += d[number] * (10 ** (lenth - bit))
    return new_str


def string_to_float(strs):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9}
    new_str = 0
    num_left, num_right = strs.split('.')
    for bit, number in enumerate(num_left, start=1):
        lenth = len(num_left)
        new_str += d[number] * (10 ** (lenth - bit))

    for bit, number in enumerate(num_right, start=1):
        new_str += d[number] / (10 ** bit)
    return new_str
