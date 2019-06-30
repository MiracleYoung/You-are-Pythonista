# 斐波那契数列，计算某个数范围内的斐波那契数列
num = int(input("please input an int:"))
lst = list(range(0,num))
F = lst
for x in lst:
    if x <= 1:
        F[x] = lst[x]
    else:
        F[x] = lst[x-1] + lst[x-2] # 斐波那契数列公式，经过不断循环，有新的赋值给到F和lst。
    print(F[x],end=' ')
print()
