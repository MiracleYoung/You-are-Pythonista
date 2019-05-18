a = 0
b = 1
n = int(input("请输入斐波那契数列的项数："))
for i in range(n):
    a,b = b,a+b   #a+b 相加产生新斐波那契数
    print(a)
