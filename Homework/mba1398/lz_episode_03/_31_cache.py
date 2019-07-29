# -*- encoding: utf-8 -*-
"""
装饰器
20190528
"""

import time
import hashlib #对函数返回值使用摘要算法，快速判别是否已经计算过
import pickle  #序列化对象并保存到磁盘中，并在需要的时候读取出来
import functools

cache_dict = {}
# 初始化cache


def is_expired(entry, expired_time):
    d = time.time() - entry['time']
    return d > expired_time


def compute_key(function, args, kwargs):
    key = pickle.dumps((function, args, kwargs))
    # 获取‘函数名称、位置参数、关键字参数组成的字符串’的序列化结果
    print((function, args, kwargs))
    print(key)
    return hashlib.md5(key).hexdigest()
    # 使用摘要算法对序列化结果进行计算，以便快速判断是否计算过（基于函数名称、函数参数构成的字符串进行序列化，并非对计算结果序列化）


def cache(expired_time):
    def _cache(func):
        # @functools.wraps(func)
        def wrap(*args, **kwargs):
            key = compute_key(func.__name__, args, kwargs)
            if key in cache_dict and not is_expired(cache_dict[key], expired_time):
                print('Just use values in cache!')
                return cache_dict[key]['value']
            result = func(*args, **kwargs)
            cache_dict[key] = {'value': result, 'time': time.time()}  # 摘要算法结果作为字典的key，
                                                                      # 函数计算结果和时间构成的字段作为key的value
            print(cache_dict)
            return result
        return wrap
    return _cache


@cache(3)
def add(x, y):
    time.sleep(2)
    return x + y


print(add(1, 2))
time.sleep(2)
print(add(1, 2))
time.sleep(2)
print(add(1, 3))
# print(hashlib.md5(pickle.dumps('add,1,2')).hexdigest())
# print(pickle.dumps((function, args, kwargs)))
# add(1, 2)
# def fib(n):
#     if n <= 2:
#         return 1
#     caches = fib(n-1) + fib(n-2)
#     return caches


# fib_cache = cache(fib)

# print(fib(13))
# print(fib_cache(13))

