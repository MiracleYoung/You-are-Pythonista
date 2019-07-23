import functools
import random
import time

func_dic = {}


def cache(t):
    """ 设置过期时间 """
    def _times(func, *args, **kwargs):
        @functools.wraps(func)
        def _ca(*args, **kwargs):
            """ 未过期则返回已有结果 """
            if func_dic.get(func.__name__) and time.time() - func_dic[func.__name__].get("times", 0) < t:
                return func_dic[func.__name__]["reault"]
            reault = func(*args, **kwargs)
            func_dic[func.__name__] = {
                "times": time.time(),
                "reault": reault
            }
            return reault
        return _ca
    return _times


@cache(1.1)
def add(a, b):
    return a + b


@cache(2.6)
def sub(a, b):
    return a - b


def main():
    start_time = time.time()
    print("+", "----------------------+" * 3, sep="")

    rand_num = lambda: random.randint(0, 100)
    a = add(rand_num(), rand_num())
    b = sub(rand_num(), rand_num())
    print(f"|add func reault: {a: >4}", end="")
    print(f" | sub func reault: {b: >3} |{' '*22}|")
    print("+", "----------------------+" * 3, sep="")
    for i in range(100):
        time.sleep(0.1)
        x = add(rand_num(), rand_num())
        y = sub(rand_num(), rand_num())
        if (a, b) != (x, y):
            a, b = x, y
            print(f"|add func reault: {a: >4}", end="")
            print(f" | sub func reault: {b: >3} |", end="")
            passed_time = f"{time.time() - start_time:0.2f}"
            print(f" Time passed {passed_time: >5} s  |")
            print("+", "----------------------+" * 3, sep="")


if __name__ == "__main__":
    main()

    """ 结果:
    +----------------------+----------------------+----------------------+
    |add func reault:   74 | sub func reault:   6 |                      |
    +----------------------+----------------------+----------------------+
    |add func reault:   97 | sub func reault:   6 | Time passed  1.20 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  177 | sub func reault:   6 | Time passed  2.30 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  177 | sub func reault:  59 | Time passed  2.70 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  129 | sub func reault:  59 | Time passed  3.50 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  140 | sub func reault:  59 | Time passed  4.70 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  140 | sub func reault: -55 | Time passed  5.30 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  147 | sub func reault: -55 | Time passed  5.80 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  123 | sub func reault: -55 | Time passed  6.90 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  123 | sub func reault: -24 | Time passed  7.90 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  142 | sub func reault: -24 | Time passed  8.00 s  |
    +----------------------+----------------------+----------------------+
    |add func reault:  154 | sub func reault: -24 | Time passed  9.10 s  |
    +----------------------+----------------------+----------------------+
    """
