"""
斐波那契数列
"""
def fib(num):
    def _fib(num):
        a, b = 1, 0
        for i in range(num):
            yield a
            a, b = a + b, a
    return [i for i in _fib(num)]

if __name__ == "__main__":
    n = 15
    print(fib(n))
    # 结果: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
