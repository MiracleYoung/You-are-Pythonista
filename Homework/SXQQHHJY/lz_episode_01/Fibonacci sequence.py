def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
n = eval(input('请输入斐波那契数列的项'))
if type(n) != int and n < 3:
    print('请输入大于3的整数')
else:
    print('斐波那契数列的第%d项为：%d' % (n ,f(n)))