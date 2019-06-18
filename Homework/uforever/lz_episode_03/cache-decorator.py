#!/usr/bin/env python
# encoding:utf-8
# @Time    : 2019/6/11 5:05

__author__ = 'Uforever I'

'''
写一个cache装饰器，允许过期。 
当某个函数被cache装饰器装饰过后，在过期时间内重复调用它，是返回的缓存结果，而不是去重新计算。
提示：过期时间可自定义，不用考虑换出策略。
'''

from functools import wraps
import inspect
import datetime
import time


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} called took {}'.format(fn.__name__, delta))
        return ret
    return wrapper

def py_cache(duration):
    def _cache(fn):
        local_cache = {} # 对不同函数名是不同的cache
        @wraps(fn)
        def wrapper(*args, **kwargs):
            def deal_expire(cache):
                # 根据需要决定使用缓存时是否清除过期的key
                expire_keys = []
                for k, (_, _, last) in cache.items():
                    stamp = datetime.datetime.now().timestamp()
                    time.sleep(last%last)
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration:
                        expire_keys.append(k)
                # 清除过期的key
                #for k in expire_keys:
                #    cache.pop(k)

            deal_expire(local_cache)

            def make_key():
                # 参数处理,构建key
                sig = inspect.signature(fn)
                params = sig.parameters
                param_names = list(params.keys())    #[key for key in params.keys()]
                param_dict = {} # 目标参数字典

                # 位置参数
                for i, v in enumerate(args):
                     k = param_names[i]
                     param_dict[k] = v

                # 关键字参数
                for k, v in kwargs.items():
                    param_dict[k] = v
                    param_dict.update(kwargs)

                # 缺省值处理
                for k, v in params.items():
                    if k not in param_dict.keys():
                        param_dict[k] = v.default

                return tuple(sorted(param_dict.items()))

            key = make_key()

            #print(key)
            #print(local_cache.keys())

            if key not in local_cache.keys():
                local_cache[key] = fn(*args, **kwargs)
                datetime.datetime.now().timestamp() # 时间戳

            return local_cache[key]

        return wrapper
    return _cache

@logger
@py_cache(10)
def add(x, z, y=6):
    time.sleep(3)
    return x,y,z

result = []
result.append(add(4, 5))
result.append(add(4, 5, 6))
result.append(add(4, z=6, y=5))
result.append(add(4, y=5, z=6))
result.append(add(x=4, y=5, z=6))
result.append(add(z=6, x=4, y=5))

for x in result:
    print(x)

time.sleep(15)
result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=6, z=5))
result.append(add(4, 6))
result.append(add(4, z=6))