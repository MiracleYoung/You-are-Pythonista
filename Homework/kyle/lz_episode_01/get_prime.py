# 求100w以内的质数，先求10以内的质数
ret = []
for n in range(2,1000000):
    for x in range(2,n):
        if n % x == 0: # 如果n能被2到n的数整除，结束该层循环，后面的else语句不会被执行，继续上面的更大一层for循环
            break
    else:
        ret.append(n) # 如果不能整除，证明它是质数，并将其添加到列表中

print(ret)
