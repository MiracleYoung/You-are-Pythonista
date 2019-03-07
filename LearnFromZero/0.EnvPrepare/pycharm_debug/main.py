#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/5 6:49 AM

__author__ = 'Miracle'

from xxmodule import add, is_digit, get_xnum, get_xwords


def main():
    num1 = get_xnum()
    word = get_xwords()
    num2 = word if is_digit(word) else -1
    ret = add(num1, num2)
    print(ret)


if __name__ == '__main__':
    main()
