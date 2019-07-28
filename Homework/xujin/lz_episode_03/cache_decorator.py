import functools
import time

def cache(seconds):
    cache_result = 0
    start_time = 0
    def _cache(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal cache_result,start_time
            print(f"{func.__name__} 距离上次执行时间过了 {time.time() - start_time} s了")
            if time.time() - start_time > seconds:
                start_time = time.time()
                cache_result = result = func(*args,**kwargs)
            else:
                print("我没有重新计算,在使用缓存中的值")
                result = cache_result
            return result
        return wrapper
    return _cache

@cache(3)
def get_sum_one_to_hundred():
    print("我在重新计算,没有使用缓存中的值")
    return sum([i for i in range(1,101)])


@cache(3)
def test():
    print("我在重新计算,没有使用缓存中的值")
    return 'test'

if __name__ == '__main__':
    print(get_sum_one_to_hundred())
    start_time = time.time()
    time.sleep(3)
    print(test())
    print(get_sum_one_to_hundred())
    print(test())
    time.sleep(2)
    print(get_sum_one_to_hundred())
    print(test())


