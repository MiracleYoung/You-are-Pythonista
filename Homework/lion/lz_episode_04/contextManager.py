# -*- coding: utf-8 -*-
from functools import wraps


class ContextManager:
    # 对函数进行装饰 需要把函数传递进来 函数是一个生成器
    def __init__(self, func, *args, **kwargs):
        self.gen = func(*args, **kwargs)

    # def __call__(self, *args, **kwargs):
    #     # 函数被装饰器装饰以后 原来的函数变量指向了ContextManager的一个实例变量 函数在实例变量的属性中存放
    #     self.gen = self.fn(*args, **kwargs)  # 执行函数 接受生成器的值
    #     return self

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, *args, **kwargs):
        # 执行finall块中的内容
        try:
            return next(self.gen)
        except StopIteration:
            return False


def contextmanager(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        # fn(*args, **kwargs)
        return ContextManager(fn, *args, **kwargs)
    return wrap


@contextmanager
def context():
    """ context 的有关内容 """
    try:
        yield 'value'
    finally:
        print('cleanup')


def main():
    with context() as val:
        print(val)
    help(context)


if __name__ == '__main__':
    main()
