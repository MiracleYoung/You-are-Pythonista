"""
用类实现一个contextlib.contextmanager装饰器
"""
from functools import wraps


class CONTEXTMANAGER:

    def __init__(self, fn):
        wraps(fn)(self)
        self.wrap = self.__wrapped__()

    def __call__(self, *args, **kwargs):
        return self

    def __enter__(self):
        ret = self.wrap.__next__()  # 返回yield的值
        return ret

    def __exit__(self, *args, **kwargs):
        del self.wrap  # 删除该变量，以执行生成器函数最后的finally


@CONTEXTMANAGER
def context():
    print('enter context')
    try:
        yield 'haha'
    finally:
        print('exit context')


with context() as cc:
    # raise Exception
    print(cc)
