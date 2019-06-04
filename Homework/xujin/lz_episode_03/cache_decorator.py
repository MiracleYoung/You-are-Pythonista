import functools
import time

start_time = 0
cache_result = 0

def cache(seconds):
    def _cache(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if time.time() - start_time > seconds:
                result = func(*args,**kwargs)
            else:
                print("我没有重新计算,在使用缓存中的值")
                result = cache_result
            return result
        return wrapper
    return _cache

@cache(3)
def get_sum_one_to_hundred():
    global start_time,cache_result
    start_time = time.time()
    print("我在重新计算,没有使用缓存中的值")
    cache_result = sum([i for i in range(1,101)])
    return cache_result

if __name__ == '__main__':
    print(get_sum_one_to_hundred())
    time.sleep(2)
    print(get_sum_one_to_hundred())
    time.sleep(2)
    print(get_sum_one_to_hundred())