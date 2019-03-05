#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/5 6:50 AM

__author__ = 'Miracle'

import random
import string


def add(a, b):
    '''
    累加器，计算a + b 的结果
    '''
    return a + b


def is_digit(s):
    '''
    判断是否为数字
    '''
    return isinstance(s, (int, float))


def get_xnum():
    '''
    获取一个随机0-9数字
    '''
    return random.randint(0, 9)


def get_xwords():
    '''
    获取一个随机英文字母或数字
    '''
    return random.choice(string.ascii_letters + string.digits)
