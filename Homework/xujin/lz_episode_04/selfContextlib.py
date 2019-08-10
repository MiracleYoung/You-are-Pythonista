from functools import wraps
# from contextlib import contextmanager

class SelfContextManager():
    def __init__(self,func,*args,**kwargs):
        self.gen = func(*args,**kwargs)

    # def __call__(self, *args, **kwargs):
    #     self.gen = self.func(*args,*kwargs)
    #     return self

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            return next(self.gen)
        except StopIteration as e:
            return False

# 写一个函数装饰器是为了保持函数的属性不会被改变
def contextmanager(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        return SelfContextManager(fn,*args,**kwargs)
    return inner

@contextmanager
def add(x,y):
    '''
    example context
    :param x:
    :param y:
    :return:
    '''
    print("enter ....")
    try:
        yield x+y
    finally:
        print("exit ...")

if __name__ == '__main__':
    help(add)
    with add(3,4) as result:
        print(result)

