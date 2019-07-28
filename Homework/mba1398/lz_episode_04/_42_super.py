"""
用类实现一个super()函数
"""
from types import MethodType
from functools import wraps


class SUPER:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        @wraps(self.fn)
        def wrap(*args, **kwargs):
            ret = self.fn(*args, **kwargs)
            name = args[1]
            for item in owner.__mro__:
                if hasattr(item, name):
                    getattr(item, name)(instance)
                    break
            return ret

        if instance is not None:
            return MethodType(wrap, instance)

        return self


class C:

    def print(self):
        print('class C')

    def print_c(self):
        print('class C')


class B:
    def print(self):
        print('class B')


class A(B, C):
    def __init__(self, name):
        pass

    @SUPER
    def super(self, name):
        print('Called the class: ')


a = A(1)
a.super('print')
a.super('print_c')

