def func(n):
    if n <=1:
        return n
    else:
        return func(n-2) + func(n-1)


if __name__ == "__main__":
    n = input("请输入展示的数列个数：")
    for i in range(0,int(n)):
        print(func(i))