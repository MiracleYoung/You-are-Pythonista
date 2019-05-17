# -*- coding: utf-8 -*-


# 递归求解第n项斐波那契数列值
def get_fibonacci_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci_recursion(n - 1) + get_fibonacci_recursion(n - 2)


def get_fibonaccibyloop(n):
    fibonacci_list = [1, 1]
    if n < 3:
        return fibonacci_list
    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    return fibonacci_list


def get_fibonaccibygenerator(n):
    a, b = 0, 1
    while n > 1:
        yield b
        a, b = b, a + b
        n -= 1


def main():
    # squence_list = list()
    # for i in range(1, 6):
    #     squence_list.append(get_fibonacci_recursion(i))

    # squence_list = get_fibonaccibyloop(5)

    squence_list = get_fibonaccibygenerator(10)
    for i in squence_list:
        print(i, end=' ')


if __name__ == '__main__':
    main()
