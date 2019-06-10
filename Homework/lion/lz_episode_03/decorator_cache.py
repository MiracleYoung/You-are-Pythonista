# -*- coding: utf-8 -*-


FUNC_VALUE = dict()


def cache(times):  # times 自定期过期参数，第一次计算之后的times次数以内返回缓存结果
    # 记录函数缓存时间
    nums = times

    def _cache(func):
        def wrap(*args, **kwargs):
            nonlocal times
            # 第一次执行时，计次已经开始
            # 当次数为0时，表明缓存时间已经到期需要重新计算函数结果
            if times == 0:
                result = func(*args, **kwargs)
                FUNC_VALUE[func] = result
                times = nums - 1  # 重新设置过期时间
                return result
            else:
                if nums == times:  # 说明函数第一次调用
                    times -= 1
                    result = func(*args, **kwargs)
                    FUNC_VALUE[func] = result
                    return result
                else:  # 不是第一次调用 返回缓存的结果
                    times -= 1
                    return FUNC_VALUE[func]
        return wrap
    return _cache


@cache(3)
def add(x, y):
    return x + y


@cache(3)
def sum(x, y):
    return x * y


def main():
    print(add(1, 2))
    print(add(2, 2))
    print(add(3, 2))
    print(add(4, 2))
    print(sum(1, 2))
    print(sum(2, 2))
    print(sum(2, 2))
    print(sum(3, 2))
    print(sum(2, 2))


if __name__ == '__main__':
    main()
