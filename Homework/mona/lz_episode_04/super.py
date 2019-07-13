from types import MethodType
from functools import wraps
class Super:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, cls):
        @wraps(self.fn)
        def wrap(*args, **kwargs):
            ret = self.fn(*args, **kwargs)
            name = args[1]
            for ccls in cls.__mro__:
                if(hasattr(ccls, name)):
                    getattr(ccls, name)(instance)
                    break
            return ret

        if instance is not None:
            return MethodType(wrap, instance)

        return self

class C:
    def print(self):
        print('The class is C')

    def printC(self):
        print('The class is C')
class B:
    def print(self):
        print('The class is B')
class A(B,C):
    def __init__(self, x):
        pass
    @Super
    def super(self, name):
        print('You call the method of the parent class.')

a = A(1)
a.super('print')
a.super('printC')