from functools import wraps
import inspect
import time


def cache(maxsize=128, expire=0):

    def make_signature(func, *args, **kwargs):
        key = list()   # 参数列表 (key, value)
        names = set()  # 参数名集合 -> 存放所有非默认值参数
        # 获取函数参数
        params = inspect.signature(func).parameters
        # 对应参数，值
        for index, arg in enumerate(args):
            k = list(params.keys())[index]
            key.append((k, arg))
            names.add(k)

        key.extend(kwargs.items())
        names.update(kwargs.keys())
        # 添加默认值参数
        for k, v in params.items():
            if k not in names:
                key.append((k, v.default))

        return '&'.join(f'{key}={val}' for key, val in key)

    def _cache(func):
        cache = dict()
        @wraps(func)
        def wrap(*args, **kwargs):
            signature_key = make_signature(func, *args, **kwargs)
            if signature_key in cache.keys():
                value,  timestamp, _ = cache[signature_key]
                if expire == 0 or time.time() - timestamp < expire:
                    cache[signature_key] = (value, timestamp, time.time())
                    print('using cache')
                    return value

            # 缓存是否超过最大限制：
            if len(cache) >= maxsize:
                cleared_func = list()
                # 记录过期函数
                for key, ret in cache.items():
                    if time.time() - ret[1] > expire:
                        # 记录key值
                        cleared_func.append(key)
                # 清除过期函数
                for key in cleared_func:
                    cache.pop(key)
            # 清楚最久未使用的函数
            if len(cache) >= maxsize:
                key = sorted(cache.items(), key=lambda x: x[1][2])[0]
                # print(key)
                cache.pop(key[0])

            ret = func(*args, **kwargs)
            cache[signature_key] = (ret, time.time(), time.time())  # 结果 执行时间 最后一次调用时间
            # time.sleep(1)
            print(cache)
            return ret
        return wrap
    return _cache


@cache(maxsize=3, expire=2)
def add(a, b, c, d=4):
    t = a + b
    return t


@cache()
def dde(a, b, c, d=4):
    t = a - b
    return t


print(add(1, 2, c=3))
print(add(1, 2, c=3))
print(add(3, 1, c=3))

print(add(4, 1, c=3))
print(add(6, 1, c=3))
print(add(5, 1, c=3))
