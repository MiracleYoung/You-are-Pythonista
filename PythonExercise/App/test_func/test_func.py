#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/8/21 下午9:56
# @Author  : MiracleYoung
# @File    : test_func.py

# def testFun():
#     temp = [lambda x: i * x for i in range(4)]
#     return temp
#
#
# for everyLambda in testFun():
#     print(everyLambda(2))


# def testFun():
#     temp = [lambda x, i=i: i * x for i in range(4)]
#     return temp
#
#
# for everyLambda in testFun():
#     print(everyLambda(2))

# from functools import partial
# from operator import mul
#
#
# def testFun():
#     return [partial(mul, i) for i in range(4)]
#
#
# for everyLambda in testFun():
#     print(everyLambda(2))
#
#
# def testFun():
#     return (lambda x, i=i: i * x for i in range(4))
#
#
# for everyLambda in testFun():
#     print(everyLambda(2))
#
#
def testFun():
    for i in range(4):
        yield lambda x: i * x


for everyLambda in testFun():
    print(everyLambda(2))
