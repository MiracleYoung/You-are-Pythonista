# -*- coding: utf-8 -*-
from functools import wraps
import time
import pickle
import hashlib


FUNC_VALUE = dict()


def hash_key(func_name, args, kwargs):
    """ 生成指纹，存放到字典中，判断该函数是否第一次计算 """
    # 将数据序列化成字节
    func_byte = pickle.dumps((func_name, args, kwargs))
    return hashlib.md5(func_byte).hexdigest()


def judge_time(expire_time, execute_time):
    """ 判断是否超出函数缓存时间 """
    current_time = time.time() - execute_time
    return current_time < expire_time


def cache(expire_time):  # expire_time 函数缓存的时间
    def _cache(func):
        @wraps(func)  # 保留函数原属性
        def wrap(*args, **kwargs):
            key = hash_key(func.__name__, args, kwargs)  # 不解包直接传递，减少函数迭代解包执行时间
            if key in FUNC_VALUE.keys() and judge_time(expire_time, FUNC_VALUE[key]['time']):
                print('使用缓存中的值')
                return FUNC_VALUE[key]['value']

            # result = func(*args, **kwargs)
            FUNC_VALUE[key] = {'value': func(*args, **kwargs), 'time': time.time()}
            return FUNC_VALUE[key]['value']
        return wrap
    return _cache

# 初始化时，设置缓存时间
@cache(1)
def add(x, y):
    return x + y


def main():
    print(add(1, 2))
    print(add(1, 2))
    time.sleep(2)
    print(add(1, 2))
    print(add(2, 3))
    print(FUNC_VALUE)


if __name__ == '__main__':
    main()
