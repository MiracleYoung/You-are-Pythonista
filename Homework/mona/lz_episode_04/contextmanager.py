from functools import wraps


class Contextmanager:

    def __init__(self, fn):
        wraps(fn)(self)
        self.r = self.__wrapped__() # 为了复合try finally 的特点，要把这个生成器作为贯穿整个对象的实例变量，而不是是放在函数体内的局部变量

    def __call__(self, *args, **kwargs):
        return self  # 返回支持上下文管理的对象

    def __enter__(self):
        ret = self.r.__next__()  # 返回yield的值
        return ret

    def __exit__(self, *args):
        del self.r  # 删除该变量，以执行生成器函数最后的finally
        
@Contextmanager
def context():
    print('enter context')
    try:
        yield 'haha'
    finally:
        print('exit context')
        
with context() as c:
    print(c)