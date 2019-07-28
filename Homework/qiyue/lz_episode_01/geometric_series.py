# encoding: utf-8
a1 = float(input("请输入等比数列首项a1："))
q = float(input("请输入公比q："))
n = float(input("请输入项数n："))
if q != 1:
    sum=(a1*q**n-a1)/(q-1)
elif q==1:
    sum=n*a1
print("该等比数列的和为：" + str(sum))

