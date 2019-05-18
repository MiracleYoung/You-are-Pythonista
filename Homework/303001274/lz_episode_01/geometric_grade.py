# 求任意整数的几何级数
sum = 0
a = int(input("请输入首项a："))
q = int(input("请输入公比q："))
n = int(input("请输入项数n："))
sum += a
for i in range(2, n):
    sum += a * (q**i)
print(sum)
