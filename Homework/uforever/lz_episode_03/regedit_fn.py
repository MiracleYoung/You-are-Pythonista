#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/6/15 21:38

__author__ = 'Uforever I'


from functools import wraps

dict_maths_fn={}

def register_f(fn):
    dict_maths_fn.update({fn.__name__:fn})
    print("The maths function ( {} ) is registered.".format(fn.__name__))
    @wraps(fn)
    def wrap(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return wrap

def maths_func():
    end = 'q'
    while True:
        c = input('>>请输入命令:')
        if c == end:
            break
        if c in dict_maths_fn:
            param = input('>>请输入参数:')
            params = param.split(',')
            t = []
            for v in params:
                t.append(int(v))
            print('>>结果:',dict_maths_fn[c](*t))
        else:
            print('抱歉！该命令没有被注册，无法使用。')


@register_f
def add(x,y,z=1):
    return x+y+z

@register_f
def multi(x,y=1):
    return x*y

maths_func()