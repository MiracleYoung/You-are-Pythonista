a = int(input("请输入首项a："))
q = int(input("请输入公比q："))
n = int(input("请输入项数n："))

sum = 0                 #sum 为和
for i in range(n):      #从0到n-1
    sum += a*(q**i)     #加上每一项
print('几何数级为：',sum)#输出和
