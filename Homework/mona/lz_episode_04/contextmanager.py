from functools import wraps


class Contextmanager:

    def __init__(self, fn):
        wraps(fn)(self)
        self.r = self.__wrapped__() # Ϊ�˸���try finally ���ص㣬Ҫ�������������Ϊ�ᴩ���������ʵ���������������Ƿ��ں������ڵľֲ�����

    def __call__(self, *args, **kwargs):
        return self  # ����֧�������Ĺ���Ķ���

    def __enter__(self):
        ret = self.r.__next__()  # ����yield��ֵ
        return ret

    def __exit__(self, *args):
        del self.r  # ɾ���ñ�������ִ����������������finally
        
@Contextmanager
def context():
    print('enter context')
    try:
        yield 'haha'
    finally:
        print('exit context')
        
with context() as c:
    print(c)