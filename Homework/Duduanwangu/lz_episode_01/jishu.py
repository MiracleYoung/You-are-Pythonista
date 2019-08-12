# 求任意整数的几何级数
def jishu(a, q, n):
    s = a * ((q**n - 1) / (q - 1))
    print(s)

jishu(1, 2, 3)
