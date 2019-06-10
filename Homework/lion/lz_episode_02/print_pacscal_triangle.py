# -*- coding: utf-8 -*-


def triangle():
    a = [1]
    while True:
        yield a
#         a.append(0)
#         a = [a[i - 1] + a[i] for i in range(len(a))]
        a = [sum(i) for i in zip([0] + a, a + [0])]


def main():
    row = int(input('请输入你要的值得行：'))
    column = int(input('请输入你要的值得列：'))

    n = 1
    current_row = list()
    for i in triangle():
        print(i)
        n += 1
        if n > row:
            current_row = i
            break
    print(current_row[column - 1])


if __name__ == '__main__':
    main()
