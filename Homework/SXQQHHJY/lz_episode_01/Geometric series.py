a1 = eval(input('请输入几何级数第一项的值'))
r = eval(input('请输入几何级数的公比'))
if r == 1:
    print('r不能为1')
n = eval(input('请输入几何级数共有多少项'))
if type(n) != int or n <= 0:
    print('几何级数的项需为大于0的整数')
else:
    Sn = a1 * ((r ** n - 1) / (r - 1))
    print('该几何级数的和为：%s' % Sn)
