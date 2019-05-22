# 求100000内的质数
for i in range(1, 100001):
    j = 1
    while j*j <= i:
        j += 1
        if i % j == 0:
            break
    else:
        print(i, end=" ")