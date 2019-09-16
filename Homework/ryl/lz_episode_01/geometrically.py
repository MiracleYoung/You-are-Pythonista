# 求整数的几何级数
# 等比数列求和公式： Sn = a(1-q**n)/(1-q)

print('几何级数')
a = int(input('a:'))
q = int(input('q:'))
n = int(input('n:'))

sum = a*(1-q**n)/(1-q)

print(sum)
