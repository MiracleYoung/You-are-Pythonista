def Geometric_series(a,n,r = 2):
    total = 0
    for i in range(0,n):
        num = a * r ** i
        total += num
    return total


if __name__ == "__main__":
    a = input("请输入任意整数：")
    r = input("请输入公比：")
    n = input("请输入几何级数个数：")

    total = Geometric_series(int(a),int(n),int(r))
    print(total)