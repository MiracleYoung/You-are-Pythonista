from functools import wraps
import time

def cache(seconds):
    start_time = 0
    cache_result = 0
    def _cache(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache_result,start_time
            if time.time() - start_time > seconds:
                start_time=time.time()
                cache_result = func(*args, **kwargs)
            else:
                return "{}正在使用缓存中的值".format(func.__name__)
            return cache_result
        return wrapper
    return _cache

@cache(5)
def cached1():
    global start_time, cache_result
    start_time = time.time()
    cache_result = "cached1没有使用缓存中的值"
    return cache_result
@cache(5)
def cached2():
    global start_time, cache_result
    start_time = time.time()
    cache_result ="cached2没有使用缓存中的值"
    return cache_result

if __name__ == '__main__':
    print(cached1())
    print(cached2())
    time.sleep(2)
    print(cached1())
    print(cached2())
    time.sleep(2)
    print(cached1())
    print(cached2())
    time.sleep(2)
    print(cached1())
    print(cached2())