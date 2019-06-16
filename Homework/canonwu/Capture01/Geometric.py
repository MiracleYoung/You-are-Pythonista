#几何级数即一个等比数列的前N项和
num_first = int(input('请输入几何级数第一项的值'))
r = eval(input('请输入几何级数的公比'))
n = int(input('请输入几何级数共有多少项'))
if r == 1:
    Sn = num_first * n

if not isinstance(n, int) or n <= 0:
    raise ValueError('this value must be int which lg 0 expect')
else:
    Sn = num_first * ((r ** n - 1) / (r - 1))
    print('整数 %d 的几何级数的和为：%s' %(n, Sn))
